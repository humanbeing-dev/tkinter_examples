"""Application that turn on calendar and gives possibility to get selected date"""

from tkinter import *
from tkcalendar import *
from datetime import date, datetime


class CalendarWidget(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Grab the date")
        self.today = date.today()
        self.create_widgets()

    def create_widgets(self):
        """Function that build all application elements"""
        self.my_button = Button(self.master, text="Get Date", command=self.grab_date)
        self.my_button.pack()
        self.my_label = Label(self.master, text="")
        self.my_label.pack()
        self.cal = Calendar(self.master, selectmode="day", year=self.today.year, month=self.today.month, day=self.today.day)
        self.cal.pack()

    def grab_date(self):
        """function that grabs selected day and print it on the screen"""
        strip_date = datetime.strptime(self.cal.get_date(), "%m/%d/%y")
        format_date = datetime.strftime(strip_date, "%Y-%m-%d")
        self.my_label.config(text=f'{format_date}')


if __name__ == '__main__':
    root = Tk()
    app = CalendarWidget(master=root)
    app.mainloop()
