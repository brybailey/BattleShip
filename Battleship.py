#Multiple battleships
#Make battleships multiple spaces
#Make it a two player game
from random import randint


ship_row = 0
ship_col = 0
board = []
ships = ['A', 'B', 'C', 'D']
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
#print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def pos_empty(shipx, shipy):
    return board[shipx][shipy] == 'O'

def add_ship(k):
    ship_length = randint(1,3)
    upORaccross = randint(0,1)
    ship_row = random_row(board)
    ship_col = random_col(board)
        #This means the ship goes up 
    if upORaccross == 0:
        while ship_length+ship_row>5:
            ship_col = random_col(board)
        for g in range(ship_length):
            board[ship_row+g][ship_col] = ships[k-1]
    elif upORaccross == 1:
        #if the ship length would take the ship off the screen, pick a new row
        while ship_length+ship_col>5:
            ship_row = random_row(board)
        for i in range(ship_length):
            """if not pos_empty(ship_row+1, ship_col):
                ship_row = random_row(board)
                ship_col = random_col(board)
            else:"""
            board[ship_row][ship_col+i] = ships[k-1]
                


def pop_board(board):
    for x in range(1,5):
        print x
        add_ship(x)

pop_board(board)
print_board(board)
                
                    
                


            




# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print "Turn", turn+1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print_board(board)
if turn == 3:
    print "Game Over"
    board[ship_row][ship_col] = "E"
    print_board( board )
