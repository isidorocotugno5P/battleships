from random import randint

# Generating Empty Board
board = []

for x in range(0,10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print(" ".join(row))
        
def random_row(board):
    return randint(0,len(board)-1)

def random_col(board):
    return randint(0,len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(8):
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("You have sunk a battleship!")
    else:
        if (guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
            print("You are way off! Try again with numbers equal to or less than 10")
        elif (board[guess_row][guess_col] == "X"):
            print("You already guessed that, try again!")
        else:
            print("You missed!")
            board[guess_row][guess_col] = "X"
            if turn == 10:
                print("Game Over")
        print_board(board)