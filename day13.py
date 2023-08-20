print("grader")
print()
maxscore = int(input("Max. Possible Score:"))
urscore = int(input("Your score: "))
print()
score = float(urscore / maxscore)
finalscore = round(score, 2)
percentage = round(float(urscore / maxscore)*100, 2)
print("You got",percentage,"%")
if finalscore >= .90:
    print("Your letter score is an A+")
elif finalscore >= .80 and finalscore <= .89:
    print("Your letter grade is an A-.")
elif finalscore >= .70 and finalscore <= .79:
    print("Your letter score is a B.")
elif finalscore >= .60 and finalscore <= .69:
    print("Your letter grade is a C.")
elif finalscore >= .50 and finalscore <= .59:
    print("Your letter grade is a D.")
elif finalscore <= .49:
    print("Your letter grade is a F.")
else: 
    print("Try again!")