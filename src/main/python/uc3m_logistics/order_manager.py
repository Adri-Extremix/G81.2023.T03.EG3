"""Module """
import re
import os
import json
from pathlib import Path
from uc3m_logistics import order_request
from uc3m_logistics import order_management_exception
from uc3m_logistics import order_shipping
from freezegun import freeze_time


class OrderManager:
    """Class for providing the methods for managing the orders"""

    def init(self):
        pass

    @staticmethod
    def validate_ean13(ean13):
        """Receives a barcode and validates it checking the
        control digit.
        Algorithm:
        https://es.wikipedia.org/wiki/European_Article_Number#Estructura_y_partes
        :param eAn13: barcode
        :return: boolean
        """

        if not re.fullmatch('^[0-9]{13}$', ean13):
            return False
        sum_odd = 0
        sum_even = 0

        for i in range(len(ean13) - 1):
            # not equal to correct the index starting.
            # Should start in 1.
            sumando = int(ean13[i])
            if i % 2 != 0:
                sum_even += sumando
            else:
                sum_odd += sumando
        sum_even *= 3
        validation = (10 - ((sum_odd + sum_even) % 10)) % 10
        if int(ean13[-1]) != validation:
            return False

        return True

    @staticmethod
    def validate_address(address):
        """ """
        if len(address) < 20 or len(address) > 100:
            return False
        cont_sp = 0

        for i in range(len(address)):
            if address[i] == ' ':
                cont_sp += 1

        if cont_sp < 1:
            return False
        return True

    def register_order(self, productID, orderType, address, phoneNumber, zipCode):

        if type(productID) != str:
            raise order_management_exception.OrderManagementException("Exception: Product Id type not valid")

        if not self.validate_ean13(productID):
            raise order_management_exception.OrderManagementException("Exception: Product Id not valid")

        if type(orderType) != str:
            raise order_management_exception.OrderManagementException("Exception: orderType type not valid")

        if orderType.upper() != "REGULAR" and orderType.upper() != "PREMIUM":
            raise order_management_exception.OrderManagementException("Exception: orderType not valid")

        if type(address) != str:
            raise order_management_exception.OrderManagementException("Exception : address type not valid")

        if not self.validate_address(address):
            raise order_management_exception.OrderManagementException("Exception : address not valid")

        if not isinstance(phoneNumber, str):
            raise order_management_exception.OrderManagementException("Exception : phone_number type not valid")

        if len(phoneNumber) != 9:
            raise order_management_exception.OrderManagementException("Exception : phone_number not valid")

        try:
            int(phoneNumber)
        except:
            raise order_management_exception.OrderManagementException("Exception : phone_number not valid")

        if not isinstance(zipCode, str):
            raise order_management_exception.OrderManagementException("Exception : zipcode type not valid")
        try:
            aux_zip_code = int(zipCode)
            if (not (1000 <= aux_zip_code < 53000)):
                raise order_management_exception.OrderManagementException("Exception : zipcode doesn't exists")
        except:
            raise order_management_exception.OrderManagementException("Exception : zipcode not valid")




        ord_requ = order_request.OrderRequest(productID, orderType, address, phoneNumber, zipCode)
        out = ord_requ.order_id
        path = os.path.dirname(__file__)
        path = path[:-26]
        print(path)
        path = os.path.join(path, "json")
        print(path)


        try:
            with open(path + "/Almacen.JSON", "r", encoding="utf-8") as file:
                #data = json.load(file)
                #print(data)
                data_list = json.load(file)



        except FileNotFoundError as ex:
            print("por aquí todo ok")
            data_list = list();

        data_list.append(ord_requ.__str__())
        print(data_list)

        with open(path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(data_list, file, indent=2)
        return out

    def send_code(self, json):
        ########## Tiene que guardar el tracking code en el almacén / Hecho

        ##### Falta obtener la dirección del almacén /Creo que hecho
        file_store = str(Path.home()) + "/PycharmProjects/G81.2023.T03.EG3/src/Json/Store/store.json"
        if not os.path.isfile(file_store):
            raise order_management_exception.OrderManagementException("There isn't any store")
        ###### Falta hacer las comprobaciones de la función
        #### Para comprobar que no está manipulado hay que volver a crear el OrderId con los datos del almacen
        #### Para esto hay que congelar el tiempo con el tiempo del almacén o crear un nuevo objeto con los atributos
        #### obtenidos en el almacén y forzar a que el tiempo sea el del antiguo / Creo que hecho

        ##### Revisar que el formato con el que se escribe en el JSON es el que se utiliza para indexar
        try:
            with open(file_store, encoding="utf8") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        try:
            with open(json, encoding="utf8") as file:
                dicc_json = json.load(file)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        try:
            for item in data_list:
                if item["_OrderRequest__OrderId_"] == dicc_json["_OrderRequest__OrderId_"]:
                    product_id = dicc_json["_OrderRequest__Product_Id_"]
                    order_id = dicc_json["_OrderRequest__Order_Id_"]
                    delivery_email = dicc_json["_OrderRequest__DeliveryEmail_"]
                    order_type = dicc_json["_OrderRequest__Order_Type_"]
                    ord_shi = order_shipping.OrderShipping(product_id, order_id, delivery_email, order_type)
                    out = ord_shi.tracking_code
                    ##################Falta escribir el tracking code = out en el almacén / Hecho
                    item["_OrderRequest_tracking_code_"] = out

                    # # Con esto se debería poder parar el tiempo parar el tiempo a la hora de llamar a la función
                    # del hash
                    my_freeze = freeze_time(item["_OrderRequest__Time_Stamp_"])
                    my_freeze.start()
                    req = order_request.OrderRequest(product_id, order_type,
                                                     dicc_json["_OrderRequest__Delivery_Address_"],
                                                     dicc_json["_OrderRequest__Phone_Number_"],
                                                     dicc_json["_OrderRequest__Zip_Code_"])
                    real_hash = req.order_id
                    if real_hash != dicc_json["OrderRequest__Order_Id"]:
                        raise order_management_exception.OrderManagementException("The hash has been manipulated")
                    # hash.time_stamp si no funciona el freeze utilizar el atributo privado para asignarlo a un nuevo
                    # objeto
                    my_freeze.stop()

                    return out
        except:
            raise order_management_exception.OrderManagementException("Your OrderId doesn't exist")
