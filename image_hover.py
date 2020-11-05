from tkinter import *
from PIL import ImageTk, Image


class Hover(Frame):
    """Class that loads an image and hovers it when mouse enters the image"""
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Hovering")
        self.images = ['images/login_button.jpg', 'images/CAP.png']
        self.create_widgets()
        self.bind_image()

    def create_widgets(self):
        """Create image label"""
        self.update_image(self.images[0])
        self.my_label = Label(self.master, image=img)
        self.my_label.pack(padx=30, pady=30)

    def bind_image(self):
        """Bind events with function"""
        self.my_label.bind("<Enter>", self.hover)
        self.my_label.bind("<Leave>", self.hover)

    def hover(self, e):
        """Check event type and update image"""
        index = 1 if str(e.type) == "Enter" else 0
        self.update_image(self.images[index])
        self.my_label.config(image=img)

    @staticmethod
    def update_image(image_path):
        """Load image, resize it and return"""
        global img
        img = Image.open(image_path)
        img = img.resize((408, 136))
        img = ImageTk.PhotoImage(img)
        return img


if __name__ == '__main__':
    root = Tk()
    app = Hover(master=root)
    app.mainloop()
