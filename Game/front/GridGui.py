from tkinter import*

class GridGui:
    
    def __init__(self, pathGui, pathButton, pathCircle, pathCross):
        self.gui = PhotoImage(file = pathGui) 
        self.button = PhotoImage(file = pathButton) #file of the background
        self.circle = PhotoImage(file = pathCircle)
        self.cross = PhotoImage(file = pathCross)
    
        self.button_00 = None     
        self.button_01 = None 
        self.button_02 = None
        
        self.button_10 = None
        self.button_11 = None
        self.button_12 = None

        self.button_20 = None
        self.button_21 = None
        self.button_22 = None

    def setSquare(x, y):
        """Change the square (x,y)"""
        
        pass # use the back end here to set the square
        
    def display(self, can):
        """Display the GUI on a given canvas"""

        height = int(can.cget("height"))
        width = int(can.cget("width"))
        
        can.create_image(width/2 , height/2, image = self.gui)
        
        grille = Frame(can, bg="white",width=600, height=600)
        grille.place(x = 350, y = 50)
        
        self.button_00 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(0, 0))
        self.button_00.grid(row=1,column = 1)

        self.button_01 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(0, 1))
        self.button_01.grid(row=1,column = 2)

        self.button_02 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(0, 2))
        self.button_02.grid(row=1,column = 3)

        self.button_10 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(1, 0))
        self.button_10.grid(row=2,column = 1)

        self.button_11 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(1, 1))
        self.button_11.grid(row=2,column = 2)
        
        self.button_12 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(1, 2))
        self.button_12.grid(row=2,column = 3)

        self.button_20 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(2, 0))
        self.button_20.grid(row=3,column = 1)

        self.button_21 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(2, 1))
        self.button_21.grid(row=3,column = 2)

        self.button_22 = Button(grille, image =  self.button, borderwidth = 1, command = lambda: self.changeSquare(2, 2))
        self.button_22.grid(row=3,column = 3)

#-------Test of the class ----------------------
fen = Tk()
fen.title("test")
    
layout = Canvas(fen,bg= "white" ,height=700, width=1000)
layout.pack()

menu = GridGui("images/GridGui.gif", "images/ButtonGrid.gif", "images/Circle.gif", "images/Cross.gif")
menu.display(layout)

fen.mainloop()
