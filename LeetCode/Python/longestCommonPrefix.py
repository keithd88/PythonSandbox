strs = ["dog","racecar","car"]

def longestCommonPrefix(strs):
    shortest = min(strs, key = len)
    # print(shortest)
    
    prefix = ''

    # iterate over each char in shortest word
    for index in range(len(shortest)):
        # print(shortest[index])
        curr_letter = shortest[index]

        # check if all strings share current letter
        for string in strs:
            if curr_letter != string[index]:
                return prefix

        prefix += curr_letter

    return prefix

pre = longestCommonPrefix(strs)

print(f'Prefix is "{pre}"')