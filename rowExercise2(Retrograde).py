import sys
import math
import random

print("Twelve Tone Row Generator!!")
print()
tones = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

print(f"Default Row is {tones}")
print()


def getrando():

    while True:
        print("Want a random 12 tone row? Please enter 'yes' or 'no'.")
        print()
        cmd = input().lower()
        if cmd == "yes":
            randtoneshuff = list(enumerate(tones))
            x = random.shuffle(randtoneshuff)
            shufftones, shuffnums = zip(*randtoneshuff)
            shufftones = list(shufftones)
            shuffnums = list(shuffnums)
            print(shufftones)
            print(shuffnums)      
            break
        if cmd == "no":
            print("Okay, come back soon!")
            sys.exit()
        if cmd != "yes" and cmd != "no":
            print("Input not accepted. Please enter 'yes' or 'no'.\n")

    while True:
        print("Would you like to display this row in retrograde?")
        cmdret = input().lower()
        if cmdret == "yes":
            print("In Retrograde: ")
            print()
            print(shufftones[::-1])
            print(shuffnums[::-1])
            print()
            break
        if cmdret == "no":
            break
        if cmdret != "yes" and cmdret != "no":
            print("Input not accepted. Please enter 'yes' or 'no'.")
            continue


    while True:
        print("Begin again?")
        cmdrpt = input().lower()
        if cmdrpt == "yes":
            getrando()
            print()
        if cmdrpt == "no":
            print("Exiting! Bye!")
            sys.exit()
        if cmdrpt != "yes" and cmdrpt != "no":
            print("Input not accepted. Please enter 'yes' or 'no'.\n") 
            continue
try:

    getrando()

except:
    KeyboardInterrupt
   




