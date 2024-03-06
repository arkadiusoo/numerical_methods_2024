import math

collection = {
    "0" : ["3sin(2x)", ["sin", 3, 2, 0,0]], #trygonometryczna funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,
    "1" : ["(2^3x - 6) + 11", [2,3,-6,11]], #wykladnicza podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY
    "2" : ["x^3 - 2x - 2", [1,0,-2,-2]], #wielomian wspolczynnikPrzyX^3, wspolczynnikPrzyX^2, wspolczynnikPrzyX^1, wyrazWolny

}

def potegowanie (x,potega):
    wynik = 1
    for i in range(potega):
        wynik *=x
    return wynik
def rozwiazWielomioan (wspolczynniki, x):
    #wspolczynniki = [wspolczynnikPrzyX^3, wspolczynnikPrzyX^2, wspolczynnikPrzyX^1, wyrazWolny]
    wynik = 0
    for i in range(len(wspolczynniki)):
        wynik = wynik * x + wspolczynniki[i]
    return wynik
print(rozwiazWielomioan(collection["2"][1],4.7))
def rozwiazWykladnicze(wspolczynniki, x):
    #wspolczynniki = [podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY]
    return pow(wspolczynniki[0],((wspolczynniki[1] * x +  wspolczynniki[2]) ))+ wspolczynniki[3]
