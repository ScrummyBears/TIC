from tkinter import*

class GridGui:
    
    def __init__(self, pathGui, pathButton, pathCircle, pathCross):
        self.gui = PhotoImage(file = pathGui) 
        self.button = PhotoImage(file = pathButton)
        self.circle = PhotoImage(file = pathCircle)
        self.cross = PhotoImage(file = pathCross)

        self.P1name = "P1"
        self.P2name = "P2"
        self.currentName = StringVar()
        
        self.labTurn = None
        
        self.matrixButton = None

        self.gameCtrl = None
        self.guiCtrl = None
        
    def setGameControler(self, ctrl):
        self.gameCtrl = ctrl

    def setGuiControler(self, ctrl):
        self.guiCtrl = ctrl
        
    def setName(self, tupleName):
        self.P1name = tupleName[0]
        self.P2name = tupleName[1]
        self.currentName.set(self.P1name)
        
    def setSquare(self, x, y):
        """Change the square (x,y)"""
        grid = self.gameCtrl.grid
        turn = self.gameCtrl.turnHandler
        
        if self.gameCtrl.grid.getGrid(x, y) == grid.DEFAULT:
            player = turn.getCurrentPlayer()
            grid.setGrid(player, x, y)
            
            if player == 1:
                self.currentName.set(self.P2name)
                self.matrixButton[x][y]["image"] = self.circle
                
            if player == 2:
                self.currentName.set(self.P1name)
                self.matrixButton[x][y]["image"] = self.cross

            if grid.hasPlayerWon(x,y):
                if player == 1:
                    self.guiCtrl.gui["end"].setEndTxt("Player 1 won !")
                    
                    self.guiCtrl.setState("end")

                if player == 2:
                    self.guiCtrl.gui["end"].setEndTxt("Player 2 won !")
                    self.guiCtrl.setState("end")

            elif turn.turn >= 8: # if it is the 9th turn and no one has won
                self.guiCtrl.gui["end"].setEndTxt("No one won !")
                self.guiCtrl.setState("end")

                
            turn.changePlayer()
        
    def display(self, can):
        """Display the GUI on a given canvas"""

        height = int(can.cget("height"))
        width = int(can.cget("width"))
        
        can.create_image(width/2 , height/2, image = self.gui)
        
        grille = Frame(can, bg="white",width=600, height=600)
        grille.place(x = 350, y = 50)

        turn = self.gameCtrl.turnHandler
        
        self.labTurn = can.create_text(130, 40, text = self.currentName, font=("Rockwell Extra Bold", 15))
        
        self.button_00 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(0, 0))
        self.button_00.grid(row=1,column = 1)

        self.button_01 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(0, 1))
        self.button_01.grid(row=1,column = 2)

        self.button_02 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(0, 2))
        self.button_02.grid(row=1,column = 3)

        self.button_10 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(1, 0))
        self.button_10.grid(row=2,column = 1)

        self.button_11 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(1, 1))
        self.button_11.grid(row=2,column = 2)
        
        self.button_12 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(1, 2))
        self.button_12.grid(row=2,column = 3)

        self.button_20 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(2, 0))
        self.button_20.grid(row=3,column = 1)

        self.button_21 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(2, 1))
        self.button_21.grid(row=3,column = 2)

        self.button_22 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.setSquare(2, 2))
        self.button_22.grid(row=3,column = 3)

        self.matrixButton = [[self.button_00, self.button_01, self.button_02],
            [self.button_10, self.button_11, self.button_12],
                             [self.button_20, self.button_21, self.button_22]]

#--------------------------Test of the class ----------------------
if __name__ == "__main__":

    fen = Tk()
    fen.title("test")
    
    layout = Canvas(fen,bg= "white" ,height=700, width=1000)
    layout.pack()

    menu = GridGui("images/GridGui.gif", "images/ButtonGrid.gif", "images/Circle.gif", "images/Cross.gif")
    menu.display(layout)

    fen.mainloop()
