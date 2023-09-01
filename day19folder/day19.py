print("loan calculator")
total = 1000
for i in range(10):
    total += total * 0.05
    rounded1 = round(total,2)
    print("year", i +1, "is", rounded1)
interest = total - 1000
rounded = round(interest, 2)
print("you paid", rounded, "in interest")