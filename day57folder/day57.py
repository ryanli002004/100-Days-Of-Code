def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

print(factorial(5))