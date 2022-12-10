
from collections import defaultdict

class Tree():
    def __init__(self, row, col, height) -> None:
        self.row = row
        self.col = col
        self.height = height
    
    def setRowNeigh(self, neigh):
        pass
        
        
trees = defaultdict(int)

def isOnEdge(row, col, maxRow, maxCol):
    
    if (row == 0 or row == maxRow):
        return True
    if col == 0 or col == maxCol:
        return True
    return False
        
        
    
def part1(path: str):
    with open(path) as f:
        
        grid = []
        for row1, line in enumerate(f):
            l = line.replace("\n", "")
            currentRow = []
            for col1, treeH in enumerate(l):
                currentRow.append(int(treeH))
                #trees[(row, col)] = int(treeH)
            grid.append(currentRow)
    #print(grid)
    #print(grid[:1 ][1])
    #return
    import numpy as np
    grid = np.array(grid)
    maxRow = row1
    maxCol = col1
    numberOfVisTrees = 0
    for row, v1 in enumerate(grid):
        for col, v2 in enumerate(v1):
            if isOnEdge(row, col, maxRow, maxCol):
                numberOfVisTrees += 1
                continue
            isVisibleLeft = True
            isVisibleRight = True
            isVisDown = True
            isVisUp = True
            # Check left
            for x in grid[row, :col]:
                if x >= v2:
                    isVisibleLeft = False
                    break
                    
            
            # Check right
            for xx in grid[row, 1 + col:]:
                if xx >= v2:
                    isVisibleRight = False
                    break
            
            # Check up
            for xxx in grid[:row, col]:
                if xxx >= v2:
                    isVisUp = False
                    break
            
            # Check down    
            for idx, xxxx in enumerate(grid[1 + row:, col]):
                #print("comparing: ", v2, xxxx)
                if xxxx >= v2:
                    isVisDown = False
                    break
            
            if isVisibleLeft or isVisibleRight or isVisUp or isVisDown:
                numberOfVisTrees += 1
            
    return numberOfVisTrees

def part2(path: str):
    with open(path) as f:
        
        grid = []
        for row1, line in enumerate(f):
            l = line.replace("\n", "")
            currentRow = []
            for col1, treeH in enumerate(l):
                currentRow.append(int(treeH))
            grid.append(currentRow)

    import numpy as np
    grid = np.array(grid)
    maxRow = row1
    maxCol = col1
    numberOfVisTrees = 0
    bestScore = 0
    for row, v1 in enumerate(grid):
        for col, v2 in enumerate(v1):
            currentViewingDistanceL = 0
            currentViewingDistanceR = 0
            currentViewingDistanceU = 0
            currentViewingDistanceD = 0
            
            if isOnEdge(row, col, maxRow, maxCol):
                numberOfVisTrees += 1
                continue
            
            for x in reversed(grid[row, :col]):
                if x >= v2:
                    currentViewingDistanceL += 1
                    break
                currentViewingDistanceL += 1
            
            for xx in grid[row, 1 + col:]:
                if xx >= v2:
                    currentViewingDistanceR += 1
                    break
                currentViewingDistanceR += 1

            for xxx in reversed(grid[:row, col]):
                if xxx >= v2:
                    currentViewingDistanceU += 1
                    break
                currentViewingDistanceU += 1

            for idx, xxxx in enumerate(grid[1 + row:, col]):
                if xxxx >= v2:
                    currentViewingDistanceD += 1
                    break
                currentViewingDistanceD += 1
            
            viewingScore = currentViewingDistanceL * currentViewingDistanceR * currentViewingDistanceU * currentViewingDistanceD
            if viewingScore > bestScore:
                bestScore = viewingScore
                
    return bestScore
if __name__=="__main__":
    resPart1 = part1("2022/input/day8sample.txt")
    print("Res part1:", resPart1)
    
    resPart2 = part2("2022/input/day8.txt")
    print("Res part2:", resPart2)