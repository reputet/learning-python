#!/usr/bin/python3.4

# This program take a WORDS list and return their elements in random secuence

import random

WORDS = ["One", "Two", "Three", "Four", "Five"]
newlist = []

while WORDS:
    position = random.randrange(len(WORDS))
    newlist.append(WORDS[position])
    WORDS = WORDS[:position] + WORDS[(position + 1):]

for i in range(len(newlist)):
    print (newlist[i], end=" ")
print()
