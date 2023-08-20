first = input("what is your first name? ").strip().capitalize()
last = input("what is your last name? ").strip()
mom = input("what is your mom's first name? ").strip().capitalize()
born = input("where was your mom born? ").strip()
fir = first[0:3]
las = last[0:3]
mo = mom[0:3]
bor = born[0:2]
print(f"your starwars name will be: {fir}{las} {mo}{bor}")