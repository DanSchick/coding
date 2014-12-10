############
# Danny Schick
# CS 21A
# MPG GUI
############
import tkinter as tk

class myGUI:
    def __init__(self):
        # Create frane and window
        self.winMain = tk.Tk()
        self.topFrame = tk.Frame(self.winMain)
        self.midFrame = tk.Frame(self.winMain)
        self.botFrame = tk.Frame(self.winMain)
        self.buttonFrame = tk.Frame(self.winMain)
        # miles label
        self.milesLabel = tk.Label(self.topFrame,text="Miles Traveled",width=15)
        self.milesLabel.pack(side = "left")
        # input box
        self.milesIn = tk.Entry(self.topFrame, width = 10)
        self.milesIn.pack(side = "right")
        # gallon label
        self.gallonLabel = tk.Label(self.midFrame,text="Gallons Used", width=15)
        self.gallonLabel.pack(side="left")
        # gallon input
        self.gallonIn = tk.Entry(self.midFrame, width=10)
        self.gallonIn.pack(side="right")
        # MPG label
        self.mpgLabel =  tk.Label(self.botFrame, text="Miles Per Gallon:")
        self.mpgLabel.pack(side="left")
        # MPG counter
        self.mpg = tk.StringVar()
        self.mpgCounter = tk.Label(self.botFrame, textvariable=self.mpg)
        self.mpgCounter.pack(side="right")
        # buttons
        self.calculate = tk.Button(self.buttonFrame,text = "Calculate MPG",command = self.calcFunc)
        self.calculate.pack(side="left")
        self.quit = tk.Button(self.buttonFrame, text = "Quit",command = self.winMain.destroy)
        self.quit.pack(side="right")
        # init frames
        self.topFrame.pack(side = "top")
        self.midFrame.pack()
        self.botFrame.pack()
        self.buttonFrame.pack(side = "bottom")
        tk.mainloop()
    def calcFunc(self):
        # calculate MPG
        mileString = self.milesIn.get()
        gallonString = self.gallonIn.get()
        try:
            mileString = float(mileString)
            gallonString = float(gallonString)
            mpg = mileString / gallonString
            self.mpg.set(mpg)
        except BaseException:
            self.mpg.set("NOT VALID INPUTS")


gui = myGUI()
