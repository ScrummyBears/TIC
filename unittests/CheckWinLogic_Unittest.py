#This can run independently
import unittest, sys, os

#modifying sys path to import winLogic
lib_path = os.path.abspath(os.path.join('..','Game'))
sys.path.append(lib_path)

from checkWinLogic import WinLogic

#Each def test a specific patern. Hardcoded, yes, but the failure output list per function so 
class CheckWinLogic(unittest.TestCase):
	def test_ClearMatrix_GetGrid_SetGrid(self):
		win = WinLogic()
		self.assertEqual(win.GetGrid(0,0),False)
		win.SetGrid("TEST",0,0)
		self.assertEqual(win.GetGrid(0,0),"TEST")
		win.ClearMatrix()
		self.assertEqual(win.GetGrid(0,0),False)

	def test_SetPlayer_GetPlayer(self):
		win = WinLogic()
		self.assertEqual(win.GetPlayer(),"")
		win.SetPlayer("PlayerOne")
		self.assertEqual(win.GetPlayer(),"PlayerOne")
		win.SetPlayer("PlayerTwo")
		self.assertEqual(win.GetPlayer(),"PlayerTwo")
		
	#check win logic
	def test_hasPlayerWon_CollumnOne(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,0,i)
		self.assertTrue(win.hasPlayerWon(player)) #win case 1

	def test_hasPlayerWon_CollumnTwo(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,1,i)
		self.assertTrue(win.hasPlayerWon(player)) #win case 2
		
	def test_hasPlayerWon_CollumnThree(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,2,i)
		self.assertTrue(win.hasPlayerWon(player)) #win case 3	
	#Check Rows
	def test_hasPlayerWon_RowOne(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,i,0)
		self.assertTrue(win.hasPlayerWon(player)) #win case 4

	def test_hasPlayerWon_RowTwo(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,i,1)
		self.assertTrue(win.hasPlayerWon(player)) #win case 5
		
	def test_hasPlayerWon_RowThree(self): #no winner
		
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(3):
			win.SetGrid(player,i,2)
		self.assertTrue(win.hasPlayerWon(player)) #win case 6
		
	def test_hasPlayerWon_DiagOne(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		win.SetGrid(player,0,0)
		win.SetGrid(player,1,1)
		win.SetGrid(player,2,2)
		self.assertTrue(win.hasPlayerWon(player)) #win case 7
		
	def test_hasPlayerWon_DiagTwo(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		win.SetGrid(player,0,2)
		win.SetGrid(player,1,1)
		win.SetGrid(player,2,0)
		self.assertTrue(win.hasPlayerWon(player)) #win case 8
		
	def test_hasPlayerWon_LoseCaseOne(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(2):
			win.SetGrid(player,0,i)
		self.assertFalse(win.hasPlayerWon(player)) #lose case 1
	
	def test_hasPlayerWon_LoseCaseTwo(self): #no winner
		#Make Class
		win = WinLogic()
		player = "Player1"
		win.SetPlayer(player)
		win.ClearMatrix()
		for i in range(2):
			win.SetGrid(player,0,i)
		win.SetGrid("Player2",0,2)
		self.assertFalse(win.hasPlayerWon(player)) #lose case 1

#unittest.main()
if __name__ == '__main__':
	#hasPayerWon()
    unittest.main()
