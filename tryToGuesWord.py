#!/usr/bin/python3.4

"""
I will make a random word and give you 5 atempts to guess a one letter or a whole word.
Then you'll have to try to guess a whole word
"""

import random

WORDS = ("admin", "wake", "street", "welcome", "name", "hello")
print("\nHello! I made a word. Try to guess it!")
secretword = random.choice(WORDS)

print("There is have a " + str(len(secretword)), "letters")

guess = 0
myword = None
letter = None
letters = ""

while guess != 5 and myword != secretword:
    print ("You have", 5 - guess, "attemtps")
    myword = input("Enter your letter or the whole word\n")
    print()
    if len(myword) == 1:
        letter = myword
        if letter in secretword:
            print("Yes. There is a letter \"" + letter + "\" in the word")
        else:
            print("No. There is no such letter \"" + letter + "\" in the word")
    elif len(myword) == len(secretword):
        if myword == secretword:
            print (
            "Right!\n" +\
            "It is word \"" + secretword + "\"")
        else:
            print("No. You're wrong!")
    else:
        print(
        "Wrong letters number.\n" +\
        "Check the number of letters in your word and try again, but your attempt was burned")
    guess += 1

if myword != secretword:
    myword = input(
    "Your attempts has expired\n" +\
    "Please, enter whole word\n")
    print()
    if myword == secretword:
        print (
        "Right!\n" +\
        "It is word \"" + secretword + "\"")
    else:
        print("No. You're wrong!")

