import math
from copy import deepcopy


def readDataFromFile(fileName):
    #this function returns two arrays,so you need to use this syntax: coefficients, constants = readDataFromFile(xyz)
    file = open(fileName, "r")
    file.readline() #skip first line of the file where is description
    coefficients = []
    constants = []
    for line in file.readlines():
        line = line.strip() #removes new line sign
        line = line.split() #crates array based on spaces between numbers
        line = [float(element) for element in line] #converts every element to float
        constants.append(line.pop())
        coefficients.append(line)
    return coefficients, constants

def createMatrix(coefficients, constants):
    rows = len(coefficients)
    columns = rows
    gigaMatrix = []
    for i in range(rows):
        divisior = coefficients[i][i]
        if divisior == 0:
            divisior = 1
        temp = []
        for j in range(columns):
            value = (coefficients[i][j] / divisior) * (-1.0)
            temp.append(value)
        temp[i] *= (-1.0)
        value2 = constants[i] / divisior
        temp.append(value2)
        gigaMatrix.append(temp)
    return gigaMatrix

def theJacobMethod(gigaMatrix,x0):
    unknownCount = len(gigaMatrix)

    newX0 = []
    for i in range(unknownCount):
        tempSum = 0

        for j in range(unknownCount):
            if i == j:
                None
            else:
                xi = x0[j]
                tempSum += (gigaMatrix[i][j] * xi)
        tempSum += gigaMatrix[i][unknownCount]

        newX0.append(tempSum)
    return newX0

def theGaussSeidelMethod(gigaMatrix, x0):
    unknownCount = len(gigaMatrix)

    newX0 = deepcopy(x0)
    for i in range(unknownCount):
        tempSum = 0
        for j in range(unknownCount):
            if i == j:
                None
            else:
                xi = newX0[j]
                tempSum += (gigaMatrix[i][j] * xi)
        tempSum += gigaMatrix[i][unknownCount]
        newX0[i] = tempSum
        # print("iteracja: {} | newX0 = {}".format(i+1, newX0))
    return newX0

def getPrecisions(oldX0, newX0):
    precisions = []
    for i in range(len(oldX0)):
        precisions.append(abs(newX0[i] - oldX0[i]))
    return precisions

def getAverage(array):
    return sum(array) / len(array)
def iterativeGaussSeidelMethod(gigaMatrix, x0, iterations):
    oldX0 = x0
    newX0 = theGaussSeidelMethod(gigaMatrix, x0)
    for i in range(iterations-1):
        oldX0 = deepcopy(newX0)
        newX0 = theGaussSeidelMethod(gigaMatrix, newX0)
    precisions = getPrecisions(oldX0, newX0)
    return newX0,precisions,iterations


def precisionGaussSeidelMethodL1Metric(gigaMatrix, x0, precision):
    oldX0 = deepcopy(x0)
    newX0 = theGaussSeidelMethod(gigaMatrix, x0)
    counter = 1
    oldPrecisionAverage = 0
    newPrecisionAverage = 0
    while getAverage(getPrecisions(oldX0,newX0)) > precision:
        counter += 1
        oldX0 = deepcopy(newX0)
        newX0 = theGaussSeidelMethod(gigaMatrix, newX0)

        oldPrecisionAverage = newPrecisionAverage
        newPrecisionAverage = getAverage(getPrecisions(oldX0,newX0))
        #zabezpieczenie przed wpadnieciem w petle nieskonczona
        if newPrecisionAverage > (oldPrecisionAverage) and oldPrecisionAverage != 0:
            return oldX0, oldPrecisionAverage, counter, False
    precisions = getPrecisions(oldX0, newX0)

    return newX0, newPrecisionAverage, counter, True

def getEuklidesPrecission(oldX0, newX0):
    sum = 0
    for i in range(len(oldX0)):
        sum += (oldX0[i] - newX0[i]) **2
    sum = math.sqrt(sum)
    return sum
