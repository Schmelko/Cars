import unittest
from log import Log


class TestSolution(unittest.TestCase):

    def setUp(self):
        with open('autok.txt') as f:
            lines = f.readlines()
        
        self.log = Log(lines)

    def test_task1(self):
        self.assertEqual(len(self.log.entries), 294)

    def test_task2(self):
        self.assertEqual(self.log.findlastcar1(), ('30', '19:01', 'CEG307'))


if __name__ == '__main__':
    unittest.main()
