s = " "


def stringToInt(s):
    sign = 1
    value = ''
    
    s = s.strip(' ')

    if len(s) == 0:
            return 0

    # read in sign of int and update string
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # add all sequential digits to value
    for char in s:
        if not char.isdigit():
            break
        value += char

    if len(value) == 0:
         return 0

    value = int(value)
    
    value = sign * value
    value = max(value, -2**31)
    value = min(value, 2**31 - 1)

    return value



answer = stringToInt(s)

print(answer)