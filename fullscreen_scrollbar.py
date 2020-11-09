"""Application that creates scrollbar along whole tkinter window"""

from tkinter import *
from tkinter import ttk


class FullscreenScrollbar(Frame):
    """Fullscreen Scrollbar class"""
    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("500x400")
        self.create_widgets()

    def create_widgets(self):
        """Create all widgets"""

        # Set the main_frame
        main_frame = Frame(self.master)
        main_frame.pack(fill=BOTH, expand=1)

        # Set the canvas within main_frame
        canvas = Canvas(main_frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=1)

        #
        my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)
        # canvas.yview returns tuple with top and bottom


        canvas.configure(yscrollcommand=my_scroll.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        second_frame = Frame(canvas)
        canvas.create_window((0, 0), window=second_frame, anchor='nw')

        # Create buttons
        for i in range(20):
            # Button(second_frame, width=12, text=f"Click {i}", command=lambda: print(canvas.yview())).grid(row=i, column=0)
            Button(second_frame, width=12, text=f"Click {i}", command=lambda: my_scroll.set(0.0967741935483871, 0.7387096774193549)).grid(row=i, column=0)
            # Button(second_frame, width=12, text=f"Click {i}", command=lambda: print(canvas.bbox('all'))).grid(row=i, column=0)




if __name__ == '__main__':
    root = Tk()
    app = FullscreenScrollbar(master = root)
    app.mainloop()
