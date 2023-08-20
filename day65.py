class character:

    name = str
    hp = int 
    mp = int

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def print1(self):
        print(f'{self.name} has {self.hp} and {self.mp}')


class player(character):

    nickname = str
    lives = int

    def __init__(self, name, hp, mp, nickname, lives):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.nickname = nickname
        self.lives = lives

    def print1(self):
        print(f'{self.name}:{self.nickname} has {self.hp} hp, {self.mp} mp, and {self.lives} lives')

    def isalive(self):
        if self.lives > 0:
            print(f'{self.name} the {self.nickname} is alive!')
        else:
            print(f'{self.name} the {self.nickname} has died!')


class enemy(character):

    type = str
    strength = int

    def __init__(self, name, hp, mp, type, strength):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.type = type
        self.strength = strength

    def print1(self):
        print(f"{self.name} type: {self.type} has {self.hp} hp, {self.mp} mp, and {self.strength} strength")


class orc(enemy):

    speed = int

    def __init__(self, name, hp, mp, strength, speed):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.type = "orc"
        self.strength = strength
        self.speed = speed

    def print1(self):
        print(f"{self.name} type: {self.type} has {self.hp} hp, {self.mp} mp, and {self.strength} strength and has {self.speed} speed")

class vampire(enemy):

    day = bool

    def __init__(self, name, hp, mp, strength, day):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.type = "vampire"
        self.strength = strength
        self.day = day

    def print1(self):
        if self.day == True:
            print(f"{self.name} type: {self.type} has {self.hp} hp, {self.mp} mp, and {self.strength} strength but it is daytime")
        if self.day == False:
            print(f"{self.name} type: {self.type} has {self.hp} hp, {self.mp} mp, and {self.strength} strength and it is nighttime!")

player("ryan", 100, 100, "the mighty", 10).print1()
orc("geroge", 70, 70, 7, 5).print1()
orc("roger", 80, 50, 3, 5).print1()
orc("nick", 40, 50, 9, 5).print1()
vampire("vinny", 60, 90, 7, True).print1()
vampire("luke", 80, 90, 8, False).print1()
player("ryan", 100, 100, "the weak", 10).isalive()