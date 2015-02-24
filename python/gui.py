import tkinter

class MyGUI:
    def __init__(self):
        # create frames and main window
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # create top labels
        self.value = tkinter.StringVar() # this creates a variable for the my_label label to use
        self.my_label = tkinter.Label(self.top_frame,textvariable=self.value)
        self.value.set("YOUR NUMBER HERE")
        self.my_label.pack()

        self.my_label2 = tkinter.Label(self.top_frame,text = "Enter a number")
        self.my_label2.pack()
        # input box
        self.input = tkinter.Entry(self.bottom_frame,width = 10)
        self.input.pack()
        # create button
        self.my_button = tkinter.Button(self.bottom_frame,text = "Enter",command = self.button_function)
        self.my_button.pack(side="right")
        # create quit button
        self.quit_button = tkinter.Button(self.bottom_frame,text = "Quit",command = self.main_window.destroy)
        self.quit_button.pack(side="left")
        # pack frames, enter loop
        self.top_frame.pack(side = "top")
        self.bottom_frame.pack(side = "bottom")
        tkinter.mainloop()
    def button_function(self):
        # executes command
        boxString = self.input.get()
        try:
            userValue = float(boxString)
            userValue += 5
            self.value.set(userValue)
        except ValueError:
            if boxString == "help":
                self.value.set("just enter a number it's not hard")
            else:
                self.value.set("Not a valid number")



my_gui = MyGUI()
