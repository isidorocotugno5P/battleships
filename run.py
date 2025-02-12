from random import randint

def generate_board():
    return [["O"] * 10 for _ in range(10)]

def print_board(board, hide_ships=True):
    for row in board:
        print(" ".join("O" if cell == "S" and hide_ships else cell for cell in row))

def random_position():
    return randint(0, 9), randint(0, 9)

def get_user_guess(guessed_positions):
    while True:
        try:
            row = int(input("Guess Row (0-9): "))
            col = int(input("Guess Column (0-9): "))
            if (row, col) in guessed_positions:
                print("You already guessed that position, try again.")
                continue
            if 0 <= row < 10 and 0 <= col < 10:
                return row, col
            print("Invalid input. Enter numbers between 0 and 9.")
        except ValueError:
            print("Please enter a valid number.")

def get_computer_guess(guessed_positions):
    while True:
        row, col = random_position()
        if (row, col) not in guessed_positions:
            return row, col
        
def get_user_guess(guessed_positions):
    while True:
        try:
            row = int(input("Guess Row (0-9): "))
            col = int(input("Guess Column (0-9): "))
            if (row, col) in guessed_positions:
                print("You already guessed that position, try again.")
                continue
            if 0 <= row < 10 and 0 <= col < 10:
                return row, col
            print("Invalid input. Enter numbers between 0 and 9.")
        except ValueError:
            print("Please enter a valid number.")

def get_computer_guess(guessed_positions):
    while True:
        row, col = random_position()
        if (row, col) not in guessed_positions:
            return row, col

def play_turn(player, opponent_board, guessed_positions):
    print(f"{player}'s turn!")
    if player == "User":
        row, col = get_user_guess(guessed_positions)
    else:
        row, col = get_computer_guess(guessed_positions)
        print(f"Computer guessed: {row}, {col}")
    
    guessed_positions.add((row, col))
    
    if opponent_board[row][col] == "S":
        print(f"{player} has sunk the battleship!")
        return True
    else:
        print("Miss!")
        opponent_board[row][col] = "X"
        return False
    
# Initialize boards and positions
user_board = generate_board()
computer_board = generate_board()
user_guesses = set()
computer_guesses = set()

# Place ships
user_ship = random_position()
computer_ship = random_position()
user_board[user_ship[0]][user_ship[1]] = "S"
computer_board[computer_ship[0]][computer_ship[1]] = "S"

turn = 0
while True:
    print("\nUser's Board:")
    print_board(user_board, hide_ships=False)
    print("\nComputer's Board:")
    print_board(computer_board)
    
    if play_turn("User", computer_board, user_guesses):
        print("User wins!")
        break
    if play_turn("Computer", user_board, computer_guesses):
        print("Computer wins!")
        break
    
    turn += 1