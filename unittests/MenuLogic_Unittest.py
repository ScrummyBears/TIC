#This can run independently
import unittest, sys, os#, unittest.mock

#modifying sys path to import MenuLogic
lib_path = os.path.abspath(os.path.join('..','Game'))
sys.path.append(lib_path)

# noinspection PyUnresolvedReferences
from MenuLogic import MenuLogic

class CheckMenuLogic(unittest.TestCase):
    def test_setPlayerName(self):
        menu = MenuLogic()
        menu.setPlayerName(1, "")
        menu.setPlayerName(2, "John Doe")

        self.assertEqual(menu.player1, "Player 1")
        self.assertEqual(menu.player2, "John Doe")

    def test_launchGame(self):
        menu = MenuLogic()
        menu.launchGame(" ", "John Doe")

        self.assertEqual(menu.player1, "Player 1")
        self.assertEqual(menu.player2, "John Doe")

#unittest.main()
if __name__ == '__main__':
    unittest.main()
