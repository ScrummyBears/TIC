from tkinter import *
from TurnManagement import *
from WinLogic import *

from MenuGui import *
from GridGui import *
from GuiControler import *

class TicTacToe:
    def __init__(self):
        self.grid = Grid()
        self.turnHandler = TurnManagement()
        
        self.window = Tk()
        self.window.title("TicTacToe")
        self.canvas = Canvas(self.window, bg= "white" ,height=700, width=1000)
        self.canvas.pack()

        menuGui = MenuGui("images/Menu_GUI.gif", "images/PlayButton.gif")
        gridGui = GridGui("images/GridGui.gif", "images/ButtonGrid.gif",
                          "images/Circle.gif", "images/Cross.gif")

        self.guiCtrl = GuiControler(self.canvas, menuGui, gridGui)
        menuGui.setControler(self.guiCtrl)

    def initializeGame(self):# initialize the guiControler on the state "menu" : it starts the game
        self.guiCtrl.setState("menu")
        
game = TicTacToe()
game.initializeGame()


        
