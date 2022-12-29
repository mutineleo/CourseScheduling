import unittest
import sys
sys.path.append('/Users/a23135334/Documents/Machine Coding/CourseScheduling/python-pip-starter-kit/')
from src.driver import Driver

class CourseSchedulingTest(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
    
    def test_addRegisterAlotCancel(self):
        inputFile = open('tests/resources/input/add_register_alot_cancel.txt').readlines()
        outputFile = open('tests/resources/output/add_register_alot_cancel_output.txt').readlines()
        expectedOutput = [line.split() for line in outputFile]
        output = self.driver.runApp(inputFile)
        self.assertEqual(output,expectedOutput)

    def test_addRegisterAlot(self):
        inputFile = open('tests/resources/input/add_register_alot.txt','r').readlines()
        outputFile = open('tests/resources/output/add_register_alot_output.txt','r').readlines()
        expectedOutput = [line.split() for line in outputFile]
        output = self.driver.runApp(inputFile)
        self.assertEqual(output,expectedOutput)

    def test_addRegisterCancelAlot(self):
        inputFile = open('tests/resources/input/add_register_cancel_alot.txt').readlines()
        outputFile = open('tests/resources/output/add_register_cancel_alot_output.txt').readlines()
        expectedOutput = [line.split() for line in outputFile]
        output = self.driver.runApp(inputFile)
        self.assertEqual(output,expectedOutput)


if __name__ == '__main__':
    unittest.main()
