import random
import sys
import balance as pybalance



def shuffleapples():
    # it's recursive but works
    apples = [0, 0, 1, 0, 0]
    random.shuffle(apples)
    fields1 = apples.copy()
     
    random.shuffle(apples)
    fields2 = apples.copy()
     
    random.shuffle(apples)
    fields3 = apples.copy()
     
    apples = [0, 1, 0, 0, 1]
    random.shuffle(apples)
    fields4 = apples.copy()
     
    random.shuffle(apples)
    fields5 = apples.copy()
    apples = [0, 1, 1, 0, 1]
     
    random.shuffle(apples)
    fields6 = apples.copy()
     
    random.shuffle(apples)
    fields7 = apples.copy()
     
    random.shuffle(apples)
    fields8 = apples.copy()
     
    apples = [0, 1, 1, 1, 1]
    random.shuffle(apples)
    fields9 = apples.copy()

    allfields = []
    allfields.append(fields1)
    allfields.append(fields2)
    allfields.append(fields3)
    allfields.append(fields4)
    allfields.append(fields5)
    allfields.append(fields6)
    allfields.append(fields7)
    allfields.append(fields8)
    allfields.append(fields9)

    return allfields


def getodds(i):
    odds = 1
    # firsti = i+1.232
    # nexti = firsti*1.25

    if i+1 == 1:
        odds = 1.54
    elif i+1 == 2:
        odds = 1.93
    elif i+1 == 3:
        odds = 2.41
    elif i+1 == 4:
        odds = 4.02
    elif i+1 == 5:
        odds = 6.71
    elif i+1 == 6:
        odds = 11.18
    elif i+1 == 7:
        odds = 27.97
    elif i+1 == 8:
        odds = 69.93
    elif i+1 == 9:
        odds = 349.68

    return odds


def gamestarter(i, field):
    odds = getodds(i)
    print("\n" + str(i+1) + " Column with x" + str(odds) + "\n")
    # print("\n" + "Data Leak: " + str(field) + "\n")
    whatlist = ["?", "?", "?", "?", "?"]
    print(whatlist)
    choice = int(input("Choose: "))
    choice -= 1

    return choice


def askforstake():
    print("Your Balance is: " + str(pybalance.balance))
    stake = int(input("What's your stake?" + "\n"))
    while stake > pybalance.balance:
        print("Your stake exceeds your balance. Please enter a lower stake or restart the game")
        stake = int(input("What's your stake?" + "\n"))
    pybalance.less_balance(stake)
    print("\n" + "Your stake is " + str(stake) + "\n" + "Gaming starting . . .")
    print("Balance: " + str(pybalance.balance) + "\n\n")
    return stake


def AppleOfFortune():

    stake = askforstake()
    allfields =  shuffleapples()
    winnings = 0

    for i, field in enumerate(allfields):

        choice = gamestarter(i, field)
        odds = getodds(i)

        winnings = stake * odds

        if field[choice] == 0:
            print(field)
            print("You are winning: " + str(winnings))

            if winnings == stake*349.68:
                pybalance.add_balance(winnings)
                print("\n\nYou win winner: " + str(winnings))
                print("Balance: " + str(pybalance.balance) + "\n\n")
                sys.exit()

            eorn = input("\n" + "Press 'w' to take: " + str(winnings) + " or any other key to earn more \n")
            if eorn == "w":
                pybalance.add_balance(winnings)
                print("\n\nYou win: Rs " + str(winnings))
                print("Balance: " + str(pybalance.balance) + "\n\n")
                sys.exit()
            else:
                continue
            

        elif field[choice] == 1:
            print(field)
            print("Oops Rotten apple you lose: " + str(stake))
            print("Balance: " + str(pybalance.balance))
            sys.exit()

        else:
            print("ERROR")




AppleOfFortune()
