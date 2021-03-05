

def part1(lines, move_x):
    tree_counter = 0
    jump = right = move_x
    for index in range(0, len(lines) - 1):
        next_line = lines[index + 1][0]
        length = len(next_line)
        if right >= length:
            right = right - length
        if next_line[right] == '#':
            tree_counter += 1
        right += jump

    return tree_counter


def part2(list_):
    data = list_[::2]
    part1_ = part1(data, 1)
    return part1_


with open("inputs\day3.txt", 'r') as f:
    list_ = []
    for line in f.read().splitlines():
        line = line.split(',')
        list_.append(line)
    tree_encounter1 = part1(list_, 1)
    tree_encounter2 = part1(list_, 3)
    tree_encounter3 = part1(list_, 5)
    tree_encounter4 = part1(list_, 7)
    tree_encounter5 = part2(list_)
    print("Part1 = ", tree_encounter2)
    print("Part2 = ", tree_encounter1 * tree_encounter2 * tree_encounter3 * tree_encounter4 * tree_encounter5)
f.close()
