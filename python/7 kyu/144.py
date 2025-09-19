# https://www.codewars.com/kata/56069d0c4af7f633910000d3/train/python

# Passed

def search(budget, prices):
    affordable_prices = [price for price in prices if price <= budget]
    affordable_prices.sort()
    affordable_prices_as_string = ",".join([str(price) for price in affordable_prices])
    return affordable_prices_as_string

output = search(14, [13, 15, 14, 14, 15, 13])
print(output)