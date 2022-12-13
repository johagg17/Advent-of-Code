

from collections import defaultdict

import sys

from functools import reduce


class Monkey():
    def __init__(self, monkeyId, startingItems, operation, 
                 divisbleBy, trueMonkey, 
                 falseMonkey) -> None:
        
        self.monkeyId = int(monkeyId)
        self.items = list(map(int, startingItems))
        self.operation = operation
        self.divisbleBy = int(divisbleBy)
        self.trueMonkey = int(trueMonkey)
        self.falseMonkey = int(falseMonkey)
        self.inspectCount = 0
        
    def inspectItems(self):
        while self.items:
            item = self.items.pop(0)
            self.inspectCount += 1
            old = item

            newValue = eval(self.operation) // 3
            
            if newValue % self.divisbleBy == 0:
                monkeys[self.trueMonkey].giveItem(newValue)
            else:
                monkeys[self.falseMonkey].giveItem(newValue)
               
    def inspectItemsPart2(self):
        import math
        
        while self.items:
            item = self.items.pop(0)
            self.inspectCount += 1
            old = item
             
            newValue = eval(self.operation) % 9699690
           # print(newValue)
            if newValue % self.divisbleBy == 0:
            #  print("Monkey list before: ",  monkeys[self.trueMonkey].items)
            # print("Throw to monkey: ", self.trueMonke
                monkeys[self.trueMonkey].giveItem(newValue)
            #  print("Monkey list after: ",  monkeys[self.trueMonkey].items)
            else:
            #  print("Monkey list before: ",  monkeys[self.falseMonkey].items)
            #print("Throw to monkey: ", self.falseMonke
                monkeys[self.falseMonkey].giveItem(newValue)
               # print("Monkey list after: ",  monkeys[self.falseMonkey].items)
            #print("New value:", newValue)
            
            
    def giveItem(self, item):
        self.items.append(item)        
        
    
    def __str__(self) -> str:
        return "MonkeyId: " + str(self.monkeyId) + ", items: " + str(self.items) + ", div: " + str(self.divisbleBy)
    
monkeys = defaultdict(Monkey)

def processMonkeys(path):
    with open(path) as f:
        for line in f:
            if line.startswith("Monkey"):
                _, monkeyId = line.replace(":", "").split(" ")
                items = f.readline().replace("  Starting items: ", "").replace("\n", "").split(", ")
                operation = f.readline().strip().split(": new = ")[1]
                divisibleBy = f.readline().strip().replace("Test: ", "").split(" ")[-1]
                trueMonkeyId = f.readline().strip().replace("If true: throw to monkey ", "")
                falseMonkeyId = f.readline().strip().replace("If false: throw to monkey ", "")
                monkey = Monkey(monkeyId, items, operation, divisibleBy, trueMonkeyId, falseMonkeyId)
                monkeys[monkey.monkeyId] = monkey
                

def part1():
    
    # Start the rounds.
    roundNumber = 0
    roundEndNumber = 20
    while roundNumber != roundEndNumber:
        
        for k, v in monkeys.items():
            currentMonkey = v
            currentMonkey.inspectItems()
            
        roundNumber += 1
    
    monkeyList = monkeys.values()
    
    sortedMonkeyList = sorted(monkeyList, key = lambda x: x.inspectCount, reverse=True)
    
    return sortedMonkeyList[0].inspectCount * sortedMonkeyList[1].inspectCount

def part2():
    
    # Start the rounds.
    roundNumber = 0
    roundEndNumber = 10000 
    while roundNumber != roundEndNumber:
        
        for k, v in monkeys.items():
            currentMonkey = v
            #print(currentMonkey)
            currentMonkey.inspectItemsPart2()
        
        roundNumber += 1
       # print("round: ", roundNumber)
    
    monkeyList = monkeys.values()
    
    sortedMonkeyList = sorted(monkeyList, key = lambda x: x.inspectCount, reverse=True)
    
    print(sortedMonkeyList[0].inspectCount, sortedMonkeyList[1].inspectCount)
    return sortedMonkeyList[0].inspectCount * sortedMonkeyList[1].inspectCount

if __name__ == "__main__":
    processMonkeys("2022/input/day11.txt")
    
    resPart1 = part1()
    print("Part1: ", resPart1)
    
    monkeys = defaultdict(Monkey)
    processMonkeys("2022/input/day11.txt")
    resPart2 = part2()
    print("Part2: ", resPart2)