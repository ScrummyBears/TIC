import unittest, sys, os

#modifying sys path to import winLogic
lib_path = os.path.abspath(os.path.join('..','Game'))
sys.path.append(lib_path)

#from Main import TicTacToe
from TurnManagement import TurnManagement


class TestTurnManagement(unittest.TestCase):
	def test_TurnManagement_GetCurrentPlayer(self):
		tm = TurnManagement()
		tm.SetCurrentPlayer(1)
		self.assertEqual(tm.GetCurrentPlayer(), 1)
		tm.SetCurrentPlayer(2)
		self.assertEqual(tm.GetCurrentPlayer(), 2)
	
	def test_TurnManagment_ChangePlayer(self):
		tm = TurnManagement()
		tm.SetCurrentPlayer(1)
		tm.ChangePlayer()
		self.assertEqual(tm.GetCurrentPlayer(), 2)
		tm.ChangePlayer()
		self.assertEqual(tm.GetCurrentPlayer(), 1)
		
	def test_TurnManagement_NewGame(self):
		tm = TurnManagement()
		tm.SetCurrentPlayer(1)
		p1 = tm.GetCurrentPlayer()
		tm.NewGame()
		p2 = tm.GetCurrentPlayer()
		tm.NewGame()
		p3 = tm.GetCurrentPlayer()
		self.assertTrue(p1!=p2)
		self.assertTrue(p1==p3)
		
	def test_WinnerFound(self):
		tm = TurnManagement()
		self.assertTrue(tm.WinnerFound(1))
		self.assertFalse(tm.WinnerFound(0))

#unittest.main()
if __name__ == '__main__':
	#hasPayerWon()
    unittest.main()
