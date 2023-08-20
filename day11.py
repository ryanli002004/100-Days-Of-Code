ask = input("is it leap year? ")
if ask == "no":
    seconds = 365*24*60*60
    print("there are",seconds,"seconds in this year")
elif ask =="yes":
    seconds = 366*24*60*60
    print("there are",seconds,"seconds in this year")