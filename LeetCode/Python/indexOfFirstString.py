haystack = "sadbutsad"
needle = "sad"

def findString(haystack, needle):
    # iterate over each letter in the haystack
    # once it matches the first letter of the needle, check if following letters match
    for index, char in enumerate(haystack):
        first_letter = needle[0]
        
        # if letter is found, check if entire needle is there
        if first_letter == char:
            if needle == haystack[index:index+len(needle)]:
                return index
            
    return -1
    


out = findString(haystack, needle)

print(out)