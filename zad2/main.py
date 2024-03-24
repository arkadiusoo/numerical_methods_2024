import myFunctions as mf

flag = True

text0 = "\t\tWitaj w programie do rozwiazywania rownan nieliniowych metoda Gaussa-Seidela"
text1 = "\tWybierz w metode w jaki sposob chcesz wprowadzic dane:\n1 - z pliku\n2 - recznie wprowadze\n\tTwoj wybor: "
text2 = "\tWybierz motedo zakonczenia algorytmu:\n1 - iteracyjnie\n2 - dokladnosc\n\tTwoj wybor: "
text3 = "Nie jest to macierz diagonalna, wpisz poprawne wartosci."

print(text0)
while flag:
    wybor1 = input(text1)

    x0 = [1, 1, 1, 1]
    coefficients = []
    constants = []
    newX0 = []
    precisions = []
    counter = []



    match wybor1:
        case "1":
            coefficients, constants = mf.readDataFromFile("data.txt")
            if mf.ifCatercornered(coefficients) == False:
                print(text3)
                continue
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
            if mf.ifCatercornered(coefficients) == False:
                print(text3)
                continue
        case _:
            raise Exception("Niepoprawny pierwszy wybor")

    gigaMatrix = mf.createMatrix(coefficients, constants)
    wybor2 = input(text2)

    match wybor2:
        case "1":
            iterations = int(input("Podaj ilsoc iteracji, po ktorych algorytm ma sie zatrzymac: "))
            newX0,precisions,counter = mf.iterativeGaussSeidelMethod(gigaMatrix, x0,iterations)

        case "2":
            precision = float(input("Podaj dokladnosc, po osiagnieciu ktorej algorytm ma sie zatrzymac: "))
            newX0, precisions, counter = mf.precisionGaussSeidelMethod(gigaMatrix, x0, precision)
        case _:
            raise Exception("Niepoprawny drugi wybor")

    mowaKoncowa = "\tObliczone rozwiazania:\n{}\n\tDokladnosc dla kazdego rozwiazania:\n{}\n\tLiczba iteracji: {}\n".format(x0,precisions,counter)
    print(mowaKoncowa)



