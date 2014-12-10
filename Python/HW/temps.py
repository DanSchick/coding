################
# Danny Schick
# CS 21A
# temps.py
##################

import tkinter as tk

class myGUI:
    def __init__(self):
        self.winMain = tk.Tk()
        self.topFrame = tk.Frame(self.winMain)
        self.botFrame = tk.Frame(self.winMain)

        self.celsiusLabel = tk.Label(self.topFrame, text = "Celsius temperature",width=25)
        self.celsiusLabel.pack(side="left")

        self.convert = tk.Button(self.topFrame, text = "Convert",width=20,command=self.convert)
        self.convert.pack(side="right")

        self.fahrLabel = tk.Label(self.topFrame, text = "Fahrenheit temperature", width = 30)
        self.fahrLabel.pack(side="right")

        self.cIn = tk.Entry(self.botFrame,width=25)
        self.cIn.pack(side="left")

        self.quit = tk.Button(self.botFrame,text="Quit",width=20)
        self.quit.pack(side="right")

        self.fValue = tk.StringVar()
        self.fLabel = tk.Label(self.botFrame,width=30, textvariable=self.fValue)
        self.fLabel.pack(side="right")

        self.topFrame.pack(side="top")
        self.botFrame.pack(side="bottom")
        tk.mainloop()
    def convert(self):
        c = self.cIn.get()
        try:
            c = float(c)
            f = ((c*9)/5) + 32
            self.fValue.set(f)
        except BaseException:
            self.fValue.set("Invalid number")



myGUI = myGUI()



