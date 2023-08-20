def login():
    while True:
        username1 = "ryan"
        password1 = "password"
        username = input("what is your username? ")
        password = input("what is your password? ")
        if username1 == username and password1 == password:
            print("welcome")
            break
        else:
            print("your username or password is not recognized please try again.")
            continue

login()