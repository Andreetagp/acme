import csv

customers_csv_path = 'csv/curstomers.csv'
orders_csv_path = 'csv/orders.csv'
products_csv_path = 'csv/products.csv'


def from_list_of_dict_to_dict (list_of_dict, primary_key='id'):
    result = {}
    for row in list_of_dict:
        no_key_row = row.copy()
        del no_key_row[primary_key]     #del palabra reservada per a borrar key
        result[row[primary_key]] = no_key_row
    return result
        
def generate_order_prices ():
    result_path = 'order_prices.csv' 

    with open(products_csv_path, newline='') as csvfile:
        products_by_id = from_list_of_dict_to_dict(csv.DictReader(csvfile))

    with open(result_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        with open(orders_csv_path, newline='') as csvfile:
            list_of_orders = csv.DictReader(csvfile)
            for order in list_of_orders:
                order_result = {}
                total_price = 0
                for product_id in order['products'].split(' '):
                    dict_of_product = products_by_id[product_id]
                    total_price += float(dict_of_product['cost'])             #se fica el 0 perque es dic i es el primer elem
                order_result['id'] = order['id']
                order_result['total'] = total_price
                print(order_result)
                writer.writerow(order_result)


generate_order_prices()