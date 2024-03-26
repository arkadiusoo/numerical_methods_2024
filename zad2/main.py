import myFunctions as mf

text0 = "\t\t***Witaj w programie do rozwiazywania rownan nieliniowych metoda Gaussa-Seidela***"
text1 = "Wybierz w metode w jaki sposob chcesz wprowadzic dane:\n\t1 - z pliku\n\t2 - recznie wprowadze\n\t3 - zakoncz program\nTwoj wybor: "
text2 = "Wybierz metode zakonczenia algorytmu:\n\t1 - iteracyjnie\n\t2 - dokladnosc\nTwoj wybor: "
text3 = "Niestety, nie jest to macierz diagonalna, sprobuje ją przeksztalcic.\n\n"

print(text0)
while True:
    wybor1 = input(text1)

    coefficients = []
    constants = []
    newX0 = []
    precisions = []
    counter = []
    flag = True



    match wybor1:
        case "1":
            coefficients, constants = mf.readDataFromFile("data.txt")
        case "2":
            coefficientsCount = int(input("Podaj zadana ilosc niewiadomych: "))
            for i in range(coefficientsCount):
                print("\t\tWiersz {}: ".format(i+1))
                temp = []
                for j in range(coefficientsCount):
                    value = float(input("Podaj wspolczynnik przy x^{}: ".format(coefficientsCount-j)))
                    temp.append(value)
                value2 = float(input("Podaj wspolczynnik przy x^{}: ".format(coefficientsCount-coefficientsCount)))
                coefficients.append(temp)
                constants.append(value2)
        case "3":
            break
        case _:
            raise Exception("Niepoprawny pierwszy wybor")

    equetionCounter = len(constants)
    x0 = [1] * equetionCounter
    gigaMatrix = mf.createMatrix(coefficients, constants)

    if mf.ifCatercornered(coefficients) == False:
        print(text3)
        temp = mf.makeItCatercornered(gigaMatrix)
        if temp != False:
            print("Udalo sie przeksztalcic podana macierz do macierzy diagonalnie dominujaca!")
            gigaMatrix = temp
        else:
            print("Nie udalo sie przeksztalcic podanej macierzy, ale i tak sprobujemy rozwiazac te rowania.")

    wybor2 = input(text2)

    match wybor2:
        case "1":
            iterations = int(input("Podaj ilsoc iteracji, po ktorych algorytm ma sie zatrzymac: "))
            newX0,precisions,counter = mf.iterativeGaussSeidelMethod(gigaMatrix, x0,iterations)

        case "2":
            precision = float(input("Podaj dokladnosc, po osiagnieciu ktorej algorytm ma sie zatrzymac: "))
            newX0, precisions, counter,flag = mf.precisionGaussSeidelMethod(gigaMatrix, x0, precision)
            if flag == False:
                print("Podany uklad rownan nie jest zbiezny, podany output jest ostatnia obliczona wartoscia.")
        case _:
            raise Exception("Niepoprawny drugi wybor")

    mowaKoncowa = "\n\n\t\t\tOUTPUT\n**Obliczone rozwiazania:\n\t{}\n**Dokladnosc dla kazdego rozwiazania:\n\t{}\n**Liczba iteracji:\n\t{}\n\n".format(newX0,precisions,counter)
    print(mowaKoncowa)
    print("**Macierz:")
    print(gigaMatrix)

print("\nMilego dnia!")

