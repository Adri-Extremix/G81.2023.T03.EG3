"""class for testing the regsiter_order method"""
import json
import unittest
import os
from pathlib import Path
from freezegun import freeze_time
from uc3m_logistics import order_manager, order_management_exception
from uc3m_logistics import order_request

store_path = os.path.dirname(__file__)[:-15] + "json"
print("path: " + store_path)

@freeze_time("01-01-1900")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, False)

    @freeze_time("01-01-1900 00:00:00")
    def test_f2_Vt1(self):
        # elimniar el almacen
        input_file = store_path + "/f2_vt1.json"
        if os.path.isfile(store_path + "/Almancen.JSON"):
            print("por aquí pasa")
            os.remove(store_path + "/Almacen.JSON")
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": 946684800.0,
                    "_OrderRequest__order_id": "e39ed19e25d6c4f0b2ed5bf610e043b4"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        #### Falta borrar y crear el almacen
        my_order = order_manager.OrderManager()
        ########## Falta dar la dirección del json
        value = my_order.send_code(input_file)
        self.assertEqual("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0",value)

    def test_f2_NVt1(self):
        # elimniar el almacen
        input_file = store_path + "/f2_nvt1.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
            os.remove(store_path + "/Almacen.JSON")
        # Orden de ejemplo en el almacen
        dicc_json = []
        order_ex = {"_OrderRequest__product_id": "8421691423220",
                    "_OrderRequest__delivery_address": "C/LISBOA,4, MADRID, SPAIN",
                    "_OrderRequest__order_type": "REGULAR",
                    "_OrderRequest__phone_number": "123456789",
                    "_OrderRequest__zip_code": "28005",
                    "_OrderRequest__time_stamp": -2208988800.0,
                    "_OrderRequest__order_id": "45a77da7acc49cc551fab69cb6e2ce4b"}
        dicc_json.append(order_ex)
        try:
            with open(store_path + "/Almacen.JSON", "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex
        except json.JSONDecodeError as ex:
            raise order_management_exception.OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)



if __name__ == '__main__':
    unittest.main()