from random import randint

def generate_board():
    return [["O"] * 10 for _ in range(10)]

def print_board(board, hide_ships=True):
    for row in board:
        print(" ".join("O" if cell == "S" and hide_ships else cell for cell in row))

def random_position():
    return randint(0, 9), randint(0, 9)

