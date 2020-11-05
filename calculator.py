# TODO: don't double operation signs
# TODO: Activate sqrt sign
# TODO: Add unittests
# TODO: Check if entry is possible to evaluate

from tkinter import *


class Calculator(Frame):
    """Basic tkinter calculator"""
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Calculator")
        self.create_entry()
        self.create_buttons()

    def create_entry(self):
        """Create entry widget"""
        self.operation = Entry(self.master, width=40)
        self.operation.grid(row=0, column=0, columnspan=4, pady=10, ipady=10)

    def create_buttons(self):
        """Create buttons widgets"""
        btn_text = ["/", "*", "-", "+",
                    7, 8, 9, "sqrt",
                    4, 5, 6, "pow",
                    1, 2, 3, "C",
                    0, ".", "DEL", "="]

        btn_command = [self.button_click] * 15 + \
                      [self.button_clear] + [self.button_click] * 2 + [self.button_del, self.button_equal]

        # Defining buttons in designed grid
        for index, sign in enumerate(btn_text):
            row = 1 + index // 4
            column = index % 4
            btn = Button(self.master, text=sign, width=6, pady=20, command=lambda s=sign, i=index: btn_command[i](s))
            btn.grid(row=row, column=column, columnspan=1)

    def button_click(self, sign):
        """Send sign to entry"""
        self.operation.insert(END, sign)

    def button_clear(self, sign):
        """Clear entire entry"""
        self.operation.delete(0, END)

    def button_equal(self, sign):
        """Evaluate entry"""
        val = eval(self.operation.get())
        self.operation.delete(0, END)
        self.operation.insert(0, val)

    def button_del(self, sign):
        """Clear last entry"""
        index = len(self.operation.get()) - 1
        self.operation.delete(index, END)


if __name__ == '__main__':
    root = Tk()
    app = Calculator(master=root)
    app.mainloop()
