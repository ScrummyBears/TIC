import tkinter as tk

class Demo1:
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.button1 = tk.Button(self.frame, text = 'Play game', width = 25, command = self.new_window)
		self.button1.pack()
		self.button2 = tk.Button(self.frame, text = 'Close Windows', width = 25, command = self.close_windows)
		self.button2.pack()
		self.frame.pack()

	def new_window(self):
		self.newWindow = tk.Toplevel(self.master)
		self.app = Demo2(self.newWindow)
		
	def close_windows(self):
		self.master.destroy()

class Demo2:
	def __init__(self, master):
		
		self.master = master
		
		self.layout = Canvas(fen,bg= "white" ,height=700, width=1000)
		self.layout.pack()
		
		self.height = int(can.cget("height"))
		self.width = int(can.cget("width"))

		can.create_image(width/2 , height/2, image = self.gui)

		grille = Frame(can, bg="white",width=600, height=600)
		grille.place(x = 350, y = 50)

		self.button_00 = Button(grille)
		self.button_00.grid(row=1,column = 1)

		self.button_01 = Button(grille)
		self.button_01.grid(row=1,column = 2)


	def close_windows(self):
		self.master.destroy()

def main(): 
	root = tk.Tk()
	app = Demo1(root)
	root.mainloop()

if __name__ == '__main__':
	main()
