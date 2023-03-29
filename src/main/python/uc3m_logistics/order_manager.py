"""Module """
import re
import os
import json
from pathlib import Path
from uc3m_logistics import order_request
from uc3m_logistics import order_management_exception
from uc3m_logistics import order_shipping
from datetime import datetime
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

    @property
    def store_path(self):
        # Path
        path = os.path.dirname(__file__)
        path = path[:-26]
        return os.path.join(path, "json")
    def register_order(self, productID, orderType, address, phoneNumber, zipCode):

        # INPUT VALIDATION
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
        if (len(zipCode) != 5):
            raise order_management_exception.OrderManagementException("Exception : zipcode not valid")
        try:
            aux_zip_code = int(zipCode)
            if (not (1000 <= aux_zip_code < 53000)):
                raise order_management_exception.OrderManagementException("Exception : zipcode doesn't exists")
        except:
            raise order_management_exception.OrderManagementException("Exception : zipcode not valid")

        # GENERATES REQUEST
        ord_requ = order_request.OrderRequest(productID, orderType, address, phoneNumber, zipCode)
        out = ord_requ.order_id

        # OPENS THE STORE_FILE. IF NOT EXISTS CREATES IT
        try:
            with open(self.store_path + "/Almacen.JSON", "r", encoding="utf-8") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []

        ## adds the hash to the file
        data_list.append(ord_requ.__dict__)
        data_list[-1]["_OrderRequest__order_id"] = out

        # WRITES EVERYTTHING ON STORE_FILE
        with open(self.store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
            json.dump(data_list, file, indent=2)

        # returns hash
        return out

    def send_code(self, input_file):

        file_store = self.store_path + "/Almacen.JSON"
        if not os.path.isfile(file_store):
            raise order_management_exception.OrderManagementException("There isn't any store")
        ###### Falta hacer las comprobaciones de la función
        #### Para comprobar que no está manipulado hay que volver a crear el OrderId con los datos del almacen
        #### Para esto hay que congelar el tiempo con el tiempo del almacén o crear un nuevo objeto con los atributos
        #### obtenidos en el almacén y forzar a que el tiempo sea el del antiguo / Creo que hecho

        ##### Revisar que el formato con el que se escribe en el JSON es el que se utiliza para indexar
        try:
            with open(file_store, "r", encoding="utf8") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        try:
            with open(input_file, "r", encoding="utf8") as file:
                dicc_json = json.load(file)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        claves = tuple(dicc_json.keys())
        print(claves)
        if len(claves) != 2:
            raise order_management_exception.OrderManagementException("There are too/few keys")
        if claves[0] != "OrderID":
            raise order_management_exception.OrderManagementException("Incorrect keys")
        if claves[1] != "ContactEmail":
            raise order_management_exception.OrderManagementException("Incorrect keys")
        if not re.fullmatch('^[0-9|a-f]{32}$', dicc_json["OrderID"]):
            raise order_management_exception.OrderManagementException("Wrong Hash")
        if not re.fullmatch('^[0-9|a-z][0-9|a-z]*[@][0-9|a-z][0-9|a-z]*[.][0-9|a-z][0-9|a-z]*$', dicc_json["ContactEmail"]):
            raise order_management_exception.OrderManagementException("Wrong Contact Email")

        try:
            for item in data_list:
                if item["_OrderRequest__order_id"] == dicc_json["OrderID"]:
                    #print(item)
                    product_id = item["_OrderRequest__product_id"]
                    order_id = item["_OrderRequest__order_id"]
                    delivery_email = dicc_json["ContactEmail"]
                    order_type = item["_OrderRequest__order_type"]
                    print(order_shipping.OrderShipping(product_id, order_id, delivery_email, order_type))
                    ord_shi = order_shipping.OrderShipping(product_id, order_id, delivery_email, order_type)
                    out = ord_shi.tracking_code
                    print("out =" + str(out))
                    ##################Falta escribir el tracking code = out en el almacén / Hecho
                    item["_OrderRequest__delivery_day_"] = ord_shi.delivery_day
                    item["_OrderRequest__tracking_code_"] = out
                    with open(self.store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                        json.dump(data_list, file, indent=2)
                    req = order_request.OrderRequest(product_id, order_type,
                                                     item["_OrderRequest__delivery_address"],
                                                     item["_OrderRequest__phone_number"],
                                                     item["_OrderRequest__zip_code"])
                    req.time_stamp = item["_OrderRequest__time_stamp"]
                    real_hash = req.order_id

                    if real_hash != dicc_json["OrderID"]:
                        raise order_management_exception.OrderManagementException("The hash has been manipulated")
                    return out
        except:
            raise order_management_exception.OrderManagementException("Your OrderId doesn't exist")
    def send_product(self,tracking_number):
        file_store = self.store_path + "/Almacen.JSON"
        if not os.path.isfile(file_store):
            raise order_management_exception.OrderManagementException("There isn't any store")
        if not re.fullmatch('^[0-9|a-f]{64}$', tracking_number):
            raise order_management_exception.OrderManagementException("Wrong Hash")
        try:
            with open(file_store, "r", encoding="utf8") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format")
        for item in data_list:
            if item["_OrderRequest__tracking_code_"] == tracking_number:
                if item["_OrderRequest_delivery_day_"] != datetime.timestamp(datetime.utcnow()):
                    raise order_management_exception.OrderManagementException("The delivery day isn't today")
                with open(self.store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                    json.dump(data_list, file, indent=2)




