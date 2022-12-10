
from collections import defaultdict

def checkCycle(cycle, dict_: dict, x):
    if cycle in (20, 60, 100, 140, 180, 220):
        dict_[cycle] = cycle * x
    
def part1(path: str):
    x = 1
    cycle = 0
    signalStrength = defaultdict(int)
    with open(path) as f:
        for line in f:
            excLine = line.replace("\n", "")
            
            if excLine == "noop":
                cycle += 1
                checkCycle(cycle, signalStrength, x)
                continue
            
            addx, howMuch = excLine.split(" ")
           # print("Howmuch: ", howMuch)
            tempCycle = 2
            while tempCycle != 0:
                tempCycle -= 1
                cycle += 1 
                checkCycle(cycle, signalStrength, x)
                
                
            x += int(howMuch)
            
    return sum(signalStrength.values())         
            

def draw(ctrDrawings, spriteDrawings, drawPos):
    
    drawing = spriteDrawings[drawPos % 40]
    ctrDrawings.append(drawing)
    
def changeSprite(middlePos, drawings, symbol):
    if middlePos - 1 >= 0:
        drawings[middlePos - 1] = symbol

    if 0 <= middlePos and middlePos <= 39:
        drawings[middlePos] = symbol
    
    if middlePos + 1 <= 39:
         drawings[middlePos + 1] = symbol
         
def part2(path: str):
    x = 1
    cycle = 0
    signalStrength = defaultdict(int)
    
    ctrDrawings = []
    spriteMiddlePos = 1
    spriteDrawings = ["."]*40
    spriteDrawings[0] = spriteDrawings[1] = spriteDrawings[2] = "#"
    with open(path) as f:
        for line in f:
            excLine = line.replace("\n", "")
            
            if excLine == "noop":
                draw(ctrDrawings, spriteDrawings, cycle)
                cycle += 1
                checkCycle(cycle, signalStrength, x)
                
                continue
            
            addx, howMuch = excLine.split(" ")
            tempCycle = 2
            while tempCycle != 0:
                tempCycle -= 1
                draw(ctrDrawings, spriteDrawings, cycle)
                cycle += 1 
                checkCycle(cycle, signalStrength, x)
                
                
            x += int(howMuch)
            changeSprite(spriteMiddlePos, spriteDrawings, ".")
            spriteMiddlePos = x
            changeSprite(spriteMiddlePos, spriteDrawings, "#")
    
    
    for idx, value in enumerate(ctrDrawings):
        if idx % 40 == 0:
            print()
        if value == "#":
            print(value, end="")
        else:
            print(" ", end="")    
    print()      
    return sum(signalStrength.values())                

if __name__ == "__main__":
    resPart1 = part1("2022/input/day10.txt")
    print("Part1: ", resPart1) 
    
    restPart2 = part2("2022/input/day10.txt")
    print("Part2: ", restPart2)       
            