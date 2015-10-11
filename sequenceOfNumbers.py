#!/usr/bin/python3.4

# This program prints sequence of numbers.

a = int(input ("Enter the beginning of the sequence\n"))
b = int(input ("\nEnter the end of the sequence\n"))
c = int(input ("\nEnter step\n"))

for i in range(a, b, c):
    print(i, end=" ")
print()
