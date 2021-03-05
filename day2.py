from collections import defaultdict


def checkLimits(min_, max_, count):

    if count >= min_ and count <= max_:
        return True
    return False


def part1(list_):
    valid_count = 0
    for item in list_:
        content = item.split(':')
        policy, password = content[0].split(" "), content[1]
        min_, max_, alpha = int(policy[0]), int(policy[1]), policy[2]
        if checkLimits(min_, max_, password.count(alpha)):
            valid_count += 1


    return valid_count


def check_index(index1, index2, list_, alpha):
    item1, item2 = list_[index1], list_[index2]
    if item1 == alpha and item2 != alpha:
        return 1
    elif item2 == alpha and item1 != alpha:
        return 1
    return 0


def part2(list_):
    valid_count = 0
    for item in list_:
        content = item.split(':')
        policy, password = content[0].split(" "), content[1]
        first_index, second_index, alpha = int(policy[0]), int(policy[1]), policy[2]
        valid_count += check_index(first_index, second_index, password, alpha)


    return valid_count





file = open("inputs\day2.txt", 'r')
text = list((file.read()).replace("-", " ").splitlines())
#print(text)
password_correct_part1 = part1(text)
password_correct_part2 = part2(text)
print("Number of correct passwords (Part1) = ", password_correct_part1)
print("Number of correct passwords (Part2) = ", password_correct_part2)

