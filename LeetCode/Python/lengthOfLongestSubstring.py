s = "dvdf"

def lengthOfLongestSubstring(s):
    charSet = set()
    maxLength = 0
    
    left = 0
    
    for right in range(len(s)):
        if s[right] not in charSet: 
            # add new char to set & update maxLength
            charSet.add(s[right])
            maxLength = max(maxLength, len(charSet))
        else: 
            # move left pointer and erase charSet up to duplicate
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            # add right pointer to end of charSet
            charSet.add(s[right])


    return maxLength

answer = lengthOfLongestSubstring(s)

print(answer)