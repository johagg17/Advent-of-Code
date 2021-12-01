class Day1():
    def __init__(self: object, input: list, window: int) -> None:
        self.in_list = input
        self.window = window

        self.__process()
    
    def __process(self: object) -> None: # Private function
        self.in_list = [int(m.replace('\n', '')) for m in self.in_list]

    def Part1(self: object) -> int:
        '''
        Given a textfile containing values for depth measurment, count the number of times
         the measurment increases compared to the previous measurment. 
        '''
        l = self.in_list
        count = 0
        previous_m = int(l[0])
        for m in l[1:]:
            new_m = int(m)
            if new_m > previous_m:
                count += 1
            previous_m = new_m

        self.sol_part1 = count    
        return count

    def Part2(self: object) -> int:
        '''
        Same as Part1 with a slightly modification. Instead of looking at each specific measurement, we now 
        sum togheter 3 mesurments, and then compare it to previous sum. 

        '''
        wind = self.window
        list_ = self.in_list
        prev_sum = sum(list_[:3])
        count = 0
        for m in range(1, len(list_)):
            new_sum = sum(list_[m: m + wind])
            if new_sum > prev_sum: count += 1
            prev_sum = new_sum

        return count


lines = None
with open('files\day1.txt') as f:
    lines = f.readlines()
    f.close()


day1 = Day1(lines, 3)
solution_part1 = day1.Part1()
solution_part2 = day1.Part2()
print("Solution Part1: {}".format(solution_part1))
print("Solution Part2: {}".format(solution_part2))