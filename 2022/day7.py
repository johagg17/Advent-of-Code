
from collections import defaultdict
            
def part1(path: str):
    
    pathList = []
    dirs = defaultdict(int)
    dirsConnection = defaultdict(list)
    with open(path) as f:
        
        for line in f:
            terminalLine = line.replace("\n", "").split(" ")
            if terminalLine[1] == 'cd':
                if terminalLine[2] == '..':
                    pathList.pop()
                    
                else:
                    pathList.append(terminalLine[2])
            elif terminalLine[1] == 'ls':
                continue
            
            elif terminalLine[0] == 'dir':
                dirsConnection[pathList[-1]].append(terminalLine[1])
                continue
            else:
                currentDir = pathList[-1]
                for i in range(len(pathList) + 1):
                   # print('/'.join(pathList[:i]))
                    dirs['/'.join(pathList[:i])] += int(terminalLine[0])
                
    totSum = 0
    for k, v in dirs.items():
        if v <= 100000:
            totSum += v
            
    return totSum
                
def part2(path: str):
    
    pathList = []
    dirs = defaultdict(int)
    dirsConnection = defaultdict(list)
    with open(path) as f:
        
        for line in f:
            terminalLine = line.replace("\n", "").split(" ")
            if terminalLine[1] == 'cd':
                if terminalLine[2] == '..':
                    pathList.pop()
                    
                else:
                    pathList.append(terminalLine[2])
            elif terminalLine[1] == 'ls':
                continue
            
            elif terminalLine[0] == 'dir':
                dirsConnection[pathList[-1]].append(terminalLine[1])
                continue
            else:
                currentDir = pathList[-1]
                for i in range(len(pathList) + 1):
                 #   print('/'.join(pathList[:i]))
                    dirs['/'.join(pathList[:i])] += int(terminalLine[0])
                
    totSum = 0
    totalDiskSpace = 70000000
    spaceNeeded = 30000000
    
    spaceLeft = totalDiskSpace - dirs['/']
    
    print(spaceLeft)
    
    spaceToClear = spaceNeeded - spaceLeft
    print(spaceToClear)
    smallestDisk = 10000000000
    
    for k, v in dirs.items():
        print(k, v)
        
        spaceLeft = totalDiskSpace - dirs['/'] + v
        
        if spaceLeft >= spaceNeeded:
            if v < smallestDisk:
                smallestDisk = v
                
    return smallestDisk

if __name__ =="__main__":
    resPart1 = part1("2022/input/day7.txt")
    print("Part1: ", resPart1)
    
    resPart2 = part2("2022/input/day7.txt")
    print("Part2: ", resPart2)