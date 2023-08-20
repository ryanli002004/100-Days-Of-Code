bill = float(input("what was the bill: "))
num = int(input("how many people: "))
tip = int(input("what percent tip do you want to leave?"))
total = tip / 100 * bill + bill
billper = total / num
rounded = round(billper, 2)
print("each one owes:", rounded)