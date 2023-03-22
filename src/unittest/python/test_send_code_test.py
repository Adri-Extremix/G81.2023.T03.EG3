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
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, False)

    @freeze_time("01-01-1900 00:00:00")
    def test_f1_Vt1(self):
        # caso válido all corect
        file_store = str(Path.home()) + "/home/adrian/PycharmProjects/G81.2023.T03.EG3/src/Json/Store/store.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        ### Rellenar el json con datos para que el envio se encuentre en el almacén
        dicc_json = []
        try:
            with open(file_store,"w",encoding="utf-8",newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex


        #### Falta borrar y crear el almacen
        my_order = order_manager.OrderManager()
        ########## Falta dar la dirección del json
        value = my_order.send_code(json)
        self.assertEqual("",value)

    def test_f1_NVt1(self):
        file_store = str(Path.home()) + "/home/adrian/PycharmProjects/G81.2023.T03.EG3/src/Json/Store/store.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
        ### Rellenar el json con datos para que el envio se encuentre en el almacén
        dicc_json = []
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(dicc_json, file, indent=2)
        except FileNotFoundError as ex:
            raise order_management_exception.OrderManagementException("Wrong file or file path") from ex


        my_order = order_manager.OrderManager()
        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(json)
        self.assertEqual("", cm.exception.message)



if __name__ == '__main__':
    unittest.main()