
def part1_optimized(list_):
    list_ = set(list_)
    for num in list_:
        if str((2020 - int(num))) in list_:
            return int(num) * (2020 - int(num))



def part2_optimized(list_):
    list_ = set(list_)
    for num in list_:
        for num2 in list_:
            if str((2020 - int(num) - int(num2))) in list_:
                return int(num)*int(num2)*(2020 - int(num) - int(num2))



def find_two_entries_to_sum(sum = 2020, list_ = None):
    sum_ = 0
    for i in list_:
        for j in list_:

            sum_ = int(i) + int(j)
           # print(sum_)
            if sum_ == sum:
                return int(i)*int(j)

    return None

def find_three_entries_to_sum(sum = 2020, list_ = None):
    sum_ = 0
    for i in list_:
        for j in list_:
            for k in list_:
                sum_ = int(i) + int(j) + int(k)
                if sum_ == sum:
                    return int(i)*int(j)*int(k)

    return None



file = open("inputs\day1.txt", 'r')
l = list(file.read().splitlines())
part1 = find_two_entries_to_sum(list_=l)
print("Part1 = ", part1)

#part2 = find_three_entries_to_sum(list_=l)
#print("Part2 = ", part2)

print("Part1 optimized = ", part1_optimized(l))
print("Part2 optimized = ", part2_optimized(l))

