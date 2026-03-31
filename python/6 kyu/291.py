# https://www.codewars.com/kata/59d727d40e8c9dd2dd00009f/train/python

# Passed

def balance(book):
    book_rows = [book_row for book_row in book.splitlines() if book_row.strip()]
    clean_book_row = lambda book_row: "".join([char for char in book_row if char.isalnum() or char == " " or char == "."])
    float_as_str = lambda float_num: str(float_num) + "0" if len(str(float_num).split(".")[-1]) == 1 else str(float_num)    
    expenses = []
    result_rows = []
    for idx, book_row in enumerate(book_rows):
        cleaned_book_row = clean_book_row(book_row)
        if idx == 0:
            balance = float(cleaned_book_row)
            result_row = f"Original Balance: {float_as_str(balance)}"
        else:
            si, item, expense = cleaned_book_row.split(' ')
            expense = float(expense)
            expenses.append(expense)
            balance -= expense
            balance = round(balance, 2)
            result_row = f"{si} {item} {float_as_str(expense)} Balance {float_as_str(balance)}"
            
        result_rows.append(result_row)
    
    total_expense = round(sum(expenses), 2)
    average_expense = round(total_expense / len(expenses), 2)
    result_rows.append(f"Total expense  {float_as_str(total_expense)}")
    result_rows.append(f"Average expense  {float_as_str(average_expense)}")
    
    result = "\r\n".join(result_rows)
    return result

output = balance("""1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
""")
print(output)