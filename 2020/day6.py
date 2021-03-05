import collections
import time

class Day5(object):
    def __init__(self, path_):
        self.path = path_
        self.groups = []
        self.answers_ = []

    def preprocess(self):
        file = open(self.path)
        text = file.read().split('\n')
        index = 1
        sum_ = 0
        group = {str(index): None, 'sum': None}
        answers = set()
        answers = []
        for i in text:
            if i != '':
                answers.append(i)
            else:
                to_string = ''.join(answers)
                self.answers_.append([to_string, len(answers)])
                ans = group[str(index)] = to_string
                group['answers'] = answers
                group['!dub'] = set(to_string)
                group['sum'] = len(set(to_string))
                self.groups.append(group)
                index += 1
                group = {str(index): [], 'sum': None, '!dub': None, 'answers': []}
                answers = []

    def part1(self):
        start_time = time.time()
        sum = 0
        index = 1
        for group in self.groups:
            group_sum = group['sum']
            sum += group_sum
            index += 1

        ending_time = time.time()
        execution_time = ending_time - start_time
        print("Time taken to execute part1 = ", execution_time)
        return sum

    def part2_second_sol(self): # More understandable solution
        start_time = time.time()
        sum_ = 0
        for answers in self.answers_:
            sol = collections.Counter(answers[0]).values()
            count = collections.Counter(sol)
            sum_ += count[(answers[1])]
        ending_time = time.time()
        execution_time = ending_time - start_time
        print("Time taken to execute 2nd solution for part2 = ", execution_time)
        return sum_

    def part2(self):   # Ugly solution
        start_time = time.time()
        sum = 0
        index = 1
        for group in self.groups:
            group_ = group[str(index)]
            answers = group['answers']
            if len(answers) == 1:
                sum += len(group_)
            else:
                for char in set(group_):
                    count = group_.count(char)
                    if count == len(answers):
                        sum += 1

            index += 1

        ending_time = time.time()
        execution_time = ending_time - start_time
        print("Time taken to execute first solution for part2 = ", execution_time)
        return sum

day5 = Day5("inputs\day6.txt")
day5.preprocess()
part1_ = day5.part1()
part2_ = day5.part2()
part2second = day5.part2_second_sol()

print("Part1 = ", part1_)
print("Part2 = ", part2_)
print("Part2 second solution = ", part2second)