import random
import re


def pani(x):
    if x[0] != x[-1] and len(x) > 1:
        return "not a pani!"
    elif x[0] == x[-1] and len(x) > 1:
        return pani(x[1:-1])
    else:
        return "pani!"
    

def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)
    

def randomgen():
    num = random.randint(1, 99)
    return num


def sanitize_name(name):
    sanitized = re.sub(r'[\\/:*?"<>|]', '_', name)
    return sanitized


