from tkinter import *
from tkinter import colorchooser


class ColorPicker(Frame):
    """Simple class of tkinter ColorPicker"""
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Color picker")
        self.master.geometry("400x400")
        self.btn = Button(root, text="Pick color", command=self.change_background_color)
        self.btn.pack()

    def change_background_color(self):
        """Take color from colorchooser and change background color"""
        self.master.config(bg=colorchooser.askcolor()[1])


if __name__ == '__main__':
    root = Tk()
    app = ColorPicker(master=root)
    app.mainloop()
