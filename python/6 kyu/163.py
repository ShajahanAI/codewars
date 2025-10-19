# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

# Passed

def stock_list(stocklist, categories):
    if not stocklist:
        return ""
    
    result_dict = dict()
    for stock_qty in stocklist:
        stock, qty = stock_qty.split(' ')
        if stock[0] in categories:
            if stock[0] not in result_dict:
                result_dict[stock[0]] = 0
                
            result_dict[stock[0]] += int(qty)
            
    formatted_result = " - ".join([f"({category} : {result_dict.get(category, 0)})" for category in categories])
    return formatted_result

output = stock_list(["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B", "C", "D"])
print(output)