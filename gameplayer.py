import random

def shuffleapples():
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


def choose_field(field_probs):
    max_prob = max(field_probs)
    candidates = [i for i, prob in enumerate(field_probs) if prob == max_prob]
    return candidates[0]


def play_game():
    allfields = shuffleapples()
    stake = 1
    num_rounds = 0

    while True:
        field_probs = []
        for i, field in enumerate(allfields):
            num_rotten = sum(field)
            num_good = len(field) - num_rotten
            prob_good = num_good / len(field)
            prob_rotten = num_rotten / len(field)
            odds = getodds(i)
            expected_value = prob_good * odds - prob_rotten
            field_probs.append(expected_value)

        choice = choose_field(field_probs)
        num_rounds += 1
        odds = getodds(choice)

        if allfields[choice][2] == 0:
            # stake *= odds

            if odds == 2.41:
                print(f"Won after {num_rounds} rounds!")
                break

        elif allfields[choice][2] == 1:
            print("Oops")


play_game()
