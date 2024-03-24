

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

    newX0 = x0
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



coefficients, constants = readDataFromFile("data.txt")
gigaMatrix = createMatrix(coefficients,constants)
x0 = [1,1,1,1]
metodaJacoba = theJacobMethod(gigaMatrix,x0)
metodaGausa = theGaussSeidelMethod(gigaMatrix, x0)
print(metodaJacoba)
print(metodaGausa)
# for row in gigaMatrix:
#     print(row)

#
# print("wspolczynniki: " + str(coefficients))
# print("wyrazy wolne:" + str(constants))