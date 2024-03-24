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

def precisionGaussSeidelMethod(gigaMatrix, x0, precision):
    print(x0)
    oldX0 = deepcopy(x0)
    newX0 = theGaussSeidelMethod(gigaMatrix, x0)
    print("old: {} \nnew: {}".format(oldX0, newX0))
    print(getPrecisions(oldX0,newX0))
    counter = 1
    while getAverage(getPrecisions(oldX0,newX0)) > precision:
        counter += 1
        oldX0 = deepcopy(newX0)
        newX0 = theGaussSeidelMethod(gigaMatrix, newX0)
    precisions = getPrecisions(oldX0,newX0)

    return newX0,precisions, counter

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


#
# coefficients, constants = readDataFromFile("data.txt")
# print(ifCatercornered(coefficients))
# gigaMatrix = createMatrix(coefficients,constants)
# x0 = [1,1,1,1]
# newX0 = theGaussSeidelMethod(gigaMatrix, x0)
# # print(newX0)
# # for i in range(4):
# #     newX0 = theGaussSeidelMethod(gigaMatrix, newX0)
# #     print(newX0)
#
# print(iterativeGaussSeidelMethod(gigaMatrix, x0,3))
# print(precisionGaussSeidelMethod(gigaMatrix, x0,0.0000000000001))