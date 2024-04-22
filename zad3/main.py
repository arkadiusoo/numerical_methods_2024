import my_functions as mf

text0 = "\t\t***Witaj w programie do interpolowania funkcji metoda Newtona***"
text1 = "Wybierz w metode w jaki sposob chcesz wprowadzic dane:\n\t1 - z pliku\n\t2 - recznie wprowadze\n\t3 - zakoncz program\nTwoj wybor: "
text2 = "Wybierz metode zakonczenia algorytmu:\n\t1 - iteracyjnie\n\t2 - dokladnosc\n\t3 - pelen pakiet\n\t4 - tajna sciezka\nTwoj wybor: "
text3 = "Niestety, nie jest to macierz diagonalnie dominujaca, sprobuje ją przeksztalcic."

print(text0)
while True:
    wybor1 = input(text1)

    flag = True

    match wybor1:
        case "1":
            coefficients, constants = mf.readDataFromFile("data.txt")
        case "2":
            coefficientsCount = int(input("Podaj zadana ilosc niewiadomych: "))
            for i in range(coefficientsCount):
                print("\t\tWiersz {}: ".format(i + 1))
                temp = []
                for j in range(coefficientsCount):
                    value = float(input("Podaj wspolczynnik przy x^{}: ".format(coefficientsCount - j)))
                    temp.append(value)
                value2 = float(input("Podaj wspolczynnik przy x^{}: ".format(coefficientsCount - coefficientsCount)))
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
            newX0, precisions, counter = mf.iterativeGaussSeidelMethod(gigaMatrix, x0, iterations)
            if flag == False:
                mowaKoncowa1 = "\n\n\t\t\tOUTPUT\nPodany uklad rownan nie jest zbiezny, podany output jest ostatnia obliczona wartoscia\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}\n\n".format(
                    newX0, precisions, counter)
                print(mowaKoncowa1)
            else:
                mowaKoncowa2 = "\n\n\t\t\tOUTPUT\nObliczone rozwiazania:\n\t{}\nDokladnosc dla kazdego rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}\n\n".format(
                    newX0, precisions, counter)
                print(mowaKoncowa2)
            print("**Macierz:")
            print(gigaMatrix)

        case "2":
            precision = float(input("Podaj dokladnosc, po osiagnieciu ktorej algorytm ma sie zatrzymac: "))
            newX0, precisions, counter, flag = mf.precisionGaussSeidelMethodL1Metric(gigaMatrix, x0, precision)
            if flag == False:
                mowaKoncowa1 = "\n\n\t\t\tOUTPUT\nPodany uklad rownan nie jest zbiezny, podany output jest ostatnia obliczona wartoscia\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\n*iczba iteracji:\n\t{}\n\n".format(
                    newX0, precisions, counter)
                print(mowaKoncowa1)
            else:
                mowaKoncowa2 = "\n\n\t\t\tOUTPUT\nObliczone rozwiazania:\n\t{}\nDokladnosc dla kazdego rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}\n\n".format(
                    newX0, precisions, counter)
                print(mowaKoncowa2)
            print("**Macierz:")
            print(gigaMatrix)
        case "3":
            iterations = int(input("Podaj ilsoc iteracji, po ktorych algorytm ma sie zatrzymac: "))
            precision = float(input("Podaj dokladnosc, po osiagnieciu ktorej algorytm ma sie zatrzymac: "))

            # iteracje
            newX0, precisions, counter = mf.iterativeGaussSeidelMethod(gigaMatrix, x0, iterations)
            # precyzja metryka L1
            newX0L1, precisionsL1, counterL1, flagL1 = mf.precisionGaussSeidelMethodL1Metric(gigaMatrix, x0, precision)
            # precyzja metryka Euklidesowa
            newX0Euk, precisionsEuk, counterEuk, flagEuk = mf.precisionGaussSeidelMethodEuklidesMetric(gigaMatrix, x0,
                                                                                                       precision)
            # precyzja metryka Manhattan
            newX0Man, precisionsMan, counterMan, flagMan = mf.precisionGaussSeidelMethodManhattanMetric(gigaMatrix, x0,
                                                                                                        precision)
            print("\n\n\t\t\tOUTPUT")
            if flag == False:
                print("Podany uklad rownan nie jest zbiezny, podany output jest ostatnia obliczona wartoscia")
            print(
                "\t\tRozwiazanie dla iteracyjnej wersji:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0, precisions, counter))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka L1:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0L1, precisionsL1, counterL1))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka Euklidesowa:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0Euk, precisionsEuk, counterEuk))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka Manhattan:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}\n\n".format(
                    newX0Man, precisionsMan, counterMan))

        case "4":
            print("\n\n\t\t\tOUTPUT")
            # precyzja 0.1
            precision = 0.1
            print("Dokladnosc: {}".format(precision))
            # precyzja metryka L1
            newX0L1, precisionsL1, counterL1, flagL1 = mf.precisionGaussSeidelMethodL1Metric(gigaMatrix, x0, precision)
            # precyzja metryka Euklidesowa
            newX0Euk, precisionsEuk, counterEuk, flagEuk = mf.precisionGaussSeidelMethodEuklidesMetric(gigaMatrix, x0,
                                                                                                       precision)
            # precyzja metryka Manhattan
            newX0Man, precisionsMan, counterMan, flagMan = mf.precisionGaussSeidelMethodManhattanMetric(gigaMatrix, x0,
                                                                                                        precision)
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka L1:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0L1, precisionsL1, counterL1))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka Euklidesowa:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0Euk, precisionsEuk, counterEuk))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka Manhattan:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}\n\n".format(
                    newX0Man, precisionsMan, counterMan))
            print("************************************************************************************")

            # precyzja 0.01
            precision = 0.01
            print("Dokladnosc: {}".format(precision))
            # precyzja metryka L1
            newX0L1, precisionsL1, counterL1, flagL1 = mf.precisionGaussSeidelMethodL1Metric(gigaMatrix, x0, precision)
            # precyzja metryka Euklidesowa
            newX0Euk, precisionsEuk, counterEuk, flagEuk = mf.precisionGaussSeidelMethodEuklidesMetric(gigaMatrix, x0,
                                                                                                       precision)
            # precyzja metryka Manhattan
            newX0Man, precisionsMan, counterMan, flagMan = mf.precisionGaussSeidelMethodManhattanMetric(gigaMatrix, x0,
                                                                                                        precision)
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka L1:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0L1, precisionsL1, counterL1))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka Euklidesowa:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0Euk, precisionsEuk, counterEuk))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka Manhattan:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}\n\n".format(
                    newX0Man, precisionsMan, counterMan))
            print("************************************************************************************")

            # precyzja 0.0001
            precision = 0.0001
            print("Dokladnosc: {}".format(precision))
            # precyzja metryka L1
            newX0L1, precisionsL1, counterL1, flagL1 = mf.precisionGaussSeidelMethodL1Metric(gigaMatrix, x0, precision)
            # precyzja metryka Euklidesowa
            newX0Euk, precisionsEuk, counterEuk, flagEuk = mf.precisionGaussSeidelMethodEuklidesMetric(gigaMatrix, x0,
                                                                                                       precision)
            # precyzja metryka Manhattan
            newX0Man, precisionsMan, counterMan, flagMan = mf.precisionGaussSeidelMethodManhattanMetric(gigaMatrix, x0,
                                                                                                        precision)

            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka L1:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0L1, precisionsL1, counterL1))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka Euklidesowa:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0Euk, precisionsEuk, counterEuk))
            print(
                "\t\tRozwiazanie dla wersji z dokladnoscia z metryka Manhattan:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}\n\n".format(
                    newX0Man, precisionsMan, counterMan))
            print("************************************************************************************")

            # iteracje 1
            iterations = 1
            newX0, precisions, counter = mf.iterativeGaussSeidelMethod(gigaMatrix, x0, iterations)
            print(
                "\t\tRozwiazanie dla iteracyjnej wersji:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0, precisions, counter))

            # iteracje 5
            iterations = 5
            newX0, precisions, counter = mf.iterativeGaussSeidelMethod(gigaMatrix, x0, iterations)
            print(
                "\t\tRozwiazanie dla iteracyjnej wersji:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0, precisions, counter))

            # iteracje 10
            iterations = 10
            newX0, precisions, counter = mf.iterativeGaussSeidelMethod(gigaMatrix, x0, iterations)
            print(
                "\t\tRozwiazanie dla iteracyjnej wersji:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0, precisions, counter))

            # iteracje 15
            iterations = 15
            newX0, precisions, counter = mf.iterativeGaussSeidelMethod(gigaMatrix, x0, iterations)
            print(
                "\t\tRozwiazanie dla iteracyjnej wersji:\nObliczone rozwiazania:\n\t{}\nDokladnosc rozwiazania:\n\t{}\nLiczba iteracji:\n\t{}".format(
                    newX0, precisions, counter))

            if flag == False:
                print("Podany uklad rownan nie jest zbiezny, podany output jest ostatnia obliczona wartoscia")
            break

        case _:
            raise Exception("Niepoprawny drugi wybor")

print("\nMilego dnia!")