print(rozwiazWykladnicze(collection["1"][1],6.5))
def rozwiazTrygonometryczne(wspolczynniki, x ):
    #wspolczynniki = [funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,]
    if wspolczynniki[0] == "sin":
        return wspolczynniki[1]  * math.sin(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    elif wspolczynniki[0] == "cos":
        return wspolczynniki[1] * math.sin(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    elif wspolczynniki[0] == "tan":
        return wspolczynniki[1] * math.sin(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    else:
        return 5
print(rozwiazTrygonometryczne(collection["0"][1],2))
def rozwiazRownanie(iloscZlozen, kolejnoscFunkcji,x):

    if iloscZlozen == 0:
        funkcja1 = collection[kolejnoscFunkcji[0]][1]
        keyFunkcja1 = kolejnoscFunkcji[0][0]
        match (keyFunkcja1):
            case '0': #trygonometrycnza -
                return rozwiazTrygonometryczne(funkcja1,x)
            case '1':#wykladniczza -
                return rozwiazWykladnicze(funkcja1,x)
            case "2":#wielomian -
                return rozwiazWielomioan(funkcja1,x)
            case _:
                return 9999
    elif iloscZlozen == 1:
        funkcja1 = collection[kolejnoscFunkcji[0]][1]
        funkcja2 = collection[kolejnoscFunkcji[1]][1]
        keyFunkcja1 = kolejnoscFunkcji[0][0]
        keyFunkcja2 = kolejnoscFunkcji[1][0]
        print(funkcja1,funkcja2)
        match (keyFunkcja1):
            case '0':
                match (keyFunkcja2):
                    case '0':#trygonometryczna - trygonometryczna -
                        return rozwiazTrygonometryczne(funkcja1,rozwiazTrygonometryczne(funkcja2,x))
                    case '1':#trygonometryczna - wykladnicza -
                        return rozwiazTrygonometryczne(funkcja1,rozwiazWykladnicze(funkcja2, x))
                    case '2':#trygonometryczna - wielomian -
                        return rozwiazTrygonometryczne(funkcja1,rozwiazWielomioan(funkcja2, x))
                    case _:
                         return 9999

            case '1':
                match (keyFunkcja2):
                    case '0':#wykladnicza - trygonometryczna -
                        return rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1],
                                                       rozwiazTrygonometryczne(collection[kolejnoscFunkcji[0]][1], x))
                    case '1':#wykladnicza - wykladnicza -
                        return rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1],
                                                       rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1], x))
                    case '2':#wykladnicza - wielomian -
                        return rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1],
                                                       rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1], x))
                    case _:
                        return 9999
            case "2":
                match (keyFunkcja2):
                    case '0':#wielomian - trygonometryczna -
                        return rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1],
                                                  rozwiazTrygonometryczne(collection[kolejnoscFunkcji[0]][1], x))
                    case '1':#wielomian - wykladnicza -
                        return rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1],
                                                  rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1], x))
                    case '2':#wielomian - wielomian -
                        return rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1],
                                                  rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1], x))
                    case _:
                        return 9999
            case _:
                return 9999
    elif iloscZlozen == 2:
        funkcja1 = collection[kolejnoscFunkcji[0]][1]
        funkcja2 = collection[kolejnoscFunkcji[1]][1]
        funkcja3 = collection[kolejnoscFunkcji[2]][1]
        keyFunkcja1 = kolejnoscFunkcji[0][0]
        keyFunkcja2 = kolejnoscFunkcji[1][0]
        keyFunkcja3 = kolejnoscFunkcji[2][0]

        match (keyFunkcja1):
            case '0':
                match (keyFunkcja2):
                    case '0':
                        match (keyFunkcja3):
                            case '0':#trygonometryczna - trygonometryczna - trygonometryczna
                                return rozwiazTrygonometryczne(funkcja1, rozwiazTrygonometryczne(funkcja2, rozwiazTrygonometryczne(funkcja3, x)))
                            case '1':#trygonometryczna - trygonometryczna - wykladnicza
                                return rozwiazTrygonometryczne(funkcja1, rozwiazTrygonometryczne(funkcja2, rozwiazWykladnicze(funkcja3, x)))
                            case "2":#trygonometryczna - trygonometryczna - wielomian
                                return rozwiazTrygonometryczne(funkcja1, rozwiazTrygonometryczne(funkcja2, rozwiazWielomioan(funkcja3, x)))
                            case _:
                                return 9999

                    case '1':
                        match (keyFunkcja3):
                            case '0':#trygonometryczna - wykladnicza - trygonometryczna
                                return rozwiazTrygonometryczne(funkcja1, rozwiazWykladnicze(funkcja2, rozwiazTrygonometryczne(funkcja3, x)))
                            case '1':#trygonometryczna - wykladnicza - wykladnicze
                                return rozwiazTrygonometryczne(funkcja1, rozwiazWykladnicze(funkcja2, rozwiazWykladnicze(funkcja3, x)))
                            case "2":#trygonometryczna - wykladnicza - wielomian
                                return rozwiazTrygonometryczne(funkcja1, rozwiazWykladnicze(funkcja2, rozwiazWielomioan(funkcja3, x)))
                            case _:
                                return 9999

                    case '2':
                        match (keyFunkcja3):
                            case '0':#trygonometryczna - wielomian - trygonometryczna
                                return rozwiazTrygonometryczne(funkcja1, rozwiazWielomioan(funkcja2, rozwiazTrygonometryczne(funkcja3, x)))
                            case '1':#trygonometryczna - wielomian - wykladnicze
                                return rozwiazTrygonometryczne(funkcja1, rozwiazWielomioan(funkcja2, rozwiazWykladnicze(funkcja3, x)))
                            case "2":#trygonometryczna - wielomian - wielomian
                                return rozwiazTrygonometryczne(funkcja1, rozwiazWielomioan(funkcja2, rozwiazWielomioan(funkcja3, x)))
                            case _:
                                return 9999
                    case _:
                        return 9999

            case '1':
                match (keyFunkcja2):
                    case '0':
                        match (keyFunkcja3):
                            case '0':  # wykladnicza - trygonometryczna - trygonometryczna
                                return rozwiazWykladnicze(funkcja1, rozwiazTrygonometryczne(funkcja2,
                                                                                                 rozwiazTrygonometryczne(
                                                                                                     funkcja3, x)))
                            case '1':  # wykladnicza - trygonometryczna - wykladnicza
                                return rozwiazWykladnicze(funkcja1, rozwiazTrygonometryczne(funkcja2,
                                                                                                 rozwiazWykladnicze(
                                                                                                     funkcja3, x)))
                            case "2":  # wykladnicza - trygonometryczna - wielomian
                                return rozwiazWykladnicze(funkcja1, rozwiazTrygonometryczne(funkcja2,
                                                                                                 rozwiazWielomioan(
                                                                                                     funkcja3, x)))
                            case _:
                                return 9999

                    case '1':
                        match (keyFunkcja3):
                            case '0':  # wykladnicza - wykladnicza - trygonometryczna
                                return rozwiazWykladnicze(funkcja1, rozwiazWykladnicze(funkcja2,
                                                                                            rozwiazTrygonometryczne(
                                                                                                funkcja3, x)))
                            case '1':  # wykladnicza - wykladnicza - wykladnicze
                                return rozwiazWykladnicze(funkcja1, rozwiazWykladnicze(funkcja2,
                                                                                            rozwiazWykladnicze(funkcja3,
                                                                                                               x)))
                            case "2":  # wykladnicza - wykladnicza - wielomian
                                return rozwiazWykladnicze(funkcja1, rozwiazWykladnicze(funkcja2,
                                                                                            rozwiazWielomioan(funkcja3,
                                                                                                              x)))
                            case _:
                                return 9999

                    case '2':
                        match (keyFunkcja3):
                            case '0':  # wykladnicza - wielomian - trygonometryczna
                                return rozwiazWykladnicze(funkcja1, rozwiazWielomioan(funkcja2,
                                                                                           rozwiazTrygonometryczne(
                                                                                               funkcja3, x)))
                            case '1':  # wykladnicza - wielomian - wykladnicze
                                return rozwiazWykladnicze(funkcja1, rozwiazWielomioan(funkcja2,
                                                                                           rozwiazWykladnicze(funkcja3,
                                                                                                              x)))
                            case "2":  # wykladnicza - wielomian - wielomian
                                return rozwiazWykladnicze(funkcja1, rozwiazWielomioan(funkcja2,
                                                                                           rozwiazWielomioan(funkcja3,
                                                                                                             x)))
                            case _:
                                return 9999
                    case _:
                        return 9999
            case "2":
                match (keyFunkcja2):
                    case '0':
                        match (keyFunkcja3):
                            case '0':  # wielomian - trygonometryczna - trygonometryczna
                                return rozwiazWielomioan(funkcja1, rozwiazTrygonometryczne(funkcja2,
                                                                                            rozwiazTrygonometryczne(
                                                                                                funkcja3, x)))
                            case '1':  # wielomian - trygonometryczna - wykladnicza
                                return rozwiazWielomioan(funkcja1, rozwiazTrygonometryczne(funkcja2,
                                                                                            rozwiazWykladnicze(
                                                                                                funkcja3, x)))
                            case "2":  # wielomian - trygonometryczna - wielomian
                                return rozwiazWielomioan(funkcja1, rozwiazTrygonometryczne(funkcja2,
                                                                                            rozwiazWielomioan(
                                                                                                funkcja3, x)))
                            case _:
                                return 9999

                    case '1':
                        match (keyFunkcja3):
                            case '0':  # wielomian - wykladnicza - trygonometryczna
                                return rozwiazWielomioan(funkcja1, rozwiazWykladnicze(funkcja2,
                                                                                       rozwiazTrygonometryczne(
                                                                                           funkcja3, x)))
                            case '1':  # wielomian - wykladnicza - wykladnicze
                                return rozwiazWielomioan(funkcja1, rozwiazWykladnicze(funkcja2,
                                                                                       rozwiazWykladnicze(funkcja3,
                                                                                                          x)))
                            case "2":  # wielomian - wykladnicza - wielomian
                                return rozwiazWielomioan(funkcja1, rozwiazWykladnicze(funkcja2,
                                                                                       rozwiazWielomioan(funkcja3,
                                                                                                         x)))
                            case _:
                                return 9999

                    case '2':
                        match (keyFunkcja3):
                            case '0':  # wielomian - wielomian - trygonometryczna
                                return rozwiazWielomioan(funkcja1, rozwiazWielomioan(funkcja2,
                                                                                      rozwiazTrygonometryczne(
                                                                                          funkcja3, x)))
                            case '1':  # wielomian - wielomian - wykladnicze
                                return rozwiazWielomioan(funkcja1, rozwiazWielomioan(funkcja2,
                                                                                      rozwiazWykladnicze(funkcja3,
                                                                                                         x)))
                            case "2":  # wielomian - wielomian - wielomian
                                return rozwiazWielomioan(funkcja1, rozwiazWielomioan(funkcja2,
                                                                                      rozwiazWielomioan(funkcja3,
                                                                                                        x)))
                            case _:
                                return 9999
                    case _:
                        return 9999
            case _:
                return 9999

    return 0

