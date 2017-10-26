from tkinter import*

class EndGui:
    def __init__(self, pathGui, pathButtonYes, pathButtonNo):
        self.gui = PhotoImage(file = pathGui) #file of the background
        self.buttonYes = PhotoImage(file = pathButtonYes)
        self.buttonNo = PhotoImage(file = pathButtonNo)

        #controler to communicate with the GuiControler
        self.guiControler = None
        self.gameControler = None

        self.endTxt = ""

    def setEndTxt(self, txt):
        """Set the text display on the end gui (to say which player did win)"""
        self.endTxt = txt
        
    def setGuiControler(self, ctrl):
        """Set the Gui controler to allow the gui to communicate whith it"""
        self.guiControler = ctrl

    def setGameControler(self, ctrl):
        """Set the Game controler to allow the gui to communicate whith it"""
        self.gameControler = ctrl

    def YES(self):
        """Relaunch the game (call when the "yes" button of the interface is press)"""
        self.gameControler.reCreate()
        
    def NO(self):
        """Quit the game (call when the "yes" button of the interface is press)"""
        self.gameControler.window.destroy()
    
    def display(self, can):
        """Display the background and the button on a given canvas"""
        
        height = int(can.cget("height"))
        width = int(can.cget("width"))
        can.create_image(width/2 , height/2, image = self.gui)

        self.lab2 = can.create_text(width/2, 20, text = self.endTxt, font=("Rockwell Extra Bold", 20))
        
        YES = Button(can, image = self.buttonYes, borderwidth = 1, command = self.YES)
        YES.place(x = width/4 , y =height/3 + height/4, anchor='center')
        
        NO = Button(can, image = self.buttonNo, borderwidth = 1, command = self.NO)
        NO.place(x = 3*width/4 , y =height/3 + height/4, anchor='center')