def precisionGaussSeidelMethodEuklidesMetric(gigaMatrix, x0, precision):
    oldX0 = deepcopy(x0)
    newX0 = theGaussSeidelMethod(gigaMatrix, x0)
    counter = 1
    oldEuklidesPrecision = 0
    newEuklidesPrecision = 0
    while getEuklidesPrecission(oldX0,newX0) > precision:
        counter += 1
        oldX0 = deepcopy(newX0)
        newX0 = theGaussSeidelMethod(gigaMatrix, newX0)

        oldEuklidesPrecision = newEuklidesPrecision
        newEuklidesPrecision = getEuklidesPrecission(oldX0,newX0)
        #zabezpieczenie przed wpadnieciem w petle nieskonczona
        if newEuklidesPrecision > (oldEuklidesPrecision) and oldEuklidesPrecision != 0:
            # print(oldEuklidesPrecision, newEuklidesPrecision)
            return oldX0, getEuklidesPrecission(oldX0, newX0), counter, False
    precisions = getEuklidesPrecission(oldX0, newX0)

    return newX0, precisions, counter, True

def getManhattanPrecision(oldX0, newX0):
    sum = 0
    for i in range(len(oldX0)):
        sum += abs(oldX0[i] - newX0[i])
    return sum
def precisionGaussSeidelMethodManhattanMetric(gigaMatrix, x0, precision):
    oldX0 = deepcopy(x0)
    newX0 = theGaussSeidelMethod(gigaMatrix, x0)
    counter = 1
    oldManhattanPrecision = 0
    newManhattanPrecision = 0
    while getManhattanPrecision(oldX0,newX0) > precision:
        counter += 1
        oldX0 = deepcopy(newX0)
        newX0 = theGaussSeidelMethod(gigaMatrix, newX0)

        oldManhattanPrecision = newManhattanPrecision
        newManhattanPrecision = getManhattanPrecision(oldX0,newX0)
        # print(newManhattanPrecision)
        # print(oldManhattanPrecision)
        #zabezpieczenie przed wpadnieciem w petle nieskonczona
        if newManhattanPrecision > (oldManhattanPrecision) and oldManhattanPrecision != 0:
            # print(oldManhattanPrecision, newManhattanPrecision)
            return oldX0, getManhattanPrecision(oldX0, newX0), counter, False
    precisions = getManhattanPrecision(oldX0, newX0)

    return newX0, precisions, counter, True


def ifCatercornered(matrix):
    rows = len(matrix)
    for i in range(rows):
        diagonalValue = abs(matrix[i][i])
        sumOfRow = 0
        for i in matrix[i]:
            sumOfRow += abs(i)
        sumOfRow -= diagonalValue
        if diagonalValue < sumOfRow:
            return False
    return True

def makeItCatercornered(matrix):
    unknownCounter = len(matrix)
    newMatrix = [[]] * unknownCounter
    for i in range(unknownCounter):
        row = matrix[i]
        maxAbsValue = row[0]
        inexMaxAbsvalue = 0
        absSum = 0
        for j in range(unknownCounter):
            absValue = abs(row[j])
            if absValue > maxAbsValue:
                maxAbsValue = absValue
                inexMaxAbsvalue = j
            absSum += absValue
        absSum -= maxAbsValue

        if maxAbsValue > absSum:
            newMatrix[inexMaxAbsvalue] = row

    for row in newMatrix:
        if len(row) == 0:
            return False
    return newMatrix

# testowyMatrix = [[3,-1,2,40],[1,6,1,-1],[8,1,2,3],[2,1,18,2]]

# test = makeItCatercornered(testowyMatrix)
# print(test)


# coefficients, constants = readDataFromFile("data.txt")
# # print(ifCatercornered(coefficients))
# gigaMatrix = createMatrix(coefficients,constants)
# x0 = [1,1,1,1]
# newX0 = theGaussSeidelMethod(gigaMatrix, x0)
# print(newX0)
# for i in range(4):
#     newX0 = theGaussSeidelMethod(gigaMatrix, newX0)
#     print(newX0)
#
# print(iterativeGaussSeidelMethod(gigaMatrix, x0,2))
# print(precisionGaussSeidelMethodManhattanMetric(gigaMatrix, x0,0.0000000000001))