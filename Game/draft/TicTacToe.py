from tkinter import *
from TurnManagement import *
from GameLogic import *
from win import *

from MenuGui import *
from GridGui import *
from GuiControler import *

class TicTacToe:
    def __init__(self):
        self.grid = GridGame()
        self.turnHandler = TurnManagement()
        
        self.window = Tk()
        self.window.title("TicTacToe")
        self.canvas = Canvas(self.window, bg= "white" ,height=700, width=1000)
        self.canvas.pack()
        self.guiCtrl = None

    def reCreate(self):
        self.window.destroy()
        self.__init__()
        self.initializeGame()
        
    def initializeGame(self):# initialize the guiControler on the state "menu" : it starts the game
        menuGui = MenuGui("images/Menu_GUI.gif", "images/PlayButton.gif")
        gridGui = GridGui("images/GridGui.gif", "images/ButtonGrid.gif",
                          "images/Circle.gif", "images/Cross.gif")
        endGui = EndGui("images/end.gif","images/yes.gif","images/no.gif")

        self.guiCtrl = GuiControler(self.canvas, menuGui, gridGui, endGui)
        
        menuGui.setGuiControler(self.guiCtrl)
        
        gridGui.setGameControler(self)
        gridGui.setGuiControler(self.guiCtrl)
        
        endGui.setGameControler(self)
        endGui.setGuiControler(self.guiCtrl)
        
        self.guiCtrl.setState("menu")
        self.window.mainloop()


        
