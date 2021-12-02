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

    def Part2(self: classmethod):
       pass


lines = None
with open('files\day2.txt') as f:
    lines = f.readlines()
    f.close()

day2 = Day2(lines)
sol_part1 = day2.Part1()
print("Solution Part1: {}".format(sol_part1))