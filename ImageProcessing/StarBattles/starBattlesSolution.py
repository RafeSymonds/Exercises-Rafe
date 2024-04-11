import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random
from collections import deque

def returnImage(fileName):
    return mpimg.imread(fileName)

def displayImage(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def saveImg(img, num):
    plt.imshow(img)
    plt.axis('off')
    plt.savefig("test" + str(num) + ".png")

def generateStarBattlesGrid():
    starLocations = []
    starValues = []    
    regions = np.zeros((10,10), dtype=np.int32)
    filledLocations = [deque() for i in range(20)]
    valid = False

    while(valid == False):
        
        starLocations = []
        starValues = []
        regions = np.zeros((10,10), dtype=np.int32)
        filledLocations = [deque() for _ in range(20)]
        generateStars(regions, filledLocations, starLocations, starValues)

        starLocations.sort(key=lambda position: (position[0],position[1]))

        

        preferences = generatePairs(regions, starLocations)

        startLocations = []
        endLocations = []
        index = 0
        while index < len(starLocations):
            if(starLocations[index] not in startLocations and starLocations[index] not in endLocations):
                startLocations.append(starLocations[index])
                endLocations.append(starLocations[preferences[index]])

            index += 1
        
        print(regions, '\n') 
        print(starLocations[:10])
        print(endLocations)
        valid = findMultipleValidPaths(regions, startLocations, endLocations)
           
    fillZeroRegions(regions)

    
    print(regions)

    tempImg = generateGridImage((regions, []))
    saveImg(tempImg, 1)


    solution = generateSolution(regions)
    print(solution)
    
    print('Is valid solution: ', validateSolution(regions, solution))

    return (regions, solution)

def generateStars(regions, filledLocations, starLocations, starValues):
    starRows = [0] * 10
    starColumns = [0] * 10
    starsLeft = 1

    while(starsLeft < 21):
        row = random.randrange(10)
        column = random.randrange(10)
        if(starRows[row] < 2 and starColumns[column] < 2 and not regions[row,column] != 0) :
            filledLocations[starsLeft-1].append((row,column))
            
            regions[row,column] = -starsLeft

            starLocations.append((row,column))
            starValues.append(-starsLeft)
            starRows[row] += 1
            starColumns[column] += 1
            starsLeft += 1
    


def generatePairs(regions, starLocations: list):
    preferences = [-1 for i in range(20)]
    freeStar = [True for i in range(20)]
    freeCount = 20

    distances = []
    for i in range(len(starLocations)):
        starDistances = []
        for j in range(len(starLocations)):
            if(i != j):
                starDistances.append((math.sqrt((starLocations[i][0] - starLocations[j][0])** 2 + (starLocations[i][1] - starLocations[j][1])** 2), j))
            else:
                starDistances.append((-1,-1))
        starDistances.sort(key = lambda x: x[0])
        distances.append(starDistances)

    while(True):
        star = 0
        while(star < len(starLocations)):
            if(freeStar[star] == True):
                break
            star += 1

        if(star == len(starLocations)):
            break
        preference = 1

        while(freeStar[star]):
            other = distances[star][preference][1]

            if(preferences != 0 and preferences[other] == -1):
                preferences[other] = star
                freeStar[other] = False
                preferences[star] = other
                freeStar[star] = False
                #freeCount -= 2
                break
            else:
                otherStar = preferences[other]

                otherStarDistance = 0
                for index in range(len(starLocations)):
                    if (distances[otherStar][index][1] == other):
                        otherStarDistance = distances[otherStar][index][0]
                        break

                starDistance = distances[star][preference][0]
                
                if(starDistance < otherStarDistance):
                    preferences[other] = star
                    
                    freeStar[star] = False
                    preferences[star] = other

                    preferences[otherStar] = -1
                    freeStar[otherStar] = True

                    #freeCount -= 1
                    break
            preference += 1
    return preferences

def isValidPosition(grid, y, x):
    return 0 <= x < len(grid) and 0 <= y < len(grid)

def findValidPath(grid, start, end, value_to_fill):
    
    visited = set()
    queue = deque()  # Queue of (position, path) tuples
    queue.append((start, []))
    
    while len(queue) > 0:
        
        current_pos, path = queue.popleft()
        
        if current_pos == end:
            # Fill the valid path with the given value
            for pos in path:
                grid[pos[0]][pos[1]] = int(value_to_fill)
            grid[end] = int(value_to_fill)
            return path + [end]  # Return the valid path
            
        if current_pos in visited:
            continue
        
        visited.add(current_pos)
        
        y,x  = current_pos
        neighbors = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
        for neighbor in neighbors:
            if isValidPosition(grid, *neighbor) and (grid[neighbor] == 0 or grid[neighbor] == grid[end]) :
                queue.append((neighbor, path + [current_pos]))
    
    return None  # No valid path found

def findMultipleValidPaths(grid, start_positions, end_positions):
    if len(start_positions) != len(end_positions):
        return None  # Unequal number of start and end positions

    valueToFill = 1
    for start, end in zip(start_positions, end_positions):
        valid_path = findValidPath(grid, start, end, valueToFill)
        
        if not valid_path:
            return False
        valueToFill += 1
    
    return True


def joinTwoSections(regions, reaplceValue, currentFilledRegion):
    regions[regions == reaplceValue] = currentFilledRegion

def fillZeroRegions(regions):
    noZeros = False
    while(not noZeros):
        noZeros = True
        for row in range(10):
            for column in range(10):
                if regions[row, column] == 0:
                    noZeros = False
                
                    positions = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
                    random.shuffle(positions)
                    for y1,x1 in positions:
                        if(0 <= y1 and 0 <= x1 and y1 < 10 and x1 < 10 and regions[y1,x1] != 0): 
                            regions[row,column] = int(regions[y1,x1])
                            break

def generateGridImage(gridAndSolution):
    gridRegions = gridAndSolution[0]
    solution = gridAndSolution[1]
    squareSize = 9
    lineSize = 1
    gridSize = 10 * squareSize + 11 * lineSize
    x = random.randrange(10 + gridSize, squareSize * 15)
    y = random.randrange(10 + gridSize, 10 * 15)
    print(y,x)
    
    startY = random.randrange(y - gridSize)
    startX = random.randrange(x - gridSize)
    
    print(startY, startX)

    endY = startY + gridSize + 1
    endX = startX + gridSize + 1
    
    print(endY, endX)

    grid = np.ones((y, x, 3), dtype=np.float32)
    print(grid.shape)

    
    for i in range(startY, endY):
        for j in range(startX, endX):
            if(i == startY or i == startY + gridSize or j == startX or j == startX + gridSize):
                grid[i,j] = [0,0,0]
            
    for row in range(10):
        for column in range(10):
            if(row < 9 and column < 10 and gridRegions[row,column] != gridRegions[row + 1, column]):
                for fillRow in range(1, squareSize + 2):
                    grid[startY + (row + 1) * 10, startX + column*10 + fillRow] = [0,0,0]
            if(row < 10 and column < 9 and gridRegions[row,column] != gridRegions[row, column + 1]):
                for fillRow in range(1, squareSize + 2):
                    grid[startY + row * 10 + fillRow, startX + (column + 1)*10] = [0,0,0]

    if(len(solution) > 0):
        for row in range(10):
            for column in range(10):
                if(solution[row,column] == 1):
                    grid[startY + row * 10 + 5, startX + column * 10 + 5] = [0,0,0]
                    grid[startY + row * 10 + 5 - 1, startX + column * 10 + 5] = [0,0,0]
                    grid[startY + row * 10 + 5 + 1, startX + column * 10 + 5] = [0,0,0]
                    grid[startY + row * 10 + 5, startX + column * 10 + 5 - 1] = [0,0,0]
                    grid[startY + row * 10 + 5, startX + column * 10 + 5 + 1] = [0,0,0]

    return grid
    
def generateSolution(regions):
    starLocations = np.zeros((10,10), dtype=np.int32)

    starCount = 0

    regionValues = dict()
    counter = 1
    for row in range(10):
        for column in range(10):
            if(regions[row,column] not in regionValues):
                regionValues[regions[row,column]] = counter
                counter += 1

    regionCounter = [0] * 11
    rowCounter = [0] * 10
    columnCounter = [0] * 10
    stack = deque()
    row = 0
    column = 0

    startColumn = 1

    backtrackingCount = 0

    while(starCount < 20):
        while(row < 10 and rowCounter[row] < 2):
            foundSpot = False
            while column < 10:
                regionValue = regionValues[regions[row,column]]
                if(starLocations[row,column] == 0 and regionCounter[regionValue] < 2 and columnCounter[column] < 2):
                    # chooose spot
                    setSpot(regions, starLocations, rowCounter, columnCounter, regionCounter, row, column, regionValue)
                    starCount += 1
                    stack.append((row,column))
                    
                    foundSpot = True
                    break
                column += 1
            # we hit a road block go back because we only have 1 in column
            if(not foundSpot):
                y,x = stack.pop()
                if(len(stack) == 0):
                    row = 0
                    column = startColumn
                    startColumn += 1
                    break
                regionValue = regionValues[regions[y,x]]
                unsetSpot(regions, starLocations, rowCounter, columnCounter, regionCounter, y, x, regionValue)
                backtrackingCount += 1
                
                starCount -= 1
                column = x + 1
                row = y

        if(len(stack) != 0):
            column = 0
            row += 1

    print(backtrackingCount)
    return starLocations

def setSpot(regions, starLocations, rowCounter, columnCounter, regionCounter, row, column, regionValue):
    starLocations[row,column] = 1
    rowCounter[row]+= 1
    columnCounter[column] += 1
    regionCounter[regionValue] += 1
    
def unsetSpot(regions, starLocations, rowCounter, columnCounter, regionCounter, row, column, regionValue):
    starLocations[row,column] = 0
    rowCounter[row]-= 1
    columnCounter[column] -= 1
    regionCounter[regionValue] -= 1

def validateSolution(regions, solution) -> bool:
    regionCounter = [0] * 11
    regionCounter[0] = 2
    rowCounter = [0] * 10
    columnCounter = [0] * 10
    regionValues = dict()
    counter = 1
    for row in range(10):
        for column in range(10):
            if(regions[row,column] not in regionValues):
                regionValues[regions[row,column]] = counter
                counter += 1
    
    for row in range(10):
        for column in range(10):
            if(solution[row,column] == 1):
                regionCounter[regionValues[regions[row,column]]] += 1
                rowCounter[row] += 1
                columnCounter[column] += 1

    for row in rowCounter:
        if(row != 2):
            return False
    for column in columnCounter:
        if(column != 2):
            return False
    for region in regionCounter:
        if(region != 2):
            return False
    return True


def generateRegionsFromImage(img):
    
    #displayImage(img)

    regions = np.zeros((10,10), dtype=np.int32)

    for row in range(10):
        for column in range(10):
            regions[row,column] = row * 10 + column + 1


    startRow = 0
    startColumn = 0
    

    while startRow < len(img):
        foundStart = False
        startColumn = 0
        while startColumn < len(img[0]):
            if(img[startRow,startColumn, 0] < 1):
                foundStart = True
                break
            startColumn += 1
        if(foundStart):
            break
        startRow += 1
    
    endColumn = startColumn
    while(endColumn < len(img[0])):
        if(img[startRow, endColumn, 0] == 1):
            break
        endColumn += 1 

    imageSize = endColumn - startColumn

    lineSize = 0
    while img[startRow + lineSize, startColumn + lineSize, 0] == 0:
        lineSize += 1


    print('Line size:', lineSize)
    squareSize = int((imageSize - lineSize * 11 + 1)/10)

    
    startRow += int(lineSize + squareSize / 2)



    print(startRow)
    print(img[startRow, startColumn])
    print(img[startRow+ 10, startColumn + 10, 0])

    for row in range(0,10):
        for column in range(1, 10):
            if(img[startRow + row * (squareSize + lineSize), startColumn + (squareSize + lineSize) * column, 0] != 1.0):
                continue
            line = False
            for distance in range(1,6):
                if(img[startRow + row * (squareSize + lineSize), startColumn + (squareSize + lineSize) * column - distance, 0] != 1.0 or img[startRow + row * (squareSize + lineSize), startColumn + (squareSize + lineSize) * column + distance, 0] != 1.0):
                    line = True
                    break
            if(not line):
                regions[row, column] = regions[row, column - 1]
                
    startRow -= int(lineSize + squareSize / 2)
    startColumn += int(lineSize + squareSize / 2)
    for column in range(0,10):
        for row in range(1, 10):
            if(img[startRow + row * (squareSize + lineSize), startColumn + (squareSize + lineSize) * column, 0] != 1.0):
                continue
            line = False
            for distance in range(1,6):
                if(img[startRow + row * (squareSize + lineSize) - distance, startColumn + (squareSize + lineSize) * column, 0] != 1.0 or img[startRow + row * (squareSize + lineSize) + distance, startColumn + (squareSize + lineSize) * column, 0] != 1.0):
                    line = True
                    break
            if(not line):
                joinTwoSections(regions, regions[row, column], regions[row - 1, column])
                #regions[row, column] = regions[row - 1, column]
    

    return regions

def solvePuzzle(fileName):

    img = returnImage(fileName)

    regions = generateRegionsFromImage(img)
    print(regions)
    solution = generateSolution(regions)
    print(solution)
    newImg = generateGridImage((regions,solution))

    displayImage(newImg)

# img = returnImage('testingFiles/Python/imageProcessing/example.png')

# plt.imshow(img)

# plt.show()

# img = generateGrid()
# print(img)
# displayImage(img)


# gridAndSolution = generateGrid()
# img = generateGridImage(gridAndSolution)
# saveImg(img, 2)

# solvePuzzle('ImageProcessing/StarBattles/TestCases/test4_input.png')