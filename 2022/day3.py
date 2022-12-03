
"""
List of items for each rucksack is given as chars on a single line. 

A rucksack is defined as a input line. 

Compartments: Two are inside of a rucksack, all items of a specific type should belong to the same compartment.

Uppercase and lowercase defines the items. 
 
The two compartments will always have the same number of items, namely the first compartment is the first half
in the rucksack and the second is the second half. 
"""


def getCommonChar(first: str, second: str):
    return set(first).intersection(set(second))

def getCommonChar2(first: str, second: str, third: str):
    return (set(first).intersection(set(second))).intersection(set(third))

def calculatePrio(item: str):
    if item.islower():
            prio = ord(item) - 96
    else:
        prio = ord(item) - 65 + 27
    return prio
"""
lowercase items a through z have prio 1 through 26
uppercase items A-Z have prio 27-52

"""        
def part1(path: str):
    sumPrio = 0
    with open(path) as f:
        for line in f:
            ruckSack = line.replace("\n", "")
            firstComp = ruckSack[:len(ruckSack) // 2]
            secondCom = ruckSack[len(ruckSack) // 2 :]
            
            commonItem = getCommonChar(firstComp, secondCom)
            item = list(commonItem)[0]
            if item.islower():
                prio = ord(item) - 96
            else:
                prio = ord(item) - 65 + 27
            
            sumPrio += prio
    return sumPrio
            

"""
Three elves are now carrying instead each. The common item are the item that exist in all three 
rucksacks.

"""            
def toList(path: str):
    sumPrio = 0
    list_ = []
    with open(path) as f:
        
        for line in f:
            ruckSack = line.replace("\n", "")
            list_.append(ruckSack)
            
    return list_
    
def part2(path: str):
    sumPrio = 0
    finalList = toList(path)
    idx = 0
    for _, _ in enumerate(finalList):
        if idx == len(finalList): break
        elf1 = finalList[idx]
        elf2 = finalList[idx + 1]
        elf3 = finalList[idx + 2]
        commonItem = getCommonChar2(elf1, elf2, elf3)
        item = list(commonItem)[0]
        sumPrio += calculatePrio(item)
        idx += 3
        
    return sumPrio
    
    


if __name__ == "__main__":
    resultPart1 = part1("2022/input/day3.txt")
    print("Part1: ", resultPart1)
    
    resultPart2 = part2("2022/input/day3.txt")
    print("Part2: ", resultPart2)