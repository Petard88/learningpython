import random, sys

print('Rock, Paper, Scissors!')

#These variables keep track of the score.
wins = 0
losses = 0
ties = 0

while True: #the main loop
    print(f"{wins} Wins, {losses} Losses, {ties} Ties.")
    while True: #the player input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit.')
        playerMove = input()
        if playerMove.lower() == 'q':
            sys.exit() #quit the program
        if playerMove.lower() == 'r' or playerMove.lower() == 'p' or playerMove.lower() == 's':
            break
        print('Type one of r, p, s or q.')

    #Display what the player chose:
    if playerMove.lower() == 'r':
        print('ROCK versus...')
    elif playerMove.lower() == 's':
        print('SCISSORS versus...')
    elif playerMove.lower() == 'p':
        print('PAPER versus...')

    #display what the computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    #Display and record the win/loss/ties
    if playerMove == computerMove:
        print("it's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("You win!")
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print("You win!")
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You loose!")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print("You loose!")
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print("You loose!")
        losses = losses + 1