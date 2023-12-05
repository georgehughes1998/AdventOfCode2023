import string, re

class Solver:
    def __init__(self):
        pass

    def solvePart1(self, i):
        return sum([int("".join([[c for c in line if c in string.digits][ix] for ix in (0, -1)])) for line in i.split()])

    def solvePart2(self, i):
        return sum([int("".join([line[ix] for ix in (0, -1)])) for line in [[(dict(zip(["one","two","three","four","five","six","seven","eight","nine"], [str(x) for x in range(1,10)])) | {str(k):str(v) for k, v in zip(range(10), range(10))})[n] for n in re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))", line)] for line in i.split()]
])


