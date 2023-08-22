name = input("what is your name? ")
dob = input("when were you born? ")
num = input("what is your number? ")
email = input("what is your email? ")
addr = input("what is your address? ")
dic = {}
dic["name"] = name
dic["dob"] = dob
dic["num"] = num
dic["email"] = email
dic["addr"] = addr

print(f"hi, {dic['name']} you were born {dic['dob']} and your number is {dic['num']} your email is {dic['email']} and you live at {dic['addr']}")