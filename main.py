import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x400")  # Nouvelle taille de fenêtre
        self.window.configure(bg='black')  # Couleur de fond noire

        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 40), width=5, height=2,                                              command=lambda row=i, col=j: self.on_click(row, col),
                                              bg='black', fg='white')  # Taille de police ajustée
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)  # Ajuster le padding

    def on_click(self, row, col):
        if self.board[row][col] == '' and not self.check_winner():
            self.board[row][col] = self.current_player
            symbol_color = 'blue' if self.current_player == 'X' else 'red'
            self.buttons[row][col].config(text=self.current_player, fg=symbol_color)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Joueur {self.current_player} gagne!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "Match nul!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True  # Check horizontal
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True  # Check vertical

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True  # Check diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True  # Check diagonal

        return False

    def is_board_full(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', fg='white')  # Réinitialiser la couleur du texte
                self.board[i][j] = ''
        self.current_player = 'X'

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()