"""class for testing the regsiter_order method"""
import json
import unittest
import os
from pathlib import Path
from freezegun import freeze_time
from uc3m_logistics import order_manager, order_management_exception
from uc3m_logistics import order_request

@freeze_time("01-01-1900")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def setUp(self) -> None:
        file_store = str(Path.home()) + "/home/adrian/PycharmProjects/G81.2023.T03.EG3/src/Json/Store/store.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, False)

    @freeze_time("01-01-1900 00:00:00")
    def test_f1_Vt1(self):
        # caso válido all corect
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("45a77da7acc49cc551fab69cb6e2ce4b",value)

        with(open("../../json/Almacen.JSON", "r", encoding="utf-8", newline=""))as file:
            data_list = json.load(file)
        found = False

        if data_list[-1]["_OrderRequest__order_id"] == "45a77da7acc49cc551fab69cb6e2ce4b":
            found = True
        self.assertTrue(found)

    def test_f1_NVt1(self):
        # not num
        my_order = order_manager.OrderManager()

        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("842169142322A", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt2(self):
        # check sum
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423225", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt3(self):
        # too long
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("80421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt4(self):
        # too short
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("842169142322", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)

    def test_f1_NVt5(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order(8421691423220, "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: Product Id not valid", cm.exception.message)
    ############Cambiar comentarios de los métodos a partir de aquí #############
    def test_f1_Vt2(self):
        # caso válido all corect
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("1529a75ad4abd5bafdc2981bd2d648e0",value)

        with(open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "1529a75ad4abd5bafdc2981bd2d648e0":
                found = True
        self.assertTrue(found)

    def test_f1_NVt6(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "OTHER", "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception: orderType type not valid", cm.exception.message)

    def test_f1_NVt7(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", 7, "C/LISBOA,4, MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("Exception : order type not valid", cm.exception.message)

    def test_f1_Vt3(self):
        # caso válido all corect
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4,MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("23505258223f8d9da00641c25ef3dd47",value)

        with(open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "23505258223f8d9da00641c25ef3dd47":
                found = True
        self.assertTrue(found)
    def test_f1_NVt8(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4,MADRID,SPAIN", "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_Vt4(self):
        # caso válido all corect
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBO MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("0d79d3a8bb1008bcd10120b7f9ececfb", value)

        with(open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "0d79d3a8bb1008bcd10120b7f9ececfb":
                found = True
        self.assertTrue(found)

    def test_f1_Vt5(self):
        # caso válido all corect
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA MADRID, SPAIN", "123456789", "28005")
        self.assertEqual("b79f15b28ca404f0aab3cbea1911a38c", value)

        with(open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "b79f15b28ca404f0aab3cbea1911a38c":
                found = True
        self.assertTrue(found)

    def test_f1_Vt6(self):
        # caso válido all corect
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaa"
                                                                        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                        "aaaaaaa", "123456789", "28005")
        self.assertEqual("f8453670d7bcd85d4c2caa7aff980aca", value)

        with(open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "f8453670d7bcd85d4c2caa7aff980aca":
                found = True
        self.assertTrue(found)

    def test_f1_Vt7(self):
        # caso válido all corect
        my_order = order_manager.OrderManager()
        value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaAaa"
                                                                    , "123456789", "28005")
        self.assertEqual("911bae296cfa927e0e81b4de9adce30b", value)

        with(open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "911bae296cfa927e0e81b4de9adce30b":
                found = True
        self.assertTrue(found)

    def test_f1_NVt9(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "BOA,4, MADRID, PAIN", "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_NVt10(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAINaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                                                                , "123456789", "28005")
        self.assertEqual("Exception : address not valid", cm.exception.message)

    def test_f1_NVt11(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", 42, "123456789", "28005")
        self.assertEqual("Exception : address not a string", cm.exception.message)

    def test_f1_NVt12(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "12345678", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt13(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "1234567890", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt14(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", 123456789, "28005")
        self.assertEqual("Exception : phone_number type not valid", cm.exception.message)

    def test_f1_NVt15(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "12345A789", "28005")
        self.assertEqual("Exception : phone_number not valid", cm.exception.message)

    def test_f1_NVt16(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "2800")
        self.assertEqual("Exception : zip_code not valid", cm.exception.message)

    def test_f1_NVt17(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "280051")
        self.assertEqual("Exception : zip_code not valid", cm.exception.message)

    def test_f1_NVt18(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "53005")
        self.assertEqual("Exception : zip_code doesn't exists", cm.exception.message)

    def test_f1_NVt19(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", "2A005")
        self.assertEqual("Exception : zip_code not valid", cm.exception.message)

    def test_f1_NVt20(self):
        # not string
        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.register_order("8421691423220", "REGULAR", "C/LISBOA,4, MADRID, SPAIN", "123456789", 28991)
        self.assertEqual("Exception : zip_code not valid", cm.exception.message)


if __name__ == '__main__':
    unittest.main()