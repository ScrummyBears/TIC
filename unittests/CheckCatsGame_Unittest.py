#This can run independently
import unittest, sys, os

#modifying sys path to import winLogic
lib_path = os.path.abspath(os.path.join('..','Game'))
sys.path.append(lib_path)

from checkWinLogic import WinLogic

#Each def test a specific patern. Hardcoded, yes, but the failure output list per function so 
class TestCheckCatsGame(unittest.TestCase):
	def test_isCatsGame_CaseTrue(self):
		win = WinLogic()
		player1 = "Player1"
		player2 = "Player2"
		win.SetPlayer(player1)
		win.ClearMatrix()
		win.SetGrid(player1, 0, 1)
		win.SetGrid(player1, 0, 2)
		win.SetGrid(player1, 1, 0)
		win.SetGrid(player1, 2, 0)
		win.SetGrid(player1, 2, 2)
		win.SetGrid(player2, 0, 0)
		win.SetGrid(player2, 1, 1)
		win.SetGrid(player2, 1, 2)
		win.SetGrid(player2, 2, 1)
		self.assertTrue(win.isCatsGame(player1, player2))

	def test_isCatsGame_CaseFalse_BoardNotFull(self):
		win = WinLogic()
		player1 = "Player1"
		player2 = "Player2"
		win.SetPlayer(player1)
		win.ClearMatrix()
		win.SetGrid(player1, 2, 0)
		win.SetGrid(player1, 2, 2)
		win.SetGrid(player2, 0, 0)
		win.SetGrid(player2, 1, 1)
		win.SetGrid(player2, 1, 2)
		win.SetGrid(player2, 2, 1)
		self.assertFalse(win.isCatsGame(player1, player2))

	def test_isCatsGame_CaseFalse_WinnerExists(self):
		win = WinLogic()
		player1 = "Player1"
		player2 = "Player2"
		win.SetPlayer(player1)
		win.ClearMatrix()
		win.SetGrid(player1, 0, 0)
		win.SetGrid(player1, 1, 1)
		win.SetGrid(player1, 2, 2)
		win.SetGrid(player1, 2, 1)
		win.SetGrid(player2, 0, 1)
		win.SetGrid(player2, 0, 2)
		win.SetGrid(player2, 1, 0)
		win.SetGrid(player2, 1, 2)
		win.SetGrid(player2, 2, 0)
		self.assertFalse(win.isCatsGame(player1, player2))


#unittest.main()
if __name__ == '__main__':
	#hasPayerWon()
    unittest.main()
