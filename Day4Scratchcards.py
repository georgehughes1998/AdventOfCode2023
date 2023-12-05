import re

class Solver:
    def solvePart1(self, i):
        return sum([(lambda w, a: (lambda s: 2**(s - 1) if s > 0 else 0)(sum([n in w for n in a])))(*[re.match("Card +\d+: ((?: *\d+ ?)+)\|((?: *\d+ ?)+)", line)[n].split() for n in [1, 2]]) for line in i.splitlines()])

    def solvePart2(self, i):
        return (lambda b: (f:=lambda a, m: m[0] + f(a[1:], [m[1:][v] + m[0]*(v < a[0]) for v in range(len(a)-1)]) if a else 0)(b, [1 for _ in range(len(b))]))([(lambda w, a: sum([n in w for n in a]))(*[re.match("Card +\d+: ((?: *\d+ ?)+)\|((?: *\d+ ?)+)", line)[n].split() for n in [1, 2]]) for line in i.splitlines()])


# (lambda b: (f:=lambda a, m: m[0] + f(a[1:], [m[1:][v] + m[0]*(v < a[0]) for v in range(len(a)-1)]) if a else 0)(b, [1 for _ in range(len(b))]))
