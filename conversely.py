#!/usr/bin/python3.4

# This program print the mirror of input word

word = input("\nEnter a word\n")
for i in range(len(word)):
    print(word[ -(i+1) ],end="")
print()
