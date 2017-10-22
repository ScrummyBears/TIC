from tkinter import *

STATES = {"menu", "grid", "P1win", "P2win", "catGame"}

class GuiControler:    
    def __init__(self, canvas, menu, grid):
        self.canvas = canvas
        self.gui = {"menu":menu, "grid":grid}
        self.state = "null"
    
    def setState(self, state):
        if state in STATES:
            self.state = state
            self.display()

    def display(self):
        self.erase()
        self.gui[self.state].display(self.canvas)

    def erase(self):
        self.canvas.delete("all")
        for widget in self.canvas.place_slaves():
            widget.destroy()
        
