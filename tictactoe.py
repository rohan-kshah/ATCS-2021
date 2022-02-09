import random
from array import *

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    def print_instructions():
        print()
        print("Welcome to Tic Tac Toe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns playing your pieces - the first to 3 in a row wins!")
        print()

    def print_board(self):
        print("  0 1 2")
        for r in range(len(self.board)):
            row = ""
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    row = row + "– "
                elif self.board[r][c] == 1:
                    row = row + "X "
                elif self.board[r][c] == 2:
                    row = row + "O "
            
            print(str(r)+ " " + row)

    def is_valid_move(self, row, col):
        r = row
        c = col
        if (0 > r or r > 2) or (0 > c or c > 2):
            print("Your entry was out of bounds. Has to be between 0 and 2!")
            return False
        if self.board[r][c] != 0:
            print("Your entry was in a spot already filled in.")
            return False 
        return True

    def take_manual_turn(self, player):
        print("Player " + str(player) + "'s turn!")

        row = int(input("Enter the number of the row you want to place in: "))
        col = int(input("Enter the number of the row you want to place in: "))

        while not self.is_valid_move(row,col):
            row = int(input("Please enter a valid row number: "))
            col = int(input("Please enter a valid column number: "))
        
        self.board[row][col] = player

    def take_turn(self, player):
        self.take_manual_turn(player)
        return

    def check_col_win(self, player):
        for c in range(len(self.board)):
                if (player == self.board[0][c]) and (self.board[0][c] == self.board[1][c]) and (self.board[1][c] == self.board[2][c]):
                    return True
        return False

    def check_row_win(self, player):
        for r in range(len(self.board)):
                if (player == self.board[r][0]) and (self.board[r][0] == self.board[r][1]) and (self.board[r][1] == self.board[r][2]):
                    return True
        return False

    def check_diag_win(self, player):
        if (player == self.board[0][0]) and (self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2]):
            return True
        if (player == self.board[0][2]) and (self.board[0][2] == self.board[1][1]) and (self.board[1][1] == self.board[2][0]):
            return True
        return False

    def check_win(self, player):
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == 0:
                    return False
        return True

    def play_game(self):
        TicTacToe.print_instructions()
        self.print_board()

        while not (self.check_win(1) or self.check_win(2) or self.check_tie()):
            self.take_turn(1)
            self.print_board()
            if self.check_win(1):
                print("Player 1 (X) wins.")
                return
            if self.check_tie():
                print("You tied.")
                return
            
            self.take_turn(2)
            self.print_board()
            if self.check_win(2):
                print("Player 2 (O) wins.")
                return 
            if self.check_tie():
                print("You tied.")
                return
        return
