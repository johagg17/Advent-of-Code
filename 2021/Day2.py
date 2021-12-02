class Day2():
    def __init__(self: classmethod, input: list) -> None:
        self.input_l = input

        self.__process()

    def __process(self: classmethod) -> None:
        self.input_l = [x.replace('\n', '') for x in self.input_l]

    def Part1(self: classmethod) -> int:
        horiz, depth = (0, 0)
        for cmd in self.input_l:
            action, value = cmd.split(' ')
            if action == 'forward': horiz += int(value)
            if action == 'up': depth -= int(value)
            if action == 'down': depth += int(value)

        return horiz * depth

    def Part2(self: classmethod) -> int:
        horiz, depth, aim = (0, 0, 0)
        for cmd in self.input_l:
            action, value = cmd.split(' ')
            value = int(value)
            if action == 'forward': 
                horiz += value
                depth += value*aim
            if action == 'up': aim -= value
            if action == 'down': aim += value

        return horiz * depth


lines = None
with open('files\day2.txt') as f:
    lines = f.readlines()
    f.close()

day2 = Day2(lines)
sol_part1 = day2.Part1()
sol_part2 = day2.Part2()
print("Solution Part1: {}".format(sol_part1))
print("Solution Part2: {}".format(sol_part2))