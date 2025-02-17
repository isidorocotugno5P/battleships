from random import randint

def generate_board():
    """
    Comment Placeholder
    """
    return [["O"] * 10 for _ in range(10)]

def print_board(board, hide_ships=True):
    """
    Comment Placeholder
    """
    for row in board:
        print(" ".join("O" if cell == "S" and hide_ships else cell for cell in row))

def random_position():
    """
    Comment Placeholder
    """
    return randint(0, 9), randint(0, 9)

def place_ships(board):
    """
    Comment Placeholder
    """
    ship_sizes = [5, 4, 3, 2, 1]
    ships = []
    for size in ship_sizes:
        placed = False
        while not placed:
            row, col = random_position()
            direction = randint(0, 1)  
            
            if direction == 0:  
                if col + size <= 10 and all(board[row][c] == "O" for c in range(col, col + size)):
                    for c in range(col, col + size):
                        board[row][c] = "S"
                    ships.append([(row, c) for c in range(col, col + size)])
                    placed = True
            else:  
                if row + size <= 10 and all(board[r][col] == "O" for r in range(row, row + size)):
                    for r in range(row, row + size):
                        board[r][col] = "S"
                    ships.append([(r, col) for r in range(row, row + size)])
                    placed = True
    return ships

def get_user_guess(guessed_positions):
    """
    Comment Placeholder
    """
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
    """
    Comment Placeholder
    """
    while True:
        row, col = random_position()
        if (row, col) not in guessed_positions:
            return row, col

def check_ship_sunk(ships, hit_position):
    """
    Comment Placeholder
    """
    for ship in ships:
        if hit_position in ship:
            ship.remove(hit_position)
            if not ship:
                print("A ship has been sunk!")
                ships.remove(ship)
            return len(ships) == 0
    return False

def play_turn(player, opponent_board, guessed_positions, opponent_ships):
    """
    Comment Placeholder
    """
    print(f"{player}'s turn!")
    if player == "User":
        row, col = get_user_guess(guessed_positions)
    else:
        row, col = get_computer_guess(guessed_positions)
        print(f"Computer guessed: {row}, {col}")
    
    guessed_positions.add((row, col))
    
    if opponent_board[row][col] == "S":
        """
        Comment Placeholder
        """
        print(f"{player} hit a ship!")
        opponent_board[row][col] = "X"
        if check_ship_sunk(opponent_ships, (row, col)):
            """
            Comment Placeholder
            """
            print(f"{player} has sunk all opponent's ships!")
            return True
    else:
        """
        Comment Placeholder
        """
        print("Miss!")
        opponent_board[row][col] = "X"
    
    return False

print("Welcome to Battleship!")

"""
Comment Placeholder
"""
user_board = generate_board()
computer_board = generate_board()
user_guesses = set()
computer_guesses = set()

"""
Comment Placeholder
"""
user_ships = place_ships(user_board)
computer_ships = place_ships(computer_board)

turn = 0
while True:
    """
    Comment Placeholder
    """
    print("\nUser's Board:")
    print_board(user_board, hide_ships=False)
    print("\nComputer's Board:")
    print_board(computer_board)
    
    """
    Comment Placeholder
    """
    if play_turn("User", computer_board, user_guesses, computer_ships):
        print("User wins!")
        break
    if play_turn("Computer", user_board, computer_guesses, user_ships):
        print("Computer wins!")
        break
    
    turn += 1