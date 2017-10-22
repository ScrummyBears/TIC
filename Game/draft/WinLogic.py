DEFAULT = 0
PLAYER1 = 1
PLAYER2 = 2

class Grid:
        debug = False
        def __init__(self):
                self.matrix = [[0 for x in range(3)] for y in range(3)] 

        def ClearMatrix(self):
                if self.debug:
                        print("Clearing Matrix")
                self.matrix = [[0 for x in range(3)] for y in range(3)]

        def SetGrid(self, player, w, h):
                if self.debug:
                        print ("Setting grid... ", player , " in ", w, ", ", h )
                self.matrix[w][h] = player

        def GetGrid(self, w, h):
                return self.matrix[w] [h]

        def HasPlayerWon(self, x, y):
                
                if self.GetGrid(x, y) != DEFAULT:
                        player = self.GetGrid(x, y)

                        countRow = 0
                        countColumn = 0
                        countDiag1 = 0
                        countDiag2 = 0

                        for i in range(3):
                                if self.GetGrid(x, i) == player: #count values on row
                                        countRow +=1

                                if self.GetGrid(i, y) == player:#count values on columne
                                        countColumn += 1

                                if self.GetGrid(i, i) == player:#count values on the first diagonal
                                        countDiag1 += 1

                                if self.GetGrid(i, 2-i) == player:#count values on second diagonal
                                        countDiag2 += 1

                        score = [countRow, countColumn, countDiag1, countDiag2]

                        if 3 in score: #if one of the line contains 3 of the same player move
                                return True #win
                        else:
                                return False


if __name__ == "__main__":
        m = Grid()
        if m.debug:
                m.SetGrid(1,0,0)
                m.SetGrid(1,1,1)
                m.SetGrid(1,2,2)
                print(m.HasPlayerWon(0,0))
                m.ClearMatrix()
                print(m.HasPlayerWon(0,0))

#m.SetPlayer("Test")
#print m.GetPlayer()
#hasPlayerWon("test")
#print m[0] [0]



