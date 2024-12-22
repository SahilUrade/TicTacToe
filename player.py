import random


class Player:
    def __init__(self, letter):
        # every player has chosen a letter X or O
        self.letter = letter

    # we want to get a move from a player given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_squares())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        available_squares = game.available_squares()
        valid = False
        square = None
        while not valid:
            square = input(f"It's {self.letter}'s turn. Choose a square: {available_squares}\n")
            try:
                square = int(square)
                if square not in available_squares:
                    raise ValueError
                valid = True
            except ValueError:
                print("Please enter a valid square")
        return square
