import math

collection = {
    "0" : ["3sin(2x)", ["sin", 3, 2, 0,0]], #[funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,]
    "1" : ["(2^3x - 6) + 11", [2,3,-6,11]], #podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY
    "2" : ["x^3 - 2x - 2", [1,0,-2,-2]], #wspolczynnikPrzyX^3, wspolczynnikPrzyX^2, wspolczynnikPrzyX^1, wyrazWolny

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
    print(collection[kolejnoscFunkcji[0]][1])
    print(kolejnoscFunkcji[0])
    if iloscZlozen == 0:
        match (kolejnoscFunkcji[0][0]):
            case '0':
                return rozwiazTrygonometryczne(collection[kolejnoscFunkcji[0]][1],x)
            case '1':
                return rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1],x)
            case "2":
                return rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1],x)
            case _:
                return 9999
    elif iloscZlozen == 1:
        match (kolejnoscFunkcji[0][0]):
            case '0':
                match (kolejnoscFunkcji[1][0]):
                    case '0':
                        return rozwiazTrygonometryczne(collection[kolejnoscFunkcji[0]][1],rozwiazTrygonometryczne(collection[kolejnoscFunkcji[1]][1],x))
                    case '1':
                        return rozwiazTrygonometryczne(collection[kolejnoscFunkcji[0]][1],rozwiazWykladnicze(collection[kolejnoscFunkcji[1]][1], x))
                    case '2':
                        return rozwiazTrygonometryczne(collection[kolejnoscFunkcji[0]][1],rozwiazWielomioan(collection[kolejnoscFunkcji[1]][1], x))
                    case _:
                         return 9999

            case '1':
                match (kolejnoscFunkcji[1][0]):
                    case '0':
                        return rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1],
                                                       rozwiazTrygonometryczne(collection[kolejnoscFunkcji[0]][1], x))
                    case '1':
                        return rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1],
                                                       rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1], x))
                    case '2':
                        return rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1],
                                                       rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1], x))
                    case _:
                        return 9999
            case "2":
                match (kolejnoscFunkcji[1][0]):
                    case '0':
                        return rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1],
                                                  rozwiazTrygonometryczne(collection[kolejnoscFunkcji[0]][1], x))
                    case '1':
                        return rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1],
                                                  rozwiazWykladnicze(collection[kolejnoscFunkcji[0]][1], x))
                    case '2':
                        return rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1],
                                                  rozwiazWielomioan(collection[kolejnoscFunkcji[0]][1], x))
                    case _:
                        return 9999
            case _:
                return 9999

    return 0

print(rozwiazRownanie(1,["0","0"],4.7))
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




