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

@freeze_time("01-01-2000")
class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""

    @freeze_time("01-01-2000 00:00:00")
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
        """Duplicación de format"""
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt2(self):
        """deletion de format"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt3.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt3(self):
        """duplication de llavein"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt3.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt4(self):
        """deletion de llavein"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt4.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt5(self):
        """dup de datos"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt5.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt6(self):
        """del de datos"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt6.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("There are too/few keys", cm.exception.message)

    def test_f2_NVt7(self):
        """dup llavefin"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt7.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt8(self):
        """del llavefin"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt8.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt9(self):
        """mod de llave inicio"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt9.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt10(self):
        """dup de parte1"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt10.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt11(self):
        """del de parte1"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt11.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("There are too/few keys", cm.exception.message)

    def test_f2_NVt12(self):
        """dup de comma"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt12.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
    def test_f2_NVt13(self):
        """del de comma"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt13.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt14(self):
        """dup de parte2"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt14.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
    def test_f2_NVt15(self):
        """del de parte2"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt15.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("There are too/few keys", cm.exception.message)

    def test_f2_NVt16(self):
        """mod de }"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt16.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt17(self):
        """dup etiqueta1"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt17.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt18(self):
        """del etiqueta1"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt18.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt19(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt19.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt20(self):
        """del separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt20.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt21(self):
        """dup dato1"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt21.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt22(self):
        """del dato1"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt22.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt23(self):
        """mod coma"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt23.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt24(self):
        """dup etiqueta2"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt24.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt25(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt25.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt26(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt26.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt27(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt27.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt28(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt28.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt29(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt29.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt30(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt30.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm.exception.message)

    def test_f2_NVt31(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt31.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm.exception.message)

    def test_f2_NVt32(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt32.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt33(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt33.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Hash", cm.exception.message)
    def test_f2_NVt34(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt34.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Hash", cm.exception.message)

    def test_f2_NVt35(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt35.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm.exception.message)

    def test_f2_NVt36(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt36.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm.exception.message)

    def test_f2_NVt37(self):
        """dup separador"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt37.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_Vt2(self):
        # elimniar el almacen
        input_file = store_path + "/f2_vt2.json"
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
        self.assertEqual("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0", value)

    def test_f2_NVt38(self):
        """del idmail"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt38.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_NVt39(self):
        """dup arroba"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt39.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)
    def test_f2_NVt40(self):
        """del @"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt40.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_Vt3(self):
        """dup dominio"""
        # elimniar el almacen
        input_file = store_path + "/f2_vt3.json"
        if os.path.isfile(store_path + "/Almancen.JSON"):
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
        self.assertEqual("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0", value)

    def test_f2_NVt41(self):
        """del dominio"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt41.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_NVt42(self):
        """dup ."""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt42.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_NVt43(self):
        """del ."""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt43.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_NVt44(self):
        """mod ."""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt44.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_Vt4(self):
        """dup extension"""
        ## elimniar el almacen
        input_file = store_path + "/f2_vt4.json"
        if os.path.isfile(store_path + "/Almancen.JSON"):
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
        self.assertEqual("5856fbd8f18ad8381d45e0efe946025037a3dfe689f285c1dab0b48ef91df0f0", value)

    def test_f2_NVt46(self):
        """mod \" """
        # elimniar el almacen
        input_file = store_path + "/f2_nvt46.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)

    def test_f2_NVt47(self):
        """mod OrderID """
        # elimniar el almacen
        input_file = store_path + "/f2_nvt47.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm.exception.message)

    def test_f2_NVt48(self):
        """mod id """
        # elimniar el almacen
        input_file = store_path + "/f2_nvt48.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Hash", cm.exception.message)

    def test_f2_NVt49(self):
        """mod ContactEmail"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt49.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Incorrect keys", cm.exception.message)

    def test_f2_NVt50(self):
        """mod email"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt50.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_NVt51(self):
        """mod @"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt51.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_NVt52(self):
        """mod dominio"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt52.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

    def test_f2_NVt53(self):
        """mod extension"""
        # elimniar el almacen
        input_file = store_path + "/f2_nvt53.json"
        if os.path.isfile(store_path + "/Almacen.JSON"):
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

        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(input_file)
        self.assertEqual("Wrong Contact Email", cm.exception.message)

if __name__ == '__main__':
    unittest.main()