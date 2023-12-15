import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class User:
    def __init__(self, username):
        self.username = username
        self.scores = {'X': 0, 'O': 0}

    def update_score(self, signe):
        self.scores[signe] += 1

    def get_scores(self):
        return self.scores

def ia(board, signe):
    if not (signe == 'X' or signe == 'O'):
        return False

    empty_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

    if empty_spots:
        return random.choice(empty_spots)
    else:
        return False

class TicTacToe:
    def __init__(self, niveau_ia, ia_function=None):
        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')
        self.current_player = 'X'
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.ia_function = ia_function
        self.user1 = User('Player 1')
        self.user2 = User('Player 2')
        self.niveau_ia = niveau_ia
        self.score_label = tk.Label(self.window, text='', font=('normal', 14))
        self.update_score_label()

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 30), width=10, height=4,
                                              command=lambda row=i, col=j: self.on_click(row, col), bg='white')
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

    def on_click(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, bg='blue' if self.current_player == 'X' else 'red')

            if self.check_winner():
                messagebox.showinfo('Tic Tac Toe', f'Joueur {self.current_player} gagne!')
                if self.current_player == 'X':
                    self.user1.update_score('X')
                else:
                    self.user2.update_score('O')
                self.update_score_label()
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo('Tic Tac Toe', 'Match nul!')
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O' and self.niveau_ia > 0:
                    self.play_ia()

    def play_ia(self):
        if self.ia_function:
            move = self.ia_function(self.board, 'O')
            if move:
                i, j = move
                self.on_click(i, j)

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', bg='white')
                self.board[i][j] = 0
        self.current_player = 'X'

    def update_score_label(self):
        scores = f"Scores: {self.user1.username} - X:{self.user1.get_scores()['X']} O:{self.user1.get_scores()['O']}  |  {self.user2.username} - X:{self.user2.get_scores()['X']} O:{self.user2.get_scores()['O']}"
        self.score_label.config(text=scores)
        self.score_label.grid(row=3, column=0, columnspan=3)

    def run(self):
        self.update_score_label()
        self.window.mainloop()

def main():
    niveau_ia = simpledialog.askinteger('Niveau de l\'IA', 'Choisissez le niveau de l\'IA (0 pour joueur contre joueur) :', initialvalue=1)
    
    if niveau_ia == 0:
        game = TicTacToe(niveau_ia)
    else:
        game = TicTacToe(niveau_ia, ia)
    
    game.run()

if __name__ == "__main__":
    main()