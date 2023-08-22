word1 = "racecar"
word2 = "ryan"
word3 = "a"
word4 = "is"


def pani(x):
    if x[0] != x[-1] and len(x) > 1:
        return "not a pani!"
    elif x[0] == x[-1] and len(x) > 1:
        return pani(x[1:-1])
    else:
        return "pani!"

print(pani(word1))