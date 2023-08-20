num = int(input("select a number "))
counter = 0
for i in range(1, 11):
    correct = i*num
    print(i, "x", num)
    answer = int(input("> "))
    if answer == correct:
        print("correct!")
        counter += 1
    else:
        print("wrong it should have been ", correct)
else:
    print("you got", counter, "out of 10 correct.")