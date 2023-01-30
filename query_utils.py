def from_list_of_dict_to_dict (list_of_dict, primary_key='id'):
    result = {}
    for row in list_of_dict:
        no_key_row = row.copy()
        del no_key_row[primary_key]    
        result[row[primary_key]] = no_key_row
    return result
        
def total_price_orders(order_string, products_by_id):
    total_price = 0
    for product_id in order_string.split(' '):
        dict_of_product = products_by_id[product_id]
        total_price += float(dict_of_product['cost'])
    return total_price
