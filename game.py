from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None

    def print_board(self):
        for i in range(3):
            row = self.board[3 * i: 3 * i + 3]
            print(' | '.join(row))

    @staticmethod
    def print_board_nums():
        for i in range(3):
            row = [str(j) for j in range(3 * i, 3 * i + 3)]
            print(' | '.join(row))

    def available_squares(self):
        moves = []
        for i in range(9):
            if self.board[i] == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return len(self.available_squares())

    def make_move(self, move, letter):
        if self.board[move] == ' ':
            self.board[move] = letter
            if self.check_winner(move, letter):
                self.winner = letter
            return True
        return False

    def check_winner(self, move, letter):
        # check the row and column of the move and if possible the diagonal
        # 0 1 2 3 4 5 6 7 8
        # first check row
        count = 0
        if move < 3:
            start = 0
            end = 3
        elif 3 <= move < 6:
            start = 3
            end = 6
        else:
            start = 6
            end = 9

        for i in range(start, end):
            if self.board[i] == letter:
                count += 1
        if count == 3:
            return True

        # checking column
        count = 0
        column = move % 3
        for i in range(column, 9, 3):
            if self.board[i] == letter:
                count += 1
        if count == 3:
            return True

        # checking diagonal
        if move in (0, 2, 4, 6, 8):
            count = 0
            for i in (0, 4, 8):
                if self.board[i] == letter:
                    count += 1
            if count == 3:
                return True

            count = 0
            for i in (2, 4, 6):
                if self.board[i] == letter:
                    count += 1
            if count == 3:
                return True


def play(game, x_player, o_player, print_board=True):
    if print_board:
        game.print_board_nums()

    current_letter = 'X'  # game starts with 'X'

    while game.empty_squares() and game.winner is None:
        # getting a move from the current player
        if current_letter == 'X':
            move = x_player.get_move(game)
        else:
            move = o_player.get_move(game)

        # making the move
        if game.make_move(move, current_letter):
            if print_board:
                print(current_letter + f" made a move to square {move}")
                game.print_board()

            # changing the turn
            if current_letter == 'X':
                current_letter = 'O'
            else:
                current_letter = 'X'

    if game.winner:
        print(game.winner + " won!")
    else:
        print("It's a tie!")


if __name__ == '__main__':
    t1 = TicTacToe()
    playerX = HumanPlayer('X')
    playerO = RandomComputerPlayer('O')
    play(t1, playerX, playerO)
