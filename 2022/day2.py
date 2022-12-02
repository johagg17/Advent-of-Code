
"""
A: Rock
B: Paper
C: Scisscors

X: Rock
Y: Paper
Z: Scissors

"""
combinations = {"A&Y":1, "A&X":0, "A&Z":-1, 
                "B&Y":0, "B&X":-1, "B&Z":1, 
                "C&Y":-1, "C&X":1, "C&Z":0
                }

values = {"X":1, "Y":2, "Z":3}

def calculateWin(oppMove: str, myMove: str):
    roundStr = oppMove + "&" + myMove
    roundResult = combinations[roundStr]
    score = 0
    if roundResult == 1: # Win
        score = values[myMove] + 6
    elif roundResult == -1: # Loss
        score = values[myMove] + 0
    elif roundResult == 0: # Draw
        score = values[myMove] + 3
    return score

def part1(file: str):
    totalScore = 0
    with open(file) as f:
        for line in f:
            processedLine = line.replace('\n', '').split(" ")
            
            opponentMove, myMove = processedLine
            totalScore += calculateWin(opponentMove, myMove)
            
    return totalScore

"""
Y means do draw
X means loose
Z means win
"""
        
move = {"A&Y":"X", "A&X":"Z", "A&Z":"Y", 
        "B&Y":"Y", "B&X":"X", "B&Z":"Z", 
        "C&Y":"Z", "C&X":"Y", "C&Z":"X"
        }
    
def part2(file: str):
    totalScore = 0
    with open(file) as f:
        for line in f:
            processedLine = line.replace('\n', '').split(" ")
            
            opponentMove, myMove = processedLine
            myDecision = move[opponentMove + "&" + myMove]
            totalScore += calculateWin(opponentMove, myDecision)
            
    return totalScore

if __name__== "__main__":
    
    resultPart1 = part1("2022/input/day2.txt")
    print("Part1: ", resultPart1)
    
    resultPart2 = part2("2022/input/day2.txt")
    print("Part 2: ", resultPart2)