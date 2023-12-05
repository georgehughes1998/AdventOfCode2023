import unittest
import Day1Trebuchet, Day4Scratchcards

class Day1TrebuchetTest(unittest.TestCase):
    def test_part1_sample(self):
        with open("day1-1sample.txt", "r") as f:
            i = f.read()
        
        actual = Day1Trebuchet.Solver().solvePart1(i)
        expected = 142
        self.assertEqual(expected, actual)

    def test_part1_puzzle_input(self): 
        with open("day1.txt", "r") as f:
            i = f.read()
        
        actual = Day1Trebuchet.Solver().solvePart1(i)
        print("Day 1 Answer 1:", actual)

    def test_part2_sample(self):
        with open("day1-2sample.txt", "r") as f:
            i = f.read()
        
        actual = Day1Trebuchet.Solver().solvePart2(i)
        expected = 281
        self.assertEqual(expected, actual)

    def test_part2_puzzle_input(self): 
        with open("day1.txt", "r") as f:
            i = f.read()
        
        actual = Day1Trebuchet.Solver().solvePart2(i)
        print("Day 1 Answer 2:", actual)


class Day4ScratchcardsTest(unittest.TestCase):
    def test_part1_sample(self):
        with open("day4sample.txt", "r") as f:
            i = f.read()

        actual = Day4Scratchcards.Solver().solvePart1(i)
        expected = 13
        self.assertEqual(expected, actual)

    def test_part2_sample(self):
        with open("day4sample.txt", "r") as f:
            i = f.read()

        actual = Day4Scratchcards.Solver().solvePart2(i)
        expected = 30
        self.assertEqual(expected, actual)

    def test_part1_puzzle_input(self):
        with open("day4.txt", "r") as f:
            i = f.read()

        actual = Day4Scratchcards.Solver().solvePart1(i)
        print("Day 4 Answer 1:", actual)

    def test_part2_puzzle_input(self):
        with open("day4.txt", "r") as f:
            i = f.read()

        actual = Day4Scratchcards.Solver().solvePart2(i)
        print("Day 4 Answer 2:", actual)
