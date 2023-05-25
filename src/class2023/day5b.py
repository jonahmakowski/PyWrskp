from random import choice

print('Extra Homework')

rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
player_wins = 0
computer_wins = 0
while True:
    best_of = input('How many rounds would you like (ie, best of 3)\n')
    if best_of.isdigit():
        best_of = int(best_of)
        break

rounds_left = best_of

for attempt in range(1, best_of+1):
    if player_wins > computer_wins + rounds_left:
        print('It is impossible for the computer to win overall')
        break
    elif computer_wins > player_wins + rounds_left:
        print('It is impossible for you to win overall')
        break
    computer = choice(['rock', 'paper', 'scissors'])
    while True:
        player = input('Choose rock, paper or scissors (r,p,s work too!)\n')
        player.lower()
        if (player == 'rock' or player == 'paper') or player == 'scissors':
            break
        elif (player == 'r' or player == 'p') or player == 's':
            if player == 'r':
                player = 'rock'
            elif player == 'p':
                player = 'paper'
            elif player == 's':
                player = 'scissors'
            break
        else:
            print('{} is not valid'.format(player))
        
    if rules[player] == computer:
        print('You won!')
        player_wins += 1
    elif rules[computer] == player:
        print('The computer won this round!')
        computer_wins += 1
    else:
        print('It was a tie')
    print('computer choose {}'.format(computer))
    rounds_left -= 1

if player_wins > computer_wins:
    print('Overall you won!')
elif player_wins < computer_wins:
    print('Overall you lost!')
else:
    print('It was a tie overall')
