"""This is example of moving image on canvas using arrowkeys"""

from tkinter import *
from PIL import Image, ImageTk


class MyCanvas(Frame):
    """Canvas with image to move"""
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")
        self.pack()
        self.w = 600
        self.h = 400
        self.create_widgets()

    def create_widgets(self):
        """Function that create widgets"""
        self.my_canvas = Canvas(self, width=self.w, height=self.h, bg="white")
        self.my_canvas.pack()

        global img
        img = ImageOnCanvas.create_image("images/tux.png", 60)
        self.my_image = self.my_canvas.create_image(0, 0, anchor=NW, image=img)
        self.master.bind("<Key>", self.moving)

    def moving(self, event):
        """Move image on canvas"""
        possible_moves = {"Left": (-10, 0), "Right": (10, 0), "Up": (0, -10), "Down": (0, 10)}
        move = possible_moves.get(event.keysym, (0, 0))
        self.my_canvas.move(self.my_image, *move)


class ImageOnCanvas:
    @staticmethod
    def create_image(path, size):
        img = Image.open(path)
        img = img.resize((size, size))
        return ImageTk.PhotoImage(img)


if __name__ == '__main__':
    root = Tk()
    app = MyCanvas(master=root)
    app.mainloop()
