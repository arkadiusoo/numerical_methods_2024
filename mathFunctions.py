import math
from decimal import Decimal
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
# print(rozwiazWielomioan(collection["2"][1],4.7))
def rozwiazWykladnicze(wspolczynniki, x):
    #wspolczynniki = [podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY]
    # potega = (wspolczynniki[1] * x) + wspolczynniki[2]
    # wynik = pow(wspolczynniki[0],potega)
    # print(wynik)
    # wynik += wspolczynniki[3]
    # print(wynik)
    return (pow(wspolczynniki[0],(wspolczynniki[1] * x) + wspolczynniki[2])+ wspolczynniki[3])
# print(rozwiazWykladnicze(collection["1"][1],6.5))
def rozwiazTrygonometryczne(wspolczynniki, x ):
    #wspolczynniki = [funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,]
    if wspolczynniki[0] == "sin":
        a = wspolczynniki[2] * x + wspolczynniki[3]
        print(x)
        return wspolczynniki[1]  * math.sin(a) + wspolczynniki[4]
    elif wspolczynniki[0] == "cos":
        return wspolczynniki[1] * math.sin(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    elif wspolczynniki[0] == "tan":
        return wspolczynniki[1] * math.sin(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    else:
        return 5
# print(rozwiazTrygonometryczne(collection["0"][1],2))

def rozwiazRowanianie(kolejnoscFunkcji,x):
    kolejnoscFunkcji = list(reversed(kolejnoscFunkcji))
    wynik = 0
    for i in range(len(kolejnoscFunkcji)):

        funkcja = collection[kolejnoscFunkcji[i]][1]
        keyFunkcja = kolejnoscFunkcji[i][0]

        if i != 0:
            match (keyFunkcja):
                case '0':  # trygonometrycnza -
                    wynik = rozwiazTrygonometryczne(funkcja, wynik)
                case '1':  # wykladniczza -
                    wynik = rozwiazWykladnicze(funkcja, wynik)
                case "2":  # wielomian -
                    wynik = rozwiazWielomioan(funkcja, wynik)
                case _:
                    return -9999
        else:
            match (keyFunkcja):
                case '0':  # trygonometrycnza -
                    wynik = rozwiazTrygonometryczne(funkcja, x)
                case '1':  # wykladniczza -
                    wynik = rozwiazWykladnicze(funkcja, x)
                case "2":  # wielomian -
                    wynik = rozwiazWielomioan(funkcja, x)
                case _:
                    return -9999

    return wynik
# test = rozwiazRowanianie(["0","1","2"],2)
# print(test)


def metodaBisekcjiDokladnosc (wspolczynniki, a, b, dokladnosc):

    while (abs(rozwiazRowanianie(wspolczynniki, (a-b))) > dokladnosc):
        srodek = (a + b) / 2

        wartoscA = rozwiazRowanianie(wspolczynniki, a)
        wartoscB = rozwiazRowanianie(wspolczynniki, b)
        wartoscSrodka = rozwiazRowanianie(wspolczynniki, srodek)

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

        wartoscA = rozwiazRowanianie(wspolczynniki, a)
        wartoscB = rozwiazRowanianie(wspolczynniki, b)
        wartoscSrodka = rozwiazRowanianie(wspolczynniki, srodek)

        if wartoscSrodka == 0:
            return [srodek, licznik]
        elif (wartoscA > 0 and wartoscSrodka < 0) or (wartoscA < 0 and wartoscSrodka > 0):
            b = srodek
        elif (wartoscB > 0 and wartoscSrodka < 0) or (wartoscB < 0 and wartoscSrodka > 0):
            a = srodek
        licznik += 1


a = metodaBisekcjiIloscIteracji(["0","1","2"],0,100,100)
print(a)

trygTest = rozwiazTrygonometryczne("0",100)