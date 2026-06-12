# https://www.codewars.com/kata/585d7b4685151614190001fd/train/python

# Passed

def get_total(costs, items, tax):
    total_cost_pretax = sum(costs.get(item, 0) for item in items)
    final_cost = round(total_cost_pretax * (1 + tax), 2)
    return final_cost

output = get_total({'socks':5, 'shoes':60, 'sweater':30}, ['socks', 'shoes'], 0.09)
print(output)