"""This is my tkinter template"""
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")
        self.master.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        pass


if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()
