s = 'MCMXCIV'

def romanToInteger(s):

    roman_table = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    int_conv = 0

    for index, char in enumerate(s):
        value_to_add = roman_table[char]
        
        # check for combined cases
        if char == 'I' and len(s) > index+1:
            if s[index+1] == 'V' or s[index+1] == 'X':
                value_to_add = -value_to_add
                # print(value_to_add)
                
        elif char == 'X' and len(s) > index+1:
            if s[index+1] == 'L' or s[index+1] == 'C':
                value_to_add = -value_to_add
                # print(value_to_add)
                
        elif char == 'C' and len(s) > index+1:
            if s[index+1] == 'D' or s[index+1] == 'M':
                value_to_add = -value_to_add
                print(value_to_add)
                

        
        int_conv += value_to_add
        print(int_conv)


    return int_conv