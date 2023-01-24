import csv
import pandas as pd

customers_csv_path = 'csv/customers.csv'
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
    result_path = 'results/order_prices.csv' 

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
                    total_price += float(dict_of_product['cost'])
                order_result['id'] = order['id']
                order_result['total'] = total_price
                #print(order_result)
                writer.writerow(order_result)


def generate_product_customers ():
    result_path = 'results/product_customers.csv'

    with open(customers_csv_path, newline='') as csvfile:
        list_of_customers = from_list_of_dict_to_dict(csv.DictReader(csvfile))
    
    with open(result_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'customer_id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader() 
        with open(orders_csv_path, newline='') as csvfile:
            list_of_orders = csv.DictReader(csvfile)
            customer_result = {}
            for order in list_of_orders:
                for customer in order['customer'].split(' '):
                    dict_of_customers = list_of_customers[customer]
                    print(dict_of_customers)
                    customer_result['id'] = order['id']
                    #customer_result['customer_id'] = 
                    print(dict_of_customers)
                    

                        
def generate_customer_ranking ():
    result_path = 'results/customer_ranking.csv'
                        
    with open(customers_csv_path, newline='') as csvfile:
        customers_by_id = from_list_of_dict_to_dict(csv.DictReader(csvfile))

    with open(products_csv_path, newline='') as csvfile:
        products_by_id = from_list_of_dict_to_dict(csv.DictReader(csvfile))

    with open(result_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'lastname', 'total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        with open(orders_csv_path, newline='') as csvfile:
            list_of_orders = csv.DictReader(csvfile)
            for order in list_of_orders:
                customer_ranking = {}
                total_price = 0
                for customer in order['customer']:
                    dict_of_customers = customers_by_id[customer]
                for product_id in order['products'].split(' '):
                    dict_of_product = products_by_id[product_id]
                    total_price += float(dict_of_product['cost'])

                customer_ranking['id'] = order['customer']
                customer_ranking['name'] = dict_of_customers['firstname']
                customer_ranking['lastname'] = dict_of_customers['lastname']
                customer_ranking['total'] = total_price
                print(customer_ranking)

                writer.writerow(customer_ranking)
    
    df = pd.read_csv(result_path)
    
    customer_ranking_sorted = df.sort_values(by=['total'], ascending=False)
    customer_ranking_sorted.to_csv('results/customer_ranking.csv', index=False)



generate_product_customers()                    