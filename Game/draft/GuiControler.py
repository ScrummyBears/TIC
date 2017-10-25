from tkinter import *

class GuiControler:    
    def __init__(self, canvas, menu, grid, end):
        self.canvas = canvas
        self.gui = {"menu":menu, "grid":grid, "end":end}
        self.state = "null"
    
    def setState(self, state):
        if state in self.gui.keys():
            self.state = state
            self.display()

    def display(self):
        self.erase()
        self.gui[self.state].display(self.canvas)

    def erase(self):
        self.canvas.delete("all")
        for widget in self.canvas.place_slaves():
            widget.destroy()
        
