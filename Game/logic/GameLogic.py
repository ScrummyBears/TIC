class GridGame:

        def __init__(self):
                self.matrix = [[0 for x in range(3)] for y in range(3)] 
                self.DEFAULT = 0
                self.PLAYER1 = 1
                self.PLAYER2 = 2
        
        def clearMatrix(self):
                self.matrix = [[0 for x in range(3)] for y in range(3)]

        def setGrid(self, player, w, h):
                self.matrix[w][h] = player

        def getGrid(self, w, h):
                return self.matrix[w][h]

        def hasPlayerWon(self, x, y):
                
                if self.getGrid(x, y) != self.DEFAULT:
                        player = self.getGrid(x, y)

                        countRow = 0
                        countColumn = 0
                        countDiag1 = 0
                        countDiag2 = 0

                        for i in range(3):
                                if self.getGrid(x, i) == player: #count values on row
                                        countRow +=1

                                if self.getGrid(i, y) == player:#count values on columne
                                        countColumn += 1

                                if self.getGrid(i, i) == player:#count values on the first diagonal
                                        countDiag1 += 1

                                if self.getGrid(i, 2-i) == player:#count values on second diagonal
                                        countDiag2 += 1

                        score = [countRow, countColumn, countDiag1, countDiag2]

                        if 3 in score: #if one of the line contains 3 of the same player move
                                return True #win
                        else:
                                return False

