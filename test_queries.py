import query_utils as qu
import queries as q
import unittest
import csv

with open(q.products_csv_path, newline='') as csvfile:
        products_by_id = qu.from_list_of_dict_to_dict(csv.DictReader(csvfile))

from_list_of_dict_to_dict_case_1_in = [{'id': '1', 'customer': '10', 'products': '1 3 20'},
                                        {'id': '2', 'customer': '14', 'products': '4 5 12'},
                                        {'id': '3', 'customer': '3', 'products': '4 5 8'}]

from_list_of_dict_to_dict_case_1_default_out = {'1': {'customer': '10', 'products': '1 3 20'}, 
                                        '2': {'customer': '14', 'products': '4 5 12'}, 
                                        '3': {'customer': '3', 'products': '4 5 8'}}

from_list_of_dict_to_dict_case_1_key_customer_out = {'10': {'id': '1', 'products': '1 3 20'},
                                                    '14': {'id': '2', 'products': '4 5 12'},
                                                    '3': {'id': '3', 'products': '4 5 8'}}

from_list_of_dict_to_dict_case_1_key_product_out = {'1 3 20': {'id': '1', 'customer': '10'},
                                                    '4 5 12': {'id': '2', 'customer': '14'},
                                                    '4 5 8': {'id': '3', 'customer': '3'}}    

from_list_of_dict_to_dict_case_2_in = [{'id': '0', 'name': 'screwdriver', 'cost': '2.981163654411736'},
                                        {'id': '2', 'name': 'hammer', 'cost': '2.9037321212561906'},
                                        {'id': '3', 'name': 'sickle', 'cost': '8.90156976370351'}]

from_list_of_dict_to_dict_case_2_default_out = {'0': {'name': 'screwdriver', 'cost': '2.981163654411736'},
                                                '2': {'name': 'hammer', 'cost': '2.9037321212561906'},
                                                '3': {'name': 'sickle', 'cost': '8.90156976370351'}}         

from_list_of_dict_to_dict_case_2_key_name_out = {'screwdriver': {'id': '0', 'cost': '2.981163654411736'},
                                                'hammer': {'id': '2', 'cost': '2.9037321212561906'},
                                                'sickle': {'id': '3', 'cost': '8.90156976370351'}}  

from_list_of_dict_to_dict_case_3_in = []

from_list_of_dict_to_dict_case_3_out = {}
                                    
total_price_case_1_in = '1 0 1 0'

total_price_case_1_out = 18.943120182823662

total_price_case_1_incorrect_out = 2.5353645734532

class TestQueryUtils(unittest.TestCase):

    def test_from_list_of_dict_to_dict_1(self):
        expected = from_list_of_dict_to_dict_case_1_default_out
        actual = qu.from_list_of_dict_to_dict(from_list_of_dict_to_dict_case_1_in)
        self.assertEqual(actual,expected)

    def test_from_list_of_dict_to_dict_1_key_customer(self):
        expected = from_list_of_dict_to_dict_case_1_key_customer_out
        actual = qu.from_list_of_dict_to_dict(from_list_of_dict_to_dict_case_1_in, primary_key='customer')
        self.assertEqual(actual,expected)

    def test_from_list_of_dict_to_dict_1_key_product(self):
        expected = from_list_of_dict_to_dict_case_1_key_product_out
        actual = qu.from_list_of_dict_to_dict(from_list_of_dict_to_dict_case_1_in, primary_key='products')
        self.assertEqual(actual,expected)

    def test_from_list_of_dict_to_dict_2(self):
        expected = from_list_of_dict_to_dict_case_2_default_out
        actual = qu.from_list_of_dict_to_dict(from_list_of_dict_to_dict_case_2_in)
        self.assertEqual(actual,expected)
    
    def test_from_list_of_dict_to_dict_2_key_name(self):
        expected = from_list_of_dict_to_dict_case_2_key_name_out
        actual = qu.from_list_of_dict_to_dict(from_list_of_dict_to_dict_case_2_in, primary_key='name')
        self.assertEqual(actual,expected)

    def test_from_list_of_dict_to_dict_3(self):
        expected = from_list_of_dict_to_dict_case_3_out
        actual = qu.from_list_of_dict_to_dict(from_list_of_dict_to_dict_case_3_in)
        self.assertEquals(actual, expected)

    def test_total_price_1(self):
        expected = total_price_case_1_out
        actual = qu.total_price_orders(total_price_case_1_in, products_by_id)
        self.assertEqual(actual,expected)

    def test_total_price_1_incorrect(self):
        expected = total_price_case_1_incorrect_out
        actual = qu.total_price_orders(total_price_case_1_in, products_by_id)
        self.assertNotEqual(actual,expected)

    
if __name__ == '__main__':
    unittest.main()