"""Module """
import hashlib
import re
from uc3m_logistics import order_request
from uc3m_logistics import order_management_exception


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

        if orderType.upper() != "REGULAR" or orderType.upper() != "PREMIUM":
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
        return out
