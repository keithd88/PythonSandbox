"""
search through rows for * (gear symbol)
if * has exactly two numbers adjacent, 
multiply the two numbers to get the gear ratio
"""

import pandas as pd


input = pd.read_csv('Day3\\test_input.txt', header = None)
input = input[0].apply(lambda x: pd.Series(list(x)))

max_row, max_col = input.shape

print(input)

part_number_sum = 0 # final output


def get_value(value, row, col):
    print(f'value: {value}, row: {row}, col: {col}')
    value_info = {'value': value, 'rows': [row-1, row, row+1], 'cols': [col-1, col, col+1]}
    for i in range(1,max_col-col):
        # check if next value in row is also a digit
        next_value = input.iloc[cur_row, cur_col+i]
        # print(f'next value: {next_value}')
        
        if next_value.isdigit():
            value_info['value'] = ''.join([value_info['value'], next_value])
            value_info['cols'].append(col+1+i)
        
        else:
            return value_info

    return value_info
        
def add_value(value_info):
    # print(f'current value: {value_info['value']}')
    
    # search for symbols around number
    cur_rows = value_info['rows']
    cur_cols = value_info['cols']
    
    for row in cur_rows:
        if max_row > row >= 0:
            for col in cur_cols:
                if max_col > col >= 0:
                    # print(row,col)
                    check_value = input.iloc[row, col]
                    if check_value.isdigit():
                        continue
                    elif check_value == '.':
                        continue
                    else:
                        print(f'adding value {value_info['value']}')
                        return int(value_info['value']) # only return value if there is a symbol
    return 0


cur_row = 0

while cur_row < max_row:
    print(input.iloc[[cur_row]])
    cur_col = 0

    while cur_col < max_col:
        value = input.iloc[cur_row, cur_col]
        # print(value)
    
        if value.isdigit(): # if value is a digit, get entire number
            value_info = get_value(value, cur_row, cur_col)
            part_number_sum += add_value(value_info)
            # print(value_info['rows'][-1] + 1)
            cur_col = value_info['cols'][-1]
            if cur_col >= max_col:
                break
        cur_col += 1
    cur_row += 1
                    
print(f'Final part number sum: {part_number_sum}')