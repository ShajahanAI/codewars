# https://www.codewars.com/kata/5e16ffb7297fe00001114824/train/python

# Passed

def top3(products, amounts, prices):
    get_indexes = lambda list_to_check, value_to_check: [idx for idx in range(len(list_to_check)) if list_to_check[idx] == value_to_check]
    revenues = [amount_price[0] * amount_price[1] for amount_price in zip(amounts, prices)]
    sorted_revenues = sorted(revenues, reverse=True)
    products_ordered_by_sales = []
    for revenue in sorted_revenues:
        indexes = get_indexes(revenues, revenue)
        products_ordered_by_sales.extend(products[idx] for idx in indexes)
    
    top_three_products = products_ordered_by_sales[:3]
    return top_three_products

output = top3(['Cell Phones', 'Vacuum Cleaner', 'Computer', 'Autos', 'Gold', 'Fishing Rods', 'Lego', 'Speakers'], 
              [5,             25,               2,          7,       10,     3,              2,      24], 
              [51,            225,              22,         47,      510,    83,             82,     124])
print(output)