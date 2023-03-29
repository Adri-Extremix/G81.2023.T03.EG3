"""class for testing the regsiter_order method"""
import json
import unittest
import os
from freezegun import freeze_time
from uc3m_logistics import order_manager, order_management_exception

store_path = os.path.dirname(__file__)[:-15] + "json"


@freeze_time("01-01-2000")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def setUp(self) -> None:
        a = order_manager.OrderManager()
        file_store = a.store_path + "/Almacenf1.JSON"
        if os.path.isfile(file_store):
            os.remove(file_store)

    @freeze_time("01-01-2000 00:00:00")
    def test_f3_Vt1(self):
        input_file = store_path + "/f3_vt1.json"
        if os.path.isfile(store_path + "/Almancen.JSON"):
            os.remove(store_path + "/Almacenf1.JSON")
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
            with open(store_path + "/Almacenf1.JSON", "w", encoding="utf-8", newline="") as file:
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

        if data_list[-1]["_OrderRequest__order_id"] == value:
            found = True
        self.assertTrue(found)
