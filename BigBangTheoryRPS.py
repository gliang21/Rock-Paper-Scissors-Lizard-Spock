import random, sys

print('Rock, Paper, Scissors, Lizard, Spock')

#these variables keep  track of wins,losses,and ties
wins = 0
losses = 0
ties = 0

while True: #the main game loop.
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    while True: #the player input loops
        print ('Enter your move: (r)ock (p)aper (s)cissors (l)izard sp(o)ck or (q)uit')
        print('Type either r, p, s, l, o or q \n')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's' or playerMove == 'l' or playerMove == 'o':
            break #break out of the player loop.


    #Display what the player chose:
    if playerMove == 'r':
        print ('Rock vs ')
    elif playerMove == 'p':
        print('Paper vs '  )
    elif playerMove == 's':
        print('Scissors vs ' )
    elif playerMove == 'l':
        print('Lizard vs '  )
    elif playerMove == 'o':
        print('Spock vs '  )

    #displays what the computer chose:
    randomNumber = random.randint(1,5)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock \n')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper\n')
    elif randomNumber == 3:
        computerMove = 's'
        print('scissors\n')
    elif randomNumber == 4:
        computerMove = 'l'
        print('lizard\n')
    elif randomNumber == 5:
        computerMove = 'o'
        print('spock\n')

    #Display and reord the W/L ratio.
    if playerMove == computerMove:
        print('It is a tie!\n')
        ties = ties + 1
    #record wins
    elif playerMove == 'r' and computerMove == 's':
        print('You win!\n')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'l':
        print('You win!\n')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!\n')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!\n')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'l':
        print('You win!\n')
        wins = wins + 1
    elif playerMove == 'l' and computerMove == 'p':
        print('You win!\n')
        wins = wins + 1
    elif playerMove == 'l' and computerMove == 'o':
        print('You win!\n')
        wins = wins + 1
    elif playerMove == 'o' and computerMove == 'r':
        print('You win!\n')
        wins = wins + 1
    elif playerMove == 'o' and computerMove == 's':
        print('You win!\n')
        wins = wins + 1

        #record losses
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 'o':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'o':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'l':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'o':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 'l' and computerMove == 's':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 'l' and computerMove == 'r':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 'o' and computerMove == 'p':
        print('You lose!\n')
        losses = losses + 1
    elif playerMove == 'o' and computerMove == 'l':
        print('You lose!\n')
        losses = losses + 1