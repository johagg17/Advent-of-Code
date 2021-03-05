

class Day10():
    def preprocess(self, path_):
        self.path = path_
        file = open(path_)
        txt = file.read().splitlines()
        self.jolt_list = list(map(int, txt))

    def clear_mem(self):
        self.difftable = {'1': 0, '2': 0, '3': 0}
        self.preprocess(self.path)
        self.difference = 0
        self.highest = max(self.jolt_list)
    def Part1(self):
        self.clear_mem()
        jolt_l = set(self.jolt_list)
        current = 0
        self.way = []
        while current != self.highest:
            if current + 1 in jolt_l:
                self.difference = 1
            elif current + 2 in jolt_l:
                self.difference = 2
            elif current + 3 in jolt_l:
                self.difference = 3
            self.difftable[str(self.difference)] += 1

            current = current + self.difference
            self.way.append(current)
        self.difftable[str(3)] += 1
        self.part1_sol = self.difftable['1']*self.difftable['3']

    def Part2_2Sol(self):
        input_ = self.jolt_list
        input_.append(0)
        input_.sort()
        changes_possible = {}
        for a in (input_[:-1]):
            sum_ = 0
            for x in (a + 1, a + 2, a + 3):
                if x in input_:
                    sum_ += 1
            changes_possible[a] = sum_

        changes_possible[input_[-1]] = 1
        poss = {input_[-1]: changes_possible[input_[-1]]}
        for a in reversed(list(changes_possible.keys())[:-1]):
            sum_ = 0
            for x in (a + 1, a + 2, a + 3):
                val = poss.get(x, 0)
                sum_ += val
            poss[a] = sum_
        self.part2_sol = poss[0]

    def Part2(self): # This solution is working
        from itertools import combinations
        input_ = self.jolt_list
        input_.append(0)
        input_.sort()
        possible  = {}
        possible = {input_[-1]: 1}
        for a in reversed(input_[:-1]):
            sum_ = 0
            for x in (a + 1, a + 2, a + 3):
                sum_ += possible.get(x, 0)
            possible[a] = sum_

path_ = "inputs\day10.txt"
d10 = Day10()
d10.preprocess(path_)
d10.Part1()
d10.Part2()
d10.Part2_2Sol()
print("Part1 = ", d10.part1_sol)
print("Part2 = ", d10.part2_sol)