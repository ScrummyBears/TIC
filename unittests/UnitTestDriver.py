import unittest, os, sys

#import the actual unit test
import CheckWinLogic_Unittest

print ("\n###################\nChecking CheckWinLogic...\n###################\n")
Test_CheckWinLogic = unittest.TestLoader().loadTestsFromModule(CheckWinLogic_Unittest)
unittest.TextTestRunner(verbosity=2).run(Test_CheckWinLogic)

