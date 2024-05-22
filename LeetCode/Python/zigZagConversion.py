s = "PAYPALISHIRING"
numRows = 3

"""
P   A   H   N
A P L S I I G
Y   I   R 

0   4   8     12
1 3 5 7 9  11 13
2   6   10



Need to iterate over the length of the string
Create an empty array of the correct size (numRows * )
start going down the column until we reach the desired number of rows
then go across one column and up one row until we reach the top
then repeat
then read across the rows


OR

Create a dictionary w/ numRows
As you traverse the string, add each character to the corresponding dict row
Start going down the rows, then turn around when at bottom, repeat
then return all the rows in order
"""

def convert(s, numRows):
    result = ''
    result_dict = {}

    # initialize dict to hold chars
    for row in range(numRows):
        result_dict[row] = ''
        down_rows = list(range(numRows))
        up_rows = 

    # iterate over string
    down = True
    for index, char in enumerate(s):
        # result_dict[0] += char
        if down:
            for index in range(numRows):
                result_dict[index] = char
            down = False

        # elif not down:
        #     for index in range(numRows:0):
        #         print(index)


        # if index/iteration < numRows:
        #     result_dict[index] = char
        # else:

    # combine each row in order
    for row in result_dict:
        result += result_dict[row]
    
    return result

answer = convert(s, numRows)

print(answer)