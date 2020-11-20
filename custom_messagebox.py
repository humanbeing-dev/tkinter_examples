"""
Python tkinter GUI Tutorial
# 123 Custom Message Box Popup

Simple example of custom message boxes
"""
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("ProMCS")
        self.master.geometry("400x100")

        self.popup = Button(master=self.master, text="Popup", command=self.show_popup)
        self.popup.pack(pady=10)

        self.lbl = Label(master=self.master, text="")
        self.lbl.pack(pady=10)

    def show_popup(self):
        """Create custom messagebox with yes and no option"""
        self.popup_box = Toplevel(root, background="lightblue")
        self.popup_box.title("Message")
        self.popup_box.geometry("300x80")

        message = Label(master=self.popup_box, text="Do you agree with me?", background="lightblue")
        message.pack(pady=10)

        btn_frame = Frame(master=self.popup_box)
        btn_frame.pack()

        btn_y = Button(master=btn_frame, text="Yes", command=lambda: self.choice("yes"))
        btn_y.grid(row=0, column=0)

        btn_n = Button(master=btn_frame, text="No", command=lambda: self.choice("no"))
        btn_n.grid(row=0, column=1)

    def choice(self, option):
        self.popup_box.destroy()
        if option == "yes":
            self.lbl.config(text=f"You have picked {option}")
        else:
            self.lbl.config(text=f"You have picked {option}")


if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()
