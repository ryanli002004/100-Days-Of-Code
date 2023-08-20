import time
import os
import pygame #has to be installed through terminal

def play():
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join("day26folder","day26.wav"))
    pygame.mixer.music.play()
    while True:
        choic = input("press 2 to pause: ")
        if choic == "2":
            pygame.mixer.music.pause()
            return
        else:
            continue

while True:
    os.system("clear")
    print("music player")
    time.sleep(1)
    print("press 1 to play")
    time.sleep(1)
    print("press 2 to exit")
    time.sleep(1)
    print("press anything else to reload menu")
    choice = input("")
    if choice == "1":
        play()
        continue
    elif choice == "2":
        exit()
    else:
        continue
  
