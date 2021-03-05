

class Day9():
    def preprocess(self, path):
        file = open(path)
        text = file.read().splitlines()
        int_ = [int(num) for num in text]
        self.data = int_

    def Part1(self, preemable = 25):
        valid = False
        numbers = self.data
        for i, num1 in enumerate(self.data):
            if i >= preemable:
                start_ = i - preemable
                end = i
                values = numbers[start_:end]
                valid = False
                for num2 in values:
                    if abs((num2 - num1)) in values:
                        valid = True
                        break
                if not valid:
                    self.unvalid = num1
                    return num1

    def Part2(self):
        for i, num1 in enumerate(self.data):
            numbers = set()
            numbers.add(num1)
            for num2 in self.data[i:]:
                numbers.add(num2)
                sum_ = sum(numbers)
                if sum_ == self.unvalid:
                    self.summation = max(numbers) + min(numbers)
                    return self.summation
                elif sum_ > self.unvalid:
                    break

path = "inputs\day9.txt"
day9 = Day9()
day9.preprocess(path)
part1_ = day9.Part1(preemable=25)
part2_ = day9.Part2()

print("Part1 = ", part1_)
print("Part2 = ", part2_)