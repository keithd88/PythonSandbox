s = "   fly me   to   the moon  "

def lengthOfLastWord(s):
    words = s.split()
    
    return len(words[-1])



answer = lengthOfLastWord(s)

print(answer)