year = int(input("What year were you born?"))
if year <= 1946:
    print("you are a tradionalist")
elif year >= 1947 and year <= 1964:
    print("you are a baby boomer")
elif year >= 1965 and year <= 1981:
    print("you are gen x")
elif year >= 1982 and year <= 1995:
    print("you are a millenial")
elif year >= 1996:
    print("you are gen z")
else: 
    print("numbers only!")