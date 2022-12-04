

"""
Input is containing unique ids that represents a section id. 

Each elf is assigned with a range of ids that indicates on what section that this elf will 
need to clean. 

Each line holds two elf ranges: sectionsElf1, sectionsElf2. 

"""


def part1(path: str):
    pairOverlapping = 0
    with open(path) as f:
        for line in f:
            sectionsElf1, sectionsElf2 = line.split(",")
            
            startElf1, endElf1 = sectionsElf1.split("-")
            startElf2, endElf2 = sectionsElf2.split("-")
            
            rangeElf1 = set(range(int(startElf1), int(endElf1) + 1))
            rangeElf2 = set(range(int(startElf2), int(endElf2) + 1))
            overlaps = rangeElf1.intersection(rangeElf2)
            if len(overlaps) == len(rangeElf1) or len(overlaps) == len(rangeElf2):
                pairOverlapping += 1
        
    return pairOverlapping
        
def part2(path: str):
    pairOverlapping = 0
    with open(path) as f:
        for line in f:
            sectionsElf1, sectionsElf2 = line.split(",")
            
            startElf1, endElf1 = sectionsElf1.split("-")
            startElf2, endElf2 = sectionsElf2.split("-")
            
            rangeElf1 = set(range(int(startElf1), int(endElf1) + 1))
            rangeElf2 = set(range(int(startElf2), int(endElf2) + 1))
            overlaps = rangeElf1.intersection(rangeElf2)
            if len(overlaps) > 0:
                pairOverlapping += 1
        
    return pairOverlapping

if __name__ == "__main__":
    resPart1 = part1("2022/input/day4.txt")
    print("Result Part1: ", resPart1)
    
    resPart2 = part2("2022/input/day4.txt")
    print("Result Part2: ", resPart2)