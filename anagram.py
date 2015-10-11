#!/usr/bin/python3.4

# This program show you some letters, and you need to regularize them to get the word.

import random

WORDS = ("first", "mister", "philosophy", "exchange", "workaround", "available")
word = random.choice(WORDS)
according = word
anagram = ""

while word:
    position = random.randrange(len(word))
    anagram += word[position]
    word = word[:position] + word[(position + 1):]


print("\nMake word correctly. You have to swap letters\n" + anagram)

myword = input()
hint = 0
while myword != according:
    if myword == "":
        if hint >= len(according) - 1:
            print("Enough. Next try yourself\nYour open letters is: " + according[:hint])
            myword = input()
        else:
            hint += 1
            print("Hint!\nWord begins with the " + according[:hint])
            myword = input()
    else:
        print ("\nWrong!\nTry again.\nYour anagram is: " + anagram)
        myword = input()
print("\nExcellent!")
print("Your score: ", len(according) - hint)
