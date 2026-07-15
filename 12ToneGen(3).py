# 12 Tone Row Maker (List Comprehension Exercise) 7.15.2026
import math
import sys
import random

print("12 Tone Generator and Manipulator 1.3")
tones = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(tones)

try:
    while True:
        print("Randomize Tone Row?")
        ans = input()
        if ans == 'yes':
            tones = random.sample(list(tones), len(tones))
            print(tones)
            break
        if ans == 'no':
            print("Okay!")
            print(tones)
            break
        else:
            print("Input not accepted. Enter yes or no.")
            continue        

    while True: 
        print("Retrograde?")
        ans1 = input()
        if ans1 == 'yes':
            print("Retrograde: ")
            tones[::-1] = tones
            print(tones)
            break
        if ans1 == 'no':
            print("Okay!")
            print(tones)
            break
        else:
            print("Input not accepted. Enter yes or no.")
            continue


    while True: 
        print("Invert?")
        ans2 = input()
        if ans2 == 'yes':
            sub = 12
            tones = ([abs(x - sub) for x in tones])
            tones = [0 if x == 12 else x for x in tones]
            print(tones)
            break
        if ans2 == 'no':
            print("okay!")
            print(tones)
            break

    while True:
            try: 
                print("Transpose?")
                ans3 = input()
                if ans3 == 'yes':
                    print("Semitones?")
                    trns = int(input())
                    print(trns)
                    tones = [(x + trns) % 12 for x in tones]
                    print(tones)
                    break
                if ans3 == 'no':
                    print("Okay!")
                    print(tones)
                    break
            except ValueError:
                print("Input not accepted. Enter a number.")
                continue

except KeyboardInterrupt:
    print("Interrupt! Bye!")