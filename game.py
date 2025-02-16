import random

# snakes and ladders game function
def game():
    
    print("Welcome to Snakes and Ladders Game!")
    print("Player 1 starts at 1 and Player 2 starts at 1.")
    print("The first player to reach 100 wins!")
    print("If you land on a ladder, you will climb up.")
    print("If you land on a snake, you will slide down.")
    print("Good luck!")
    
    print("Player 1 starts!")
    print("Player 1 rolls the dice!")
    
    ladders = [2, 7, 26, 32, 68]
    ladders_corresponding = [38, 12, 78, 55, 91]
    
    snakes = [33, 45, 73, 94, 98]
    snakes_corresponding = [6, 3, 31, 22, 80]
    
    player1 = 1
    player2 = 1
    
    # inclusive 1 - 6
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    while player1 < 100 and player2 < 100:
        
        # player 1
        player1 += dice1
        player1 += dice2
        print(f"Player 1 rolls a {dice1} and a {dice2}! Player 1 is currently at {player1}!")
        if player1 in ladders:
            player1 = ladders_corresponding[ladders.index(player1)]
            print(f"Player 1 lands on a ladder! Player 1 climbs up to {player1}!")
        elif player1 in snakes:
            player1 = snakes_corresponding[snakes.index(player1)]
            print(f"Player 1 lands on a snake! Player 1 slides down to {player1}!")
        
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
          
        # player 2
        player2 += dice1
        player2 += dice2
        print(f"Player 2 rolls a {dice1} and a {dice2}! Player 2 is currently at {player2}!")
        
        if player2 in ladders:
            player2 = ladders_corresponding[ladders.index(player2)]
            print(f"Player 2 lands on a ladder! Player 2 climbs up to {player2}!")
        elif player2 in snakes:
            player2 = snakes_corresponding[snakes.index(player2)]
            print(f"Player 2 lands on a snake! Player 2 slides down to {player2}!")
        
        # inclusive 1 - 6
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
    
    if player1 >= 100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

game()