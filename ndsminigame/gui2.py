from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()

buttomFrame = Frame(root)
buttomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "button 1", bg = "green" , fg = "blue")
button2 = Button(topFrame, text = "button 1", bg = "green", font=("Courier", 100), height= 500 )
button3 = Button(topFrame, text = "button 1", bg = "green")
button4 = Button(topFrame, text = "button 1", bg = "green")

button5 = Button(topFrame, text = "button 1", bg = "green")
button6 = Button(topFrame, text = "button 1", bg = "green")
button7 = Button(topFrame, text = "button 1", bg = "green")
button8 = Button(topFrame, text = "button 1", bg = "green")

button9 = Button(topFrame, text = "button 1", bg = "green")
button10 = Button(topFrame, text = "button 1", bg = "green")
button11 = Button(topFrame, text = "button 1", bg = "green")
button12 = Button(topFrame, text = "button 1", bg = "green")

button13 = Button(topFrame, text = "button 1", bg = "green")
button14 = Button(topFrame, text = "button 1", bg = "green")
button15 = Button(topFrame, text = "button 1", bg = "green")
button16 = Button(topFrame, text = "button 1", bg = "green")

theLabel = Label(root, text = "█", fg = "blue")
theLabel.config()
button4.config(font=("Courier", 100))



button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
button12.pack()
button13.pack()
button14.pack()
button15.pack()
button16.pack()

theLabel.pack()
root.mainloop()