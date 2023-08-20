print("done with 30 days what do you think so far?")
for days in range(1,31):
    print("day",days)
    answer = input("")
    text = f"you thought day {days} was"
    print(f"{text:^50}")
    print(f"{answer:^50}")