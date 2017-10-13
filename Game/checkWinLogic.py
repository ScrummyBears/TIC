class WinLogic:
	matrix = [[0 for x in range(3)] for y in range(3)] 
	player = ""
	debug = False
	def __init__(self):
		 return
		 
	def ClearMatrix(self):
		if WinLogic.debug:
			print("Clearing Matrix")
		WinLogic.matrix = [[0 for x in range(3)] for y in range(3)]
	
	def SetPlayer(self, player):
		if WinLogic.debug:
			print ("Setting player as: " + player)
		WinLogic.player = player
		
	def GetPlayer(self):
		if WinLogic.debug:
			print ("Returning: " + WinLogic.player)
		return WinLogic.player
	
	def SetGrid(self, val, w, h):
		if WinLogic.debug:
			print ("Setting grid...")
		WinLogic.matrix[w][h] = val
		
	def GetGrid(self, w, h):
		return WinLogic.matrix[w] [h]
		
	def hasPlayerWon(self, player):
		if WinLogic.debug:
			print ("Checking for winner")
		if((WinLogic.matrix[0] [0] == WinLogic.player)and(WinLogic.matrix[1] [0] == WinLogic.player)and(WinLogic.matrix[2] [0] == WinLogic.player)):
			return True
		elif((WinLogic.matrix[0] [1] == WinLogic.player)and(WinLogic.matrix[1] [1] == WinLogic.player)and(WinLogic.matrix[2] [1] == WinLogic.player)):
			return True
		elif((WinLogic.matrix[0] [2] == WinLogic.player)and(WinLogic.matrix[1] [2] == WinLogic.player)and(WinLogic.matrix[2] [2] == WinLogic.player)):
			return True
		if((WinLogic.matrix[0] [0] == WinLogic.player)and(WinLogic.matrix[0] [1] == WinLogic.player)and(WinLogic.matrix[0] [2] == WinLogic.player)):
			return True
		if((WinLogic.matrix[1] [0] == WinLogic.player)and(WinLogic.matrix[1] [1] == WinLogic.player)and(WinLogic.matrix[1] [2] == WinLogic.player)):
			return True
		if((WinLogic.matrix[2] [0] == WinLogic.player)and(WinLogic.matrix[2] [1] == WinLogic.player)and(WinLogic.matrix[2] [2] == WinLogic.player)):
			return True
		if((WinLogic.matrix[0] [0] == WinLogic.player)and(WinLogic.matrix[1] [1] == WinLogic.player)and(WinLogic.matrix[2] [2] == WinLogic.player)):
			return True
		if((WinLogic.matrix[2] [0] == WinLogic.player)and(WinLogic.matrix[1] [1] == WinLogic.player)and(WinLogic.matrix[0] [2] == WinLogic.player)):
			return True
		
		else:
			if WinLogic.debug:
				print ("No Player has won")
			return False
			

m = WinLogic()
if m.debug:
	m.SetPlayer("test")
	m.SetGrid(m.GetPlayer(),0,0)
	m.hasPlayerWon(m.GetPlayer)
	m.ClearMatrix()
	m.hasPlayerWon(m.GetPlayer)

#m.SetPlayer("Test")
#print m.GetPlayer()
#hasPlayerWon("test")
#print m[0] [0]
		


