"""This is my tkinter template"""
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Tic tac toe game")

        # Create game data
        self.load_variables()

        # Create header frame
        self.header_frame = Frame(master=self.master)
        self.header_frame.pack()
        self.lbl = Label(master=self.header_frame, text="Game is on", font="Helvetica, 20", width=10)
        self.lbl.grid(ipady=10, padx=40, row=0, column=0, columnspan=2)
        self.reset_btn = Button(master=self.header_frame, text="New game", font="Helvetica, 10", command=self.new_game)
        self.reset_btn.grid(ipady=10, row=0, column=2)

        # Create game frame
        self.game_frame = Frame(master=self.master)
        self.game_frame.pack()

        # Create buttons on game_frame
        for i in range(9):

            row = i // 3
            column = i % 3

            btn = Button(master=self.game_frame, text="", width=12, height=6, name=f"button{row}{column}")
            btn.config(command=lambda r=row, c=column, b=btn: self.insert_move(r, c, b))
            btn.grid(row=row, column=column)

    def load_variables(self):
        self.moves = iter(["O", "X"] * 5)
        self.results = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.players = {"O": "Player 1", "X": "Player 2"}
        self.clicked_buttons = []
        self.counter = 0

    def insert_move(self, row, column, btn):
        """Function that takes insert O or X on the board and in the result table"""
        if btn not in self.clicked_buttons:
            self.clicked_buttons.append(btn)
            move = self.moves.__next__()
            self.counter += 1

            btn.config(text=move)
            self.results[row][column] = move

            if self.check_if_there_is_winner(row, column, move):
                self.config_board_after_winning(move)
            elif self.counter == 9:
                self.lbl.config(text=f"There is a tie")

    def check_if_there_is_winner(self, row, column, move):
        """Function that checks all possible wins"""
        chk_row = all([self.results[row][i] == move for i in range(3)])
        chk_col = all([self.results[i][column] == move for i in range(3)])
        chk_dg1 = all([self.results[i][i] == move for i in range(3)])
        chk_dg2 = all([self.results[i][2-i] == move for i in range(3)])

        if any([chk_row, chk_col, chk_dg1, chk_dg2]):
            return True

    def config_board_after_winning(self, move):
        """Config board when the game is over"""
        self.lbl.config(text=f"{self.players[move]} won")
        [self.game_frame.children[button].config(state=DISABLED) for button in self.game_frame.children]

    def new_game(self):
        """Reset variables and buttons"""
        self.load_variables()
        [self.game_frame.children[button].config(text=" ", state=NORMAL) for button in self.game_frame.children]
        self.lbl.config(text=f"Game is on")

    # TODO check if it is a tie


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
