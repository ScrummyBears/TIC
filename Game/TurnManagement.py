debug = False

class TurnManagement():
	playerOne = 1
	playerTwo = 2
	currentPlayer = 1
	firstTurnPlayer = 1
	
	def SetCurrentPlayer(self, player):
		pass
		
	def GetCurrentPlayer(self):
		pass
	
	def ChangePlayer(self):
		pass
		
	def NewGame(self):
		pass
		
	def WinnerFound(self, hasWon):
		pass

if debug:
	tm = TurnManagement()
	print(tm.GetCurrentPlayer())
	tm.NewGame()
	print(tm.GetCurrentPlayer())
	tm.NewGame()
	print(tm.GetCurrentPlayer())
	tm.NewGame()
	print(tm.GetCurrentPlayer())
	print(tm.WinnerFound(1))
