list = []
while True:
    fir = input("first name? ").strip().capitalize()
    las = input("last name? ").strip().capitalize()
    nam = f"{fir} {las}"
    if nam not in list:
        list.append(nam)
        for loop in list:
            print(loop)
    else:
        print(f"sorry {nam} already in list")  