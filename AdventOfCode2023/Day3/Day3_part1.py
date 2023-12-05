import pandas as pd

file = open('Day3\\test_input.txt', 'r')
input = file.read()
file.close()

input = input.split('\n')

# input = pd.read_csv('Day3\\test_input.txt', header = None)
# input = input[0].apply(lambda x: pd.Series(list(x)))

print(input)

for row, values in enumerate(input):
    print(row, values)
    for column, value in enumerate(values):
        # print(row, column, value)
        if value == '.':
            continue
        elif value.isdigit():
            print(value)
        else:
            print(value)




# for index, row in input.iterrows():
#     print(index, row)
#     # print(is_num.iloc[[0]])
#     row = row.str.isnumeric()
#     print(row)

    # is_num.iloc[[0]] = row.str.isnumeric()

    # print(is_num)


    # for char in enumerate(line):
    #     print(char)
    #     is_char_num = char[1].isdigit()
    #     new_line[char[0]] = {char[1], is_char_num}

    # is_num.append(new_line)
    # print(is_num)
    # line = line.replace('.', ' ') # replace periods to split properly
    # nums = line.split() # get numbers in a list
    # print(nums)



