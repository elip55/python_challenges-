import random

def DJscratch(x): # simple function to randomize the computer response 
    random.shuffle(x) # randomize the list
    z = x[0] # pick the first element in the list
    return z # return the random element



game_list = ['rock', 'paper', 'scissors'] # list of strings
"""THE DICTIONARY IS THE TRICK TO THE GAME. AS YOU CAN SEE, EACH KEY BEATS THE VALUE.
    THEREFORE, ANYTIME USER PICKS THE KEY AND THE COMPUTER PICKS THE VALUE, ITS AN EASY IF/ELSE STATEMENT"""
game_dictionary = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'} 

user_choice = input('rock, paper, or scissors ')
counter = DJscratch(game_list)

print(f'you chose {user_choice}')
print(f'system countered with {counter}')

if user_choice == counter:
    print('Tie.  play again')
elif game_dictionary[user_choice] == counter:
    print('you won')
else:
    print('you lose')