"""Python Tkinter GUI Tutorial #97
Threading with Python
"""
from tkinter import *
from random import randint
import threading
import time


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Threading in Tkinter")
        self.create_widgets()

    def create_widgets(self):
        """Create all widgets"""
        self.lbl_1 = Label(self.master, text="Waiting")
        self.lbl_1.pack(pady=10)
        self.lbl_2 = Label(self.master, text="Random Number")
        self.lbl_2.pack(pady=10)

        self.btn_1 = Button(
            master=self.master,
            width=24,
            text="5 seconds",
            command=threading.Thread(target=self.five_seconds).start(),
        )
        self.btn_1.pack(pady=10)
        self.btn_2 = Button(
            master=self.master, width=24, text="Pick Random Number", command=self.rando
        )
        self.btn_2.pack(pady=10)

    def five_seconds(self):
        """Modify lbl_1 text"""
        time.sleep(5)
        self.lbl_1.config(text="5 seconds is Up!")

    def rando(self):
        """Pick random number and config lbl_2"""
        self.lbl_2.config(text=f"Random number: {randint(1, 100)}")


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
