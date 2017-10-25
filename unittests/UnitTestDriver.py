import unittest, os, sys

#TO USE: place unit test file name (W/O py) in the list of imports and include it in the test_to_run list

#import the actual unit test
import CheckWinLogic_Unittest, CheckCatsGame_Unittest, TurnManagement_Unittest, MenuLogic_Unittest

#initiate test suite to run 
alltests = unittest.TestSuite()

#add unittest file to this list
test_to_run = [CheckWinLogic_Unittest, CheckCatsGame_Unittest, TurnManagement_Unittest, MenuLogic_Unittest]

#appends each test automagially
for test in test_to_run:
	alltests.addTest(unittest.TestLoader().loadTestsFromModule(test))

#runs tests!
unittest.TextTestRunner(verbosity=2).run(alltests)
