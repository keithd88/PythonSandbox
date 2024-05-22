a = "11"
b = "1"

def addBinary(a, b):
    new_int = int(a, 2) + int(b, 2)

    new_bin = bin(new_int)[2:]

    return new_bin



answer = addBinary(a, b)

print(answer)