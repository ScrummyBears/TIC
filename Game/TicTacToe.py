import sys 

from tkinter import *

sys.path.append(".\gui")
sys.path.append(".\logic")

from GameLogic import*
from Turn_Management import*

from GuiControler import*
from MenuGui import*
from GridGui import*
from Win import*


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
        """Re-initialize the class and game"""
        self.window.destroy()
        self.__init__()
        self.initializeGame()
        
    def initializeGame(self):#
        """initialize the guiControler on the state "menu" : it starts the game"""
        
        menuGui = MenuGui("gui/images/Menu_GUI.gif", "gui/images/PlayButton.gif")
        gridGui = GridGui("gui/images/GridGui.gif", "gui/images/ButtonGrid.gif",
                          "gui/images/Circle.gif", "gui/images/Cross.gif")
        endGui = EndGui("gui/images/end.gif","gui/images/yes.gif","gui/images/no.gif")

        self.guiCtrl = GuiControler(self.canvas, menuGui, gridGui, endGui)
        
        menuGui.setGuiControler(self.guiCtrl)
        
        gridGui.setGameControler(self)
        gridGui.setGuiControler(self.guiCtrl)
        
        endGui.setGameControler(self)
        endGui.setGuiControler(self.guiCtrl)
        
        self.guiCtrl.setState("menu")
        self.window.mainloop()


        
