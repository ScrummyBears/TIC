class TurnManagement:
        def __init__(self):
                self.playerOne = 1
                self.playerTwo = 2
                self.currentPlayer = 1
                self.firstTurnPlayer = 1
                self.turn = 0 #will increment by one each turn
        def setCurrentPlayer(self, player):
                self.currentPlayer = player
	
        def getCurrentPlayer(self):
                return self.currentPlayer

        def changePlayer(self):
                if(self.currentPlayer == self.playerOne):
                        self.currentPlayer = self.playerTwo
                else:
                        self.currentPlayer = self.playerOne

                self.turn += 1
                
        def newGame(self):
                self.turn = 0
                if(self.firstTurnPlayer == self.playerOne):
                        self.currentPlayer = self.playerTwo
                        self.firstTurnPlayer = self.playerTwo
                elif(self.firstTurnPlayer == self.playerTwo):
                        self.currentPlayer = self.playerOne
                        self.firstTurnPlayer = self.playerTwo
                
        def winnerFound(self, hasWon):
                if(hasWon==1):
                        return True
                else:
                        return False

if __name__ == "main":
	tm = TurnManagement()
	print(tm.GetCurrentPlayer())
	tm.NewGame()
	print(tm.GetCurrentPlayer())
	tm.NewGame()
	print(tm.GetCurrentPlayer())
	tm.NewGame()
	print(tm.GetCurrentPlayer())
	print(tm.WinnerFound(1))
