import datetime

print("event countdown")

today = datetime.date.today()
event = input("what is the event? ")
year1 = int(input("what year is your event? "))
month1 = int(input("what month is it in? "))
day1 = int(input("what day is it on? "))
eventdate = datetime.date(year=year1, month=month1, day=day1)

if today == eventdate:
    print('yay the event is today!!!')
elif eventdate < today:
    print('sorry the event has passed')
else:
    daysuntil = (eventdate - today).days
    print(f'you have {daysuntil} until {event}!')