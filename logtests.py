import unittest
from log import Log
from log_entry import LogEntry


class TestSolution(unittest.TestCase):

    def setUp(self):
        with open('autok.txt') as f:
            lines = f.readlines()
        
        self.log = Log(lines)

    def test_task1(self):
        self.assertEqual(len(self.log.entries), 294)

    def test_task2(self):
        self.assertEqual(self.log.findlastcar1(), (30, '19:01', 'CEG307'))

    def test_task3(self):
        expectedEntries = (
            LogEntry('4	12:50	CEG303	561	5065	0'),
            LogEntry('4	19:17	CEG308	552	27998	1')
        )

        result = self.log.findentriesbyday(4)

        self.assertEqual(len(expectedEntries), 2)
        self.assertEqual(expectedEntries[0], result[0])

    def test_task4(self):
        expected = 4
        result = len(self.log.findCarsNotInGarageOnEndOfMonth())
        self.assertEqual(expected, result)

    def test_task5(self):
        expected = {
            'CEG300': 6751,
            'CEG301': 5441,
            'CEG302': 5101,
            'CEG303': 7465,
            'CEG304': 6564,
            'CEG305': 5232,
            'CEG306': 7165,
            'CEG307': 6489,
            'CEG308': 6745,
            'CEG309': 1252
        }

        result = self.log.find_distance_in_month_by_plate2()

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
