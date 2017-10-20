debug = False

class TurnManagement():
	playerOne = 1
	playerTwo = 2
	currentPlayer = 1
	firstTurnPlayer = 1
	
	def SetCurrentPlayer(self, player):
		TurnManagement.currentPlayer = player
	
	def GetCurrentPlayer(self):
		return TurnManagement.currentPlayer
	
	def ChangePlayer(self):
		if(TurnManagement.currentPlayer == TurnManagement.playerOne):
			TurnManagement.currentPlayer = TurnManagement.playerTwo
		else:
			TurnManagement.currentPlayer = TurnManagement.playerOne
		
	def NewGame(self):
		if(TurnManagement.firstTurnPlayer == TurnManagement.playerOne):
			TurnManagement.currentPlayer = TurnManagement.playerTwo
			TurnManagement.firstTurnPlayer = TurnManagement.playerTwo
		elif(TurnManagement.firstTurnPlayer == TurnManagement.playerTwo):
			TurnManagement.currentPlayer = TurnManagement.playerOne
			TurnManagement.firstTurnPlayer = TurnManagement.playerTwo
		#TurnManagement.currentPlayer = TurnManagement.firstTurnPlayer
		
	def WinnerFound(self, hasWon):
		if(hasWon==1):
			return True
		else:
			return False

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
