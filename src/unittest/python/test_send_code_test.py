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
        file_store = str(Path.home()) + "store_patient.json"
        if os.path.isfile(file_store):
            os.remove(file_store)
    def test_something( self ):
        """dummy test"""
        self.assertEqual(True, False)

    @freeze_time("01-01-1900 00:00:00")
    def test_f1_Vt1(self):
        # caso válido all corect
        #### Falta borrar y crear el almacen
        my_order = order_manager.OrderManager()
        ########## Falta dar la dirección del json
        value = my_order.send_code(json)
        self.assertEqual("",value)

        """with(open(file_store,"r",encoding="UTF-8", newline=""))as file:
            data_list = json.load(file)
        found = False
        for item in data_list:
            if item["_OrderRequest__order_id"] == "45a77da7acc49cc551fab69cb6e2ce4b":
                found = True
        self.assertTrue(found)"""

    def test_f1_NVt1(self):
        ##### Falta borrar y crear el almacen
        my_order = order_manager.OrderManager()

        with self.assertRaises(order_management_exception.OrderManagementException) as cm:
            my_order.send_code(json)
        self.assertEqual("", cm.exception.message)



if __name__ == '__main__':
    unittest.main()