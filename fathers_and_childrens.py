#!/usr/bin/python3.4

# This program finds a father's name by son's name and let you change dict
# For example i took names like "1", "11", "2", "22", "3", "33", etc..

family = {"1":"2", "2":"3", "3":"4", "4":"5", "11":"22", "22":"33", "33":"44", "44":"55"}

choice = None
while choice != 0:
    print ("1 - find father of man\n" +
           "2 - add a pair \"son - father\"\n" +
           "3 - edit a pair \"son - father\"\n" +
           "4 - remove a pair \"son - father\"\n" +
           "0 - exit")
    choice = int(input("You desition?\n"))
    print()
    if choice == 1:
        son = input ("Enter a person name\n")
        while not son in family:
            son = input ("\nThis son doesn't exist\n")
        print("\n" + son + " - is a " + family[son] + "'s son." +
              "\nAnd " + family[son] + " is a " + family[family[son]] + "'s son!")
    elif choice == 2:
        son = input("Add a son\n")
        while son in family:
            print ("\nThis son already exist!")
            son = input("Add a son\n")
        father = input("Add a father\n")
        family[son] = father
        print()
    elif choice == 3:
        son = input ("Enter the name that you want to change\n")
        while not son in family:
            son = input ("\nThis son not exist!\nEnter other son name!\n")
            print()
        father = input ("Add a father\n")
        family[son] = father
        print()
    elif choice == 4:
        son = input ("Enter the name of son that you want to remove\n")
        print()
        while not son in family:
            son = input ("\nThis son not exist!\n")
            print()
        del family[son]
        print()

print ("Good bye")

