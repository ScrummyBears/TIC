class MenuLogic:
    player1 = ""
    player2 = ""

    def __init__(self):
        self.player1 = ""
        self.player2 = ""

    def setPlayerName(self, playerNumber, playerName):
        if playerNumber == 1:
            if playerName.strip() == "":
                self.player1 = "Player 1"
            else:
                self.player1 = playerName
        if playerNumber == 2:
            if playerName.strip() == "":
                self.player2 = "Player 2"
            else:
                self.player2 = playerName

    def launchGame(self, playerName1, playerName2):
        self.setPlayerName(1, playerName1)
        self.setPlayerName(2, playerName2)

