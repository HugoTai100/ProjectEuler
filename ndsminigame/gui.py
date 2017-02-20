#simple GUI
from tkinter import *


class App:
    def __init__(self):
        self.master =Tk()
        self.master.title("Mini Game")

        self.mybutton = Button(self.master, text = "Click Here")

        self.mybutton.grid(row = 0, column = 0)
        self.counter = 0
        self.label = Label(self, text='Full name:')
        self.master.mainloop()

    def printMessage(self):
        print("You pressed a button")
        self.counter += 1
        if self.counter >= 5:
            self.mybutton.config(text = "Stop")

App()
