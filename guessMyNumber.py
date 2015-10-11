#!/usr/bin/python3.4

# This program make a number between 1 and 100.
# You must guess it

import random

a = random.randint(1,100)
i = 0
Z = 'xyz'
print ("\nI made a number between 1 and 100.\n" +
       "Try to guess!")
while i < 7:
    x = input ()
    print()
    if x.isdigit():
        x = int(x)
        if x < a:
            print ("more")
        elif x > a:
            print ("less")
        elif x == a:
            print ("Right!")
            break
    else:
        print ("Wrong input!\nEnter a number, please")
        continue
    i += 1
if i == 7:
    print ("Are you stupid ???!")
print ("it was number " + str(a))
