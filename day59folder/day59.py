word1 = "racecar"
word2 = "ryan"
word3 = "a"
word4 = "is"
word5 = "kjoojk"



def palindrome(x):
    if len(x) == 1:
        return "palindrome!"
    elif x[0] == x[-1] and len(x) == 2:
        return "palindrome!"
    elif x[0] == x[-1] and len(x) >2:
        return palindrome(x[1:-1])
    else:
        return "not a palindrome"
    
print(palindrome(word5))