
class Stack():
    def __init__(self, stackNumber, stackList: list) -> None:
        self.stackNumber = stackNumber
        self.stackList = stackList
        
    def add(self, create):
        self.stackList.append(create)
    
    def extend(self, list_: list):
        self.stackList.extend(list_)
        
    def pop(self):
        return self.stackList.pop()
    
    def peek(self):
        return self.stackList[-1]
    
    def __str__(self):
        return "stackNo: " + str(self.stackNumber) + ", list: " + str(self.stackList)
        
def moveCreatesPart1(stackDict: dict, line: str):

    _, createsToMove, _, stackToMoveFrom, _, stackToMoveTo  = line.split(" ")
    
    for i in range(int(createsToMove)):
        stackToRemoveFrom = stackDict[int(stackToMoveFrom)]
        stackToAddTo = stackDict[int(stackToMoveTo)]
        
        itemPoped = stackToRemoveFrom.pop()
        stackToAddTo.add(itemPoped)
    
def moveCreatesPart2(stackDict: dict, line: str):
    _, createsToMove, _, stackToMoveFrom, _, stackToMoveTo  = line.split(" ")
    stackToRemoveFrom = stackDict[int(stackToMoveFrom)]
    stackToAddTo = stackDict[int(stackToMoveTo)]
    
    list_ = []
    for i in range(int(createsToMove)):
        itemPoped = stackToRemoveFrom.pop()
        list_.append(itemPoped)
    list_.reverse()
    stackToAddTo.extend(list_)    
    
def part2():
    stacks = {}
    with open("2022/input/day5.txt") as f:
        for line in f:
            l = line.replace("\n", "")
            if l.split(" ")[0] == "move":
                moveCreatesPart2(stacks, l)
                continue
            
            stack = l.split(":")
            stackNo = int(stack[0])
            stackStartState = stack[1].split(", ")
            stackObj = Stack(stackNumber=stackNo, stackList=stackStartState)
            stacks[stackNo] = stackObj
    
    createsOnTop = []
    for key in stacks:
        createsOnTop.append(stacks[key].peek())
    return "".join(createsOnTop)
    
def part1():
    stacks = {}
    with open("2022/input/day5.txt") as f:
        for line in f:
            l = line.replace("\n", "")
            if l.split(" ")[0] == "move":
                moveCreatesPart1(stacks, l)
                continue
            
            stack = l.split(":")
            stackNo = int(stack[0])
            stackStartState = stack[1].split(", ")
            stackObj = Stack(stackNumber=stackNo, stackList=stackStartState)
            stacks[stackNo] = stackObj
    
    createsOnTop = []
    for key in stacks:
        createsOnTop.append(stacks[key].peek())
    return "".join(createsOnTop)

if __name__ == "__main__":
    resultPart1 = part1()
    print("Part1: ", resultPart1)
    
    resultPart2 = part2()
    print("Part2: ", resultPart2)