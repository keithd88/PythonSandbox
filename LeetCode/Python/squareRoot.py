x = 81

def squareRoot(x):
    # if x == 0 or 1, return x
    if (x == 0 or x == 1):
        return x

    # initialize search range for sqrt
    start = 1
    end = x

    # perform binary search to find sqrt(x)
    while (start <= end):
        # calc middle point 
        mid = start + (end - start) / 2
        
        # if mid^2 == x, return mid
        if mid * mid == x:
            return mid
        
        # if the mid^2 > x, move end to the left (mid - 1)
        elif mid * mid > x:
            end = mid - 1

        # if mid^2 < x, move start to the right (mid + 1)
        else:
            start = mid + 1

    return int(end)

answer = squareRoot(x)

print(answer)