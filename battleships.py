from random import randint

board = []
board2 = []

for x in range(10):
    board.append(["O"] * 10)
    board2.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

def print_board2(board):
    for row in board:
        print " ".join(row)

    

player = {
    'ship1' : [],
    'ship2' : [[],[]],
    'ship3' : [[],[],[]]
}

computer = {
    'ship1' : [],
    'ship2' : [[],[]],
    'ship3' : [[],[],[]]
}



print "Let's play Battleship!"
print
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

def random_pos2(row,col,board):
    if row == 1:
        print "row=1"
        if col == 1:
            dir=randint(0,1)
            if dir == 0:
                return [row+1,col]
            elif dir == 1:
                return [row,col+1]

        elif col > 1 and col < len(board):
            dir=randint(0,2)
            if dir == 0:
                return [row,col-1]
            elif dir == 1:
                return [row+1,col]
            elif dir == 2:
                return [row,col+1]

        elif col == len(board):
            dir=randint(0,1)
            if dir == 0:
                return [row,col-1]
            elif dir == 1:
                return [row+1,col]

    elif row > 1 and row < len(board):
        print "1>row>"+str(len(board))
        if col == 1:
            dir=randint(0,2)
            if dir == 0:
                return [row-1,col]
            elif dir == 1:
                return [row,col+1]
            elif dir == 2:
                return [row+1,col]

        elif col > 1 and col < len(board):
            dir=randint(0,3)
            if dir == 0:
                return [row,col-1]
            elif dir == 1:
                return [row+1,col]
            elif dir == 2:
                return [row,col+1]
            elif dir == 3:
                return [row-1,col]

        elif col == len(board):
            dir=randint(0,2)
            if dir == 0:
                return [row,col-1]
            elif dir == 1:
                return [row+1,col]
            elif dir == 2:
                return [row-1,col]

    elif row == len(board):
        print "row="+str(len(board))
        if col == 1:
            dir=randint(0,1)
            if dir == 0:
                return [row-1,col]
            elif dir == 1:
                return [row,col+1]

        elif col > 1 and col < len(board):
            dir=randint(0,2)
            if dir == 0:
                return [row,col-1]
            elif dir == 1:
                return [row-1,col]
            elif dir == 2:
                return [row,col+1]

        elif col == len(board):
            dir=randint(0,1)
            if dir == 0:
                return [row,col-1]
            elif dir == 1:
                return [row-1,col]

def computer_fill(dict):
    dict['ship1'] = [random_row(),random_col()]
    dict['ship2'] = []


ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(100):
    print "Turn", turn+1
    print
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    shippos=random_pos2(guess_row,guess_col,board)
    print shippos
    board[shippos[0]-1][shippos[1]-1] = "X"
    if guess_row == ship_row and guess_col == ship_col:
        print
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 1 or guess_row > 10) or (guess_col < 1 or guess_col > 10):
            print
            print "Oops, that's not even in the ocean."
        elif(board[guess_row-1][guess_col-1] == "X"):
            print
            print "You guessed that one already."
        else:
            print
            print "You missed my battleship!"
            board[guess_row-1][guess_col-1] = "X"
        if turn == 100:
            print "Game Over"
        print
        print_board(board)
