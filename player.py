import random
import time


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
        time.sleep(1)
        return square


def minimax(game, move, letter, is_our_move):
    # evaluates our current move and returns the value
    # if we win return 1
    # we lose return -1
    if game.check_winner(move, letter):
        if is_our_move:
            return 1
        else:
            return -1

    # draw return 0
    if not game.empty_squares():
        return 0

    available_squares = game.available_squares()
    next_letter = 'O' if letter == 'X' else 'X'

    if not is_our_move:
        best_value = float('-inf')
        for move in available_squares:
            game.board[move] = next_letter
            value = minimax(game, move, next_letter, True)
            game.board[move] = ' '
            best_value = max(best_value, value)

        return best_value

    else:
        # if none of the above happens then our opponent makes a move
        # so we will evaluate all the available moves and take the minimizing
        worst_value = float('inf')
        for move in available_squares:
            game.board[move] = next_letter
            value = minimax(game, move, next_letter, False)
            game.board[move] = ' '
            worst_value = min(worst_value, value)

        return worst_value


class PerfectComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # add Minimax
        available_squares = game.available_squares()
        # if the first move return a random square
        if len(available_squares) == 9:
            time.sleep(1)
            return random.choice(available_squares)

        best_move = None
        best_value = float('-inf')
        for move in available_squares:
            game.board[move] = self.letter
            value = minimax(game, move, self.letter, True)
            game.board[move] = ' '
            if value > best_value:
                best_value = value
                best_move = move

        time.sleep(1)
        return best_move


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

        # time.sleep(1)
        return square
