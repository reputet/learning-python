#!/usr/bin/python3.4

# You should make a number from 1 to 100.
# The program will try to guess your number.

i = 0
bottom = 1
up = 101
tryNumber = 50
a = ""

input("\nMake a number in your mind.\nWhen you will be ready, press \"Enter\"\n")
while not a == "r" and i < 10:
    print ("May be your nubmer is", tryNumber, "?")
    a = input ("More, less or right? [m/l/r]\n")
    print()
    if a == "m":
        bottom = tryNumber
        tryNumber = int(tryNumber + ((up - bottom) / 2))
    elif a == "l":
        up = tryNumber
        tryNumber = int(tryNumber - ((up - bottom) / 2))
    elif a == "r":
        print ("I guess! I am so happy!\nIt is number", tryNumber)
    else:
        print ("Wrong input! You have to enter 'm', 'l' or 'r'")
    i += 1
