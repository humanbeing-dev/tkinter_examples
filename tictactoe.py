"""This is my tkinter template"""
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")
        # self.master.geometry("400x400")
        self.create_widgets()
        self.possibilites = ["O", "X"]
        self.clicks_counter = 0
        self.results = [["", "", ""], ["", "", ""], ["", "", ""]]

    def create_widgets(self):
        # Create header frame
        self.header_frame = Frame(master=self.master)
        self.header_frame.pack()
        self.lbl = Label(master=self.header_frame, text="Game is on")
        self.lbl.pack()

        # Create game frame
        self.game_frame = Frame(master=self.master)
        self.game_frame.pack()
        # Create buttons
        for i in range(9):
            row = i // 3
            column = i % 3

            btn = Button(master=self.game_frame, text="", width=12, height=6, name=f"button{row}{column}")
            btn.config(command=lambda r=row, c=column, b=btn: self.tic_or_toe(r, c, b))
            btn.grid(row=row, column=column)

    def tic_or_toe(self, row, column, btn):
        print(btn)

        button_clicked = self.game_frame.children[f"button{row}{column}"]
        current_possibility = self.possibilites[self.clicks_counter % 2]
        current_player = (self.clicks_counter % 2) + 1

        button_clicked.config(text=current_possibility)
        self.results[row][column] = current_possibility

        # Check row or column or diagonal 1 or diagonal 2
        if all([self.results[row][i] == current_possibility for i in range(3)])\
                or all([self.results[i][column] == current_possibility for i in range(3)])\
                or all([self.results[i][i] == current_possibility for i in range(3)])\
                or all([self.results[i][2-i] == current_possibility for i in range(3)]):

            self.lbl.config(text=f"Player {current_player} won")
            [self.game_frame.children[button].config(state=DISABLED) for button in self.game_frame.children]

        self.clicks_counter += 1

    # Show when there is a winner


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
