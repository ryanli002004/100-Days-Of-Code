f = open('day48folder/day48.list','r')
contents = f.read().split("\n")
f.close()
contents.pop()
print(contents)
hs = 0
name = None
for loop in contents:
    loop1 = loop.split()
    if int(loop1[1]) > hs:
        hs = int(loop1[1])
        name = loop1[0]

print(f"current winner is {name} with a highscore of {hs}")