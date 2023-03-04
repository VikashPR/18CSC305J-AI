# Monty Hall Game in Python
import random

def play_monty_hall(choice):
    # Prizes behind the door
    # initial ordering doesn't matter
    prizes = ['goat', 'car', 'goat']
    
    # Randomizing the prizes
    random.shuffle(prizes) 
    
    # Determining door without car to open
    while True:
        opening_door = random.randrange(len(prizes))
        if prizes[opening_door] != 'car' and choice-1 != opening_door:
            break
    
    opening_door = opening_door + 1
    print('We are opening the door number-%d' % (opening_door))
    
    # Determining switching door
    options = [1,2,3]
    options.remove(choice)
    options.remove(opening_door)
    switching_door = options[0]
        # Asking for switching the option
    print('Now, do you want to switch to door number-%d? (yes/no)' %(switching_door))
    answer = input()
    if answer == 'yes':
        result = switching_door - 1
    else:
        result = choice - 1
    
    # Displaying the player's prize 
    print('And your prize is ....', prizes[result].upper())
    
# Reading initial choice
choice = int(input('Which door do you want to choose? (1,2,3): '))

# Playing game
play_monty_hall(choice)
