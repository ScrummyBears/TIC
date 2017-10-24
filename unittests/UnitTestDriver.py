import unittest, os, sys

#import the actual unit test
import CheckWinLogic_Unittest, CheckCatsGame_Unittest, TurnManagement_Unittest, MenuLogic_Unittest


#Loading the test individually
Test_CheckWinLogic = unittest.TestLoader().loadTestsFromModule(CheckWinLogic_Unittest)
Test_CheckCatsGame = unittest.TestLoader().loadTestsFromModule(CheckCatsGame_Unittest)
Test_TurnManagement = unittest.TestLoader().loadTestsFromModule(TurnManagement_Unittest)
Test_MenuLogic = unittest.TestLoader().loadTestsFromModule(MenuLogic_Unittest)

#Run each test
print ("\n###################\nChecking CheckWinLogic...\n###################\n")
unittest.TextTestRunner(verbosity=2).run(Test_CheckWinLogic)

print ("\n###################\nChecking CheckWinLogic - Cats Game...\n###################\n")
unittest.TextTestRunner(verbosity=2).run(Test_CheckCatsGame)

print ("\n###################\nChecking TurnManagement...\n###################\n")
unittest.TextTestRunner(verbosity=2).run(Test_TurnManagement)

print ("\n###################\nChecking MenuLogic...\n###################\n")
unittest.TextTestRunner(verbosity=2).run(Test_MenuLogic)

