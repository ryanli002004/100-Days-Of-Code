dic = {"webname":None,"url":None, "description":None, "rating":None}
for keys in dic.keys():
    update = input(f"please enter the {keys}: ")
    dic[keys] = update

for i, j in dic.items():
    print(f"{i}:{j}")
