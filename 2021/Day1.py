class Day1():
    def __init__(self, input):
        self.in_list = input
    
    def Part1(self):
        '''
        Given a textfile containing values for depth measurment, count the number of times
         the measurment m increases compared to the previous measurment (m - 1). 
        '''
        l = self.in_list
        count = 0
        previous_m = int(l[0].replace('\n', ''))
        for m in l[1:]:
            new_m = int(m.replace('\n', ''))
            if new_m > previous_m:
                count += 1
            previous_m = new_m

        self.sol_part1 = count    
        return count

    def Part2(self):
        pass


lines = None
with open('files\day1.txt') as f:
    lines = f.readlines()
    f.close()


day1 = Day1(lines)
solution_part1 = day1.Part1()

print("Solution Part1: {}".format(solution_part1))