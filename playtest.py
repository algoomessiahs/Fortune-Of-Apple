# import json
# from fortuneApple import AppleOfFortune

# # Load initial balance from balance.json
# with open('balance.json') as f:
#     initial_balance = json.load(f)['balance']

# # Set number of rounds to play
# num_rounds = 10

# # Play game for num_rounds and track balance after each round
# balance = initial_balance
# game = AppleOfFortune()
# for i in range(num_rounds):
#     print(f"Round {i+1}:")
#     bet_amount = 30
#     result = game.play(bet_amount)
#     balance += result['payout'] - bet_amount
#     print(f"Result: {result['message']}. Payout: {result['payout']}. Balance: {balance}\n")

# # Save final balance to balance.json
# with open('balance.json', 'w') as f:
#     json.dump({'balance': balance}, f)










import balance as pybalance
import random
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--rounds", dest="rounds", help="Number of rounds")
    parser.add_option("-s", "--stake", dest="stake", help="Stake amount")
    (options, args) = parser.parse_args()
    if not options.rounds:
        parser.error("[-] Please specify a value for the rounds use -h for more")
    elif not options.stake:
        parser.error("[-] Please specify a value for the stake use -h for more")
    else:
        return options

val = get_args()

num_rounds = int(val.rounds)

game_stake = int(val.stake)

choices = [1, 1, 2]

inital_balance = pybalance.balance

# print(len(choices))

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
    stake = game_stake
    # while stake > pybalance.balance:
    #     print("Your stake exceeds your balance. Please enter a lower stake or restart the game")
    #     stake = int(input("What's your stake?" + "\n"))
    pybalance.less_balance(stake)
    print("\n" + "Your stake is " + str(stake) + "\n" + "Gaming starting . . .")
    print("Balance: " + str(pybalance.balance) + "\n\n")
    return stake



def autoAppleOfFortune():
    stake = askforstake()
    allfields =   shuffleapples()
    winnings = 0

    wins = 0
    losses = 0


    for i, field in enumerate(allfields):

        # choice = gamestarter(i, field)
        choice = (choices[i]) - 1
        odds =  getodds(i)

        winnings = stake * odds

        if field[choice] == 0:
            print(field)
            print("You are winning: " + str(winnings))

            if winnings == stake*349.68:
                wins += 1
                pybalance.add_balance(winnings)
                print("\n\nYou win winner: " + str(winnings))
                print("Balance: " + str(pybalance.balance) + "\n\n")
                break

            # eorn = input("\n" + "Press 'w' to take: " + str(winnings) + " or any other key to earn more \n")
            if len(choices) == (i+1):
                eorn = "w"
            else:
                eorn = "p"

            if eorn == "w":
                pybalance.add_balance(winnings)
                wins += 1
                print("\n\nYou win: Rs " + str(winnings))
                print("Balance: " + str(pybalance.balance) + "\n\n")
                break
            else:
                continue
            

        elif field[choice] == 1:
            losses += 1
            print(field)
            print("Oops Rotten apple you lose: " + str(stake))
            print("Balance: " + str(pybalance.balance))
            break

        else:
            print("ERROR")

    return wins


for i in range(num_rounds):
    print("\n\n\n\n\n Round: " + str(i) + "\n\n\n\n\n")
    wins = autoAppleOfFortune()


lojez = num_rounds - wins

print( "\n\n\nYour initial balance was: " + str(inital_balance) + "And now you have " + str(pybalance.balance))
print("You played a " + str(num_rounds) + "games with the stake " + str(game_stake) + " Each game")
print("Games: " + str(num_rounds) + " Wins: " + str(wins) + " Losses: " + str(lojez) + "\n\n\n\n\n")
