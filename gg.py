outside_colours = ['RED', 'GREEN', 'BLUE', 'YELLOW']

def player_choice(name, choices):
    player_has_chosen_ok = False

    while not player_has_chosen_ok:
        print()
        print('choose a ' + name + ':')
        for i in range(0, len(choices)):
            print(choices[i])

        choice = input('--> ')

        player_has_chosen_ok = (choice in choices)

        if not player_has_chosen_ok:
            print('please choose something on the list')

    return choice

colour_choice = player_choice('colour', outside_colours)

n_letters_in_colour = len(colour_choice)

# RED (3 letters) and GREEN (5 letters) lead to [1, 2, 5, 6]
# BLUE (4 letters) and YELLOW (6 letters) lead to [3, 4, 7, 8]

if n_letters_in_colour in [3, 5]:
    first_number_choices = ['1', '2', '5', '6']
else:
    first_number_choices = ['3', '4', '7', '8']

first_number_chosen = player_choice('number', first_number_choices)

# The next choice is slightly fiddly.  There are four different ways the
# game might have player out so far:
#
# Choose RED or GREEN; show 1256; then choose 1 or 5: next is 3478
# Choose RED or GREEN; show 1256; then choose 2 or 6: next is 1256
# Choose BLUE or YELLOW; show 3478; then choose 3 or 7: next is 1256
# Choose BLUE or YELLOW; show 3478; then choose 4 or 8: next is 3478

if n_letters_in_colour in [3, 5]:
    # The player just chose from 1256

    if first_number_chosen in ['1', '5']:
        second_number_choices = ['3', '4', '7', '8']
    else:
        second_number_choices = ['1', '2', '5', '6']
else:
    # The player just chose from 3478

    if first_number_chosen in ['3', '7']:
        second_number_choices = ['1', '2', '5', '6']
    else:
        second_number_choices = ['3', '4', '7', '8']

second_number_chosen = player_choice('number', second_number_choices)

# Now we know what the player's fortune is!  But first we must convert
# the string to an integer (whole number).

fortune_number = int(second_number_chosen) - 1
print('fortune chosen:')
print(fortune_number)

fortunes = ['You will become very rich!',
            'You will fall into a big hole!',
            'You will find a worm in your next apple!',
            'You will lose your umbrella!',
            'You will dig up some treasure at the beach!',
            'You will turn into a newt!',
            'You will get no homework tomorrow!',
            'You will get eaten by a dragon!']

player_fortune = fortunes[fortune_number]

print()
print(player_fortune)
print()