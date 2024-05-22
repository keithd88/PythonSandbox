digits = [9]

def plusOne(digits):
    # convert to list of strings
    s=[str(digit) for digit in digits]
    
    # join strings, convert to int, and increment 1
    num = int("".join(s)) + 1

    # return list of digits for new num
    return [int(digit) for digit in str(num)]
    

answer = plusOne(digits)

print(answer)