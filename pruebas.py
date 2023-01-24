import csv

def from_list_of_dict_to_dict (list_of_dict, primary_key='id'):
    result = {}
    for row in list_of_dict:
        no_key_row = row.copy()
        del no_key_row[primary_key]     #del palabra reservada per a borrar key
        result[row[primary_key]] = no_key_row
    print(result)

from_list_of_dict_to_dict(csv.DictReader('csv/customers.csv'))
    