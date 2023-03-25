"""class for testing the regsiter_order method"""
import json
import unittest
import os
from freezegun import freeze_time
from uc3m_logistics import order_manager, order_management_exception

@freeze_time("01-01-1900")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def setUp(self) -> None:
        a = order_manager.OrderManager()
        file_store = a.store_path + "Almacen.JSON"
        if os.path.isfile(file_store):
            os.remove(file_store)

    @freeze_time("01-01-1900 00:00:00")
    def test_f1_Vt1(self):

        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("45a77da7acc49cc551fab69cb6e2ce4b",value)

        with(open("../../json/Almacen.JSON", "r", encoding="utf-8", newline=""))as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_NVt1(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("842169142322A", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt2(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423225", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt3(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("80421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt4(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("842169142322", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt5(self):

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order(8421691423220, "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id type not valid", cm.exception.message)
    def test_f1_Vt2(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("1529a75ad4abd5bafdc2981bd2d648e0",value)

        with(open("../../json/Almacen.JSON", "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)
    def test_f1_NVt6(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "OTHER", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: orderType not valid", cm.exception.message)

    def test_f1_NVt7(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", 7, "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: orderType type not valid", cm.exception.message)

    def test_f1_Vt3(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4,MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("23505258223f8d9da00641c25ef3dd47",value)

        with(open("../../json/Almacen.JSON", "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)
    def test_f1_NVt8(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4,MADRID,SPAIN", "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_Vt4(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBO MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("0d79d3a8bb1008bcd10120b7f9ececfb", value)

        with(open("../../json/Almacen.JSON", "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_Vt5(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("b79f15b28ca404f0aab3cbea1911a38c", value)

        with(open("../../json/Almacen.JSON", "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_Vt6(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaa"
                                                                        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                        "aaaaaaa", "123456789", "28005")
        self.assertEqual("f8453670d7bcd85d4c2caa7aff980aca", value)

        with(open("../../json/Almacen.JSON", "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_Vt7(self):
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAaa"
                                                                    , "123456789", "28005")
        self.assertEqual("911bae296cfa927e0e81b4de9adce30b", value)

        with(open("../../json/Almacen.JSON", "r", encoding="utf-8", newline="")) as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)

    def test_f1_NVt9(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "BOA,4, MADRID, PAIN", "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_NVt10(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                , "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_NVt11(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", 42, "123456789", "28005")
        self.assertEqual("Exception : address type not valid", cm.exception.message)

    def test_f1_NVt12(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "12345678", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt13(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "1234567890", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt14(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", 123456789, "28005")
        self.assertEqual("Exception : phone_number type not valid", cm.exception.message)

    def test_f1_NVt15(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "12345A789", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt16(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "2800")
        self.assertEqual("Exception : zipcode not valid", cm.exception.message)

    def test_f1_NVt17(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "280051")
        self.assertEqual("Exception : zipcode not valid", cm.exception.message)

    def test_f1_NVt18(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "53005")
        self.assertEqual("Exception : zipcode not valid", cm.exception.message)

    def test_f1_NVt19(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "2A005")
        self.assertEqual("Exception : zipcode not valid", cm.exception.message)

    def test_f1_NVt20(self):
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", 28991)
        self.assertEqual("Exception : zipcode type not valid", cm.exception.message)


if __name__ == '__main__':
    unittest.main()