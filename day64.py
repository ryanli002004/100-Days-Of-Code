class job:

    name = None
    salary = None
    hoursworked = None

    def __init__(self, name, salary, hoursworked):
        self.name = name
        self.salary = salary
        self.hoursworked = hoursworked
    
    def print1(self):
        print(f"{self.name} makes {self.salary} with {self.hoursworked} hours worked")


class doctor(job):

    expierence = None
    speciality = None

    def __init__(self, salary, hoursworked, expierence, speciality ):
        self.name = "doctor"
        self.salary = salary
        self.hoursworked = hoursworked
        self.expierence = expierence
        self.speciality = speciality
    
    def print1(self):
        print(f"{self.name} {self.salary} with {self.hoursworked} hours worked, specalized in {self.speciality} with {self.expierence} expierence")


class teacher(job):

    position = None
    subject = None

    def __init__(self, salary, hoursworked, posiiton, subject):
        self.name = "teacher"
        self.salary = salary
        self.hoursworked = hoursworked
        self.position = posiiton
        self.subject = subject

    def print1(self):
        print(f"{self.name} {self.salary} with {self.hoursworked} hours worked, teaching {self.subject} as a {self.position}")

job("lawyer","100k","100").print1()
doctor("150k","150","7yr","pediatric consultant").print1()
teacher("50k","50","subsitute teacher","math").print1()