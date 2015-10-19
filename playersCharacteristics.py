#!/usr/bin/python3.4

# This program

"""
Print main text 2 with Exit, List characteristics, Change characteristics, Change characteristics
Ask me to  choice one of them

if choice "Exit":
    Exit game
elif choice "List characteristics":
    show all characteristics and return to main menu
elif choice "Change characteristics":
    show me all characteristics and ask me output characteristic, count of points, input characteristic.
    Show me new List.
    Return to main menu
"""

pool = [30]

power = [0]
health = [0]
wisdom = [0]
agility = [0]

choice = None

while choice != 0:
    print(
        """\
    0 - Exit
    1 - List characteristics
    2 - Change characteristics\
        """
          )
    choice = int(input("\tYour choice?\n"))
    print()
    
    if choice == 0:
        print ("Good bue")
    elif choice == 1:
        print ("pool = " + str(pool[0]) +
               "\nhealth = " + str(health[0]) +
               "\nwisdom = " + str(wisdom[0]) +
               "\nagility = " + str(agility[0]), end="\n\n")
    elif choice == 2:
        print ("From: \n" +
               "1 - Pool \n" +
               "2 - Health \n" +
               "3 - Wisdom \n" +
               "4 - Agility")
        from_ = int(input(""))

        if from_ == 1:
            from_ = pool
        elif from_ == 2:
            from_ = health
        elif from_ == 3:
            from_ = wisdom
        elif from_ == 4:
            from_ = agility
            
        print()
        count = int(input("Count?\n"))
        print()
        while from_[0] < count:
            print ("Too large count")
            count = int(input("Inter a count\n"))
            print()
        print ("To: \n" +
               "1 - Pool \n" +
               "2 - Health \n" +
               "3 - Wisdom \n" +
               "4 - Agility\n")
        to = int(input(""))

        if to == 1:
            to = pool
        elif to == 2:
            to = health
        elif to == 3:
            to = wisdom
        elif to == 4:
            to = agility
            
        print()
        from_[0] = from_[0] - count
        to[0] = to[0] + count

