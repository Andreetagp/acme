import csv
import query_utils as qu

customers_csv_path = 'csv/customers.csv'
orders_csv_path = 'csv/orders.csv'
products_csv_path = 'csv/products.csv'

def generate_order_prices ():
    result_path = 'results/order_prices.csv' 

    with open(products_csv_path, newline='') as csvfile:
        products_by_id = qu.from_list_of_dict_to_dict(csv.DictReader(csvfile))
        
    with open(result_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        with open(orders_csv_path, newline='') as csvfile:
            list_of_orders = csv.DictReader(csvfile)
            for order in list_of_orders:
                order_result = {}
                order_result['id'] = order['id']
                order_result['total'] = qu.total_price_orders(order['products'], products_by_id)
                #print(order_result)
                writer.writerow(order_result)


def generate_product_customers ():
    result_path = 'results/product_customers.csv'

    with open(result_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'customer_ids']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() 

        with open(orders_csv_path, newline='') as csvfile:
            list_of_orders = csv.DictReader(csvfile)
            customers_by_product = {}
            for order in list_of_orders:
                for product_id in order['products'].split(' '):
                    customers_list = customers_by_product.get(product_id, [])
                    if len(customers_list) == 0:
                        customers_by_product[product_id] = customers_list
                    if order['customer'] not in customers_list:
                        customers_list.append(order['customer'])

            for product_id in customers_by_product:
                writer.writerow({'id': product_id, 'customer_ids': ' '.join(customers_by_product[product_id])})

                        
def generate_customer_ranking ():
    result_path = 'results/customer_ranking.csv'
                        
    with open(customers_csv_path, newline='') as csvfile:
        customers_by_id = qu.from_list_of_dict_to_dict(csv.DictReader(csvfile))

    with open(products_csv_path, newline='') as csvfile:
        products_by_id = qu.from_list_of_dict_to_dict(csv.DictReader(csvfile))

    with open(result_path, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'lastname', 'total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        with open(orders_csv_path, newline='') as csvfile:
            list_of_orders = csv.DictReader(csvfile)
            customer_ranking = {}
            
            for order in list_of_orders:
                customer_dict = customer_ranking.get(order['customer'],{})
                if len(customer_dict.keys()) == 0: 
                    customer_dict['id'] = order['customer']
                    customer_dict['name'] = customers_by_id[order['customer']]['firstname']
                    customer_dict['lastname'] = customers_by_id[order['customer']]['lastname']
                    customer_dict['total'] = qu.total_price_orders(order['products'], products_by_id)
                    customer_ranking[order['customer']] = customer_dict
                else:
                    customer_dict['total'] += qu.total_price_orders(order['products'], products_by_id) 
            sorted_customer_ranking = sorted(customer_ranking.values(), key=lambda c: c['total'], reverse=True)
            for customer in sorted_customer_ranking:
                writer.writerow(customer)
    


generate_product_customers()                    