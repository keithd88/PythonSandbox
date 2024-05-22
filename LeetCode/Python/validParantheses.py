s = "([)]"

def isValid(s):
    stack = []

    paran_map = {")": "(", "}": "{", "]": "["}
    
    # iterate through each char
    for char in s:
        # if char is a closing paran
        if char in paran_map:
            # pop the corresponding opening parenthesis from the stack
            if stack and stack[-1] == paran_map[char]:
                stack.pop()
            else:
                return False # mismatched paran
            
        else:
            stack.append(char) # append if char is opening
    
    # if stack is empty, all parantheses are matched
    return not stack
    
    # validity = True
    # open_paran = 0
    # open_brack = 0
    # open_square = 0

    # for index, char in enumerate(s):
    #     print(index, char)
        
    #     if char == '(':
    #         open_paran += 1
    #     elif char == ')':
    #         open_paran -= 1
    #     elif char == '{':
    #         open_brack += 2
    #     elif char == '}':
    #         open_brack -= 2
    #     elif char == '[':
    #         open_square += 3
    #     elif char == ']':
    #         open_square -= 3

    # if (open_paran + open_brack + open_square) != 0:
    #     validity = False

    # return validity

validity = isValid(s)

print(validity)