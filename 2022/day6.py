     
def part1():
    with open("2022/input/day6.txt") as f:
        buffer = f.readline()
        
        for idx, char in enumerate(buffer):
            datastream = buffer[idx: idx + 4]
            if len(set(datastream)) == len(datastream):
                return idx + 4

def part2():
    with open("2022/input/day6.txt") as f:
        buffer = f.readline()
        
        for idx, char in enumerate(buffer):
            datastream = buffer[idx: idx + 14]
            if len(set(datastream)) == len(datastream):
                return idx + 14

if __name__=="__main__":
    resPart1 = part1()
    print("ResultPart1: ", resPart1)
    
    resPart2 = part2()
    print("ResultPart2: ", resPart2)
    
     