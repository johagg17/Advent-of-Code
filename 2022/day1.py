import os

def convertFileToList(path: str):
    elfList = []
    sumCalories = 0
    with open(path) as f:
        for line in f:
            if line == "\n":
                elfList.append(sumCalories)
                sumCalories = 0
                continue
            sumCalories += int(line.replace("\n", ""))
            
    elfList.sort(reverse=True)        
    return elfList

def Part1(finalList: list):
    return finalList[0]

def Part2(finalList: list):
    return sum(finalList[:3])

if __name__=="__main__":
    
    finalList = convertFileToList("2022/input/day1.txt")
    
    resultPart1 = Part1(finalList)
    print("Part1: ", resultPart1)

    resultPart2 = Part2(finalList)
    print("Part2: ", resultPart2)
    
    