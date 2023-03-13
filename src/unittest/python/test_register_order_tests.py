"""class for testing the regsiter_order method"""
import unittest
from freezegun import freeze_time
from uc3m_logistics import order_manager, OrderManagementException
from uc3m_logistics import order_request
@freeze_time("01-01-1900")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, False)

    @freeze_time("01-01-1900 00:00:00")
    def test_f1_Vt1(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("45a77da7acc49cc551fab69cb6e2ce4b",value)

    def test_f1_NVt1(self):
        my_order = order_manager.OrderManager()

        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322A", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

if __name__ == '__main__':
    unittest.main()