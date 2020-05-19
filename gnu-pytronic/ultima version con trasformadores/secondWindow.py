 
import tkinter as tk

class SubWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Sub Window")
        self.geometry("400x300+30+30")
        # Change what happens when you click the X button
        # This is done so changes also reflect in the main window class
        self.protocol('WM_DELETE_WINDOW', master.close)

        tk.Button(self, text = "Print", command = self.printMessage).pack()

    def printMessage(self):
        print("Wow this actually worked!")