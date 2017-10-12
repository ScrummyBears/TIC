class WinLogic:
	matrix = [[0 for x in range(3)] for y in range(3)] 
	player = ""
	debug = False
	def __init__(self):
		 return
		 
	def ClearMatrix(self):
		pass
	
	def SetPlayer(self, player):
		pass
		
	def GetPlayer(self):
		pass
	
	def SetGrid(self, val, w, h):
		pass
		
	def GetGrid(self, w, h):
		pass
		
	def hasPlayerWon(self, player):
		pass
			

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
		


