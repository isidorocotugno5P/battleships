import random
import colorama
import os
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


class GameBoard:
    """
    This class represents the Battleship game board.

    It holds functions for board creation,
    board display, and placement of ships.
    """
    def __init__(self, size=10):
        """
        Sets size of game board, the default size for this game is 10x10.
        """
        self.size = size
        self.grid = [["O"] * size for _ in range(size)]

    def display(self, hide_ships=True):
        """
        Displays grid to terminal to become visible to user.

        Displays "O" for empty spots, "S" for the ships themselves,
        and "X" for any time a player hits a ship.
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == "S" and hide_ships:
                    print("O", end=" ")
                else:
                    print(self.grid[i][j], end=" ")
            print()

    def place_ships(self):
        """
        Randomly places ships onto the board without causing ships to overlap.

        Return a dictionairy with the value being the position of the ship,
        as well as its hit count.
        """
        fleet_sizes = [5, 4, 3, 2, 1]  # List of all ship sizes
        fleet = {}
        for size in fleet_sizes:
            placed = False
            while not placed:
                row, col = self.get_random_position()
                # Chooses randomly between horizontal and vertical placement
                direction = random.choice(["H", "V"])
                if direction == "H":
                    # Makes sure there is space for the ship and no overlap
                    if col + size <= self.size and all(
                        self.grid[row][c] == "O" for c in range(
                            col, col + size)
                    ):
                        for c in range(col, col + size):
                            self.grid[row][c] = "S"
                        fleet[size] = {
                            "coords": [(row, c) for c in range(
                                col, col + size)],
                            "hits": 0,
                        }
                        placed = True
                else:
                    if row + size <= self.size and all(
                        self.grid[r][col] == "O" for r in range(
                            row, row + size)
                    ):
                        for r in range(row, row + size):
                            self.grid[r][col] = "S"
                        fleet[size] = {
                            "coords": [(r, col) for r in range(
                                row, row + size)],
                            "hits": 0,
                        }
                        placed = True
        return fleet

    def get_random_position(self):
        """
        Returns a random position (2 values: column and row) on the board,
        for the ship placement function.
        """
        return random.choice(range(self.size)), random.choice(range(self.size))

    def get_user_guess(self, guessed_positions):
        """
        Gets a valid guess from the user, excluding letters, special symbols,
        any number outside of the board,
        and any position that has already been guessed.
        """
        while True:
            try:
                row = int(input("\nGuess Row (1-10): ")) - 1
                col = int(input("Guess Column (1-10): ")) - 1
                if (row, col) in guessed_positions:
                    print("You already guessed that position, try again.")
                    continue
                if 0 <= row < self.size and 0 <= col < self.size:
                    return row, col
                print("Invalid input. Enter numbers between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")


class BattleshipGame:
    """
    Controls the sequence of the battleship game, this includes turns,
    win/loss detection, and computer and user guesses.
    """
    def __init__(self):
        """
        Starts game and creates both game boards
        and initiates placement of both players ships

        Also initiates and collected both computer and players guesses
        """
        self.user_board = GameBoard()
        self.computer_board = GameBoard()
        self.user_ships = self.user_board.place_ships()
        self.computer_ships = self.computer_board.place_ships()
        self.user_guesses = set()
        self.computer_guesses = set()

    def play_turn(self, player):
        """
        Initiates turn for player, handling both turns for computer and player
        """
        if player == "User":
            row, col = self.user_board.get_user_guess(self.user_guesses)
        else:
            row, col = self.computer_board.get_random_position()
            while (row, col) in self.computer_guesses:
                row, col = self.computer_board.get_random_position()
            print(f"Computer guessed: {row + 1}, {col + 1}")

        # Updates targeted board

        target_board = (
            self.computer_board if player == "User" else self.user_board)
        guessed_positions = (
            self.user_guesses if player == "User" else self.computer_guesses)
        ships = self.computer_ships if player == "User" else self.user_ships
        guessed_positions.add((row, col))

        if target_board.grid[row][col] == "S":
            """
            Updates symbols on board to indicate hit or miss
            """
            print(Fore.GREEN + f"{player} hit a ship!")
            target_board.grid[row][col] = "X"
            for ship_size, ship in list(ships.items()):
                if (row, col) in ship["coords"]:
                    ship["hits"] += 1
                    if ship["hits"] == len(ship["coords"]):
                        print(Back.GREEN + f"{player} has sunk a ship!")
                        del ships[ship_size]
                    break
        else:
            print(Fore.RED + "Miss!")
            target_board.grid[row][col] = "M"

    def play_game(self):
        """
        Starts the actual game and runs until computer or user sinks all ships
        """
        print("Welcome to Battleship!\n")
        print("Instructions: Guess a number between 1-10 for a row and column")
        print("'S' marks a ship, 'X' marks a hit, and 'M' marks a miss")
        while True:
            # Prints each players board, for each iteration of the loop
            print("\nUser's Board:")
            self.user_board.display(hide_ships=False)
            print("\nComputer's Board:")
            self.computer_board.display()

            # Checks for winner
            if not self.computer_ships:
                print(Back.GREEN + "User wins!")
                print(
                    "In order to replay the game, please rerun the program\n")
                break
            if not self.user_ships:
                print(Back.RED + "Computer wins!")
                print(
                    "In order to replay the game, please rerun the program\n")
                break

            # Turn taking part of loop
            self.play_turn("User")
            self.play_turn("Computer")


if __name__ == "__main__":
    """
    Protects user from accidentally invoking script

    Only initiates when intended
    """
    game = BattleshipGame()
    game.play_game()