print(rozwiazRownanie(1,["0","0"],4.7))
print(rozwiazRownanie(2,["0","2","0"],3))
print(rozwiazRownanie(0,["0"],3))
print(rozwiazRownanie(0,["2"],rozwiazRownanie(0,["0"],3)))
print(rozwiazRownanie(3, ["0","2","0"],rozwiazRownanie(0,["2"],rozwiazRownanie(0,["0"],3))))
def metodaBisekcjiDokladnosc (wspolczynniki, a, b, dokladnosc):

    while (abs(schematHornera(wspolczynniki, (a-b))) > dokladnosc):
        srodek = (a + b) / 2

        wartoscA = schematHornera(wspolczynniki, a)
        wartoscB = schematHornera(wspolczynniki, b)
        wartoscSrodka = schematHornera(wspolczynniki, srodek)

        if wartoscSrodka == 0:
            return srodek
        elif (wartoscA > 0 and wartoscSrodka < 0) or (wartoscA < 0 and wartoscSrodka > 0):
            b = srodek
        elif (wartoscB > 0 and wartoscSrodka < 0) or (wartoscB < 0 and wartoscSrodka > 0):
            a = srodek


def metodaBisekcjiIloscIteracji (wspolczynniki, a, b, iloscIteracji):
    licznik = 1
    while (licznik < iloscIteracji):
        srodek = (a + b) / 2

        wartoscA = schematHornera(wspolczynniki, a)
        wartoscB = schematHornera(wspolczynniki, b)
        wartoscSrodka = schematHornera(wspolczynniki, srodek)

        if wartoscSrodka == 0:
            return [srodek, licznik]
        elif (wartoscA > 0 and wartoscSrodka < 0) or (wartoscA < 0 and wartoscSrodka > 0):
            b = srodek
        elif (wartoscB > 0 and wartoscSrodka < 0) or (wartoscB < 0 and wartoscSrodka > 0):
            a = srodek
        licznik += 1




