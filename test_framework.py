import unittest
import Day1Trebuchet, Day4Scratchcards



class SolverTestCases:       
    class SolverTestCasesBase(unittest.TestCase):
        @classmethod
        def setUpClass(self, solver, day, part1SampleExpected, part2SampleExpected):
            self.solver = solver
            self.day = day
            self.part1SampleExpected = part1SampleExpected
            self.part2SampleExpected = part2SampleExpected

        def _test_sample(self, part, expected):
            with open(f"input/day{self.day}-{part}sample.txt", "r") as f:
                i = f.read()

            actual = self.solver.solvePart1(i) if part == 1 else self.solver.solvePart2(i)
            self.assertEqual(expected, actual)

        def _test_puzzle_input(self, part):
            with open(f"input/day{self.day}.txt", "r") as f:
                i = f.read()

            answer = self.solver.solvePart1(i) if part == 1 else self.solver.solvePart2(i)
            print(f"Day {self.day} Part {part}: {answer}")

        def test_part1_sample(self):
            self._test_sample(1, self.part1SampleExpected)

        def test_part2_sample(self):
            self._test_sample(2, self.part2SampleExpected)

        def test_part1_puzzle_input(self):
            self._test_puzzle_input(1)

        def test_part2_puzzle_input(self):
            self._test_puzzle_input(2)


class Day4ScratchcardsTest(SolverTestCases.SolverTestCasesBase):
    @classmethod
    def setUpClass(self):
        super().setUpClass(Day4Scratchcards.Solver(), 4, 13, 30)


class Day1TrebuchetTest(SolverTestCases.SolverTestCasesBase):
    @classmethod
    def setUpClass(self):
        super().setUpClass(Day1Trebuchet.Solver(), 1, 142, 281)
