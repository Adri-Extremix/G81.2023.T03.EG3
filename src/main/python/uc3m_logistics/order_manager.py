"""Module """
import hashlib
from uc3m_logistics import order_request


class OrderManager:
    """Class for providing the methods for managing the orders"""
    def init(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        """RETURNs TRUE IF THE CODE RECEIVED IS A VALID EAN13,
        OR FALSE IN OTHER CASE"""
        return True
    def register_order(self, productID, orderType, address, phoneNumber, zipCode):
        if not self.validate_ean13(productID):
            raise #t0d0
        ord_requ = order_request.OrderRequest(productID, orderType, address, phoneNumber, zipCode)
        out = ord_requ.order_id
        return out
