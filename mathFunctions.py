import math
import random
collection = {
    "0" : ["sin(x)", ["sin", 1, 1, 0,0]], #trygonometryczna funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,
    "1" : ["2^(x+1) + 11", [1,2,1,1,+11]], #wykladnicza wspolczynnik przy podstawie, podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY
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
def rozwiazWykladnicze(wspolczynniki, x):
    #wspolczynniki = [podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY]
    nowyX = x
    if wspolczynniki[2] == "x":
        wspolczynniki[2] = x
        nowyX = 1

    return wspolczynniki[0]*(pow(wspolczynniki[1],(wspolczynniki[2] * nowyX) + wspolczynniki[3])+ wspolczynniki[4])
def rozwiazTrygonometryczne(wspolczynniki, x ):
    #wspolczynniki = [funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,]

    if wspolczynniki[0] == "sin":
        return wspolczynniki[1]  * math.sin(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    elif wspolczynniki[0] == "cos":
        return wspolczynniki[1] * math.cos(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    elif wspolczynniki[0] == "tan":
        return wspolczynniki[1] * math.tan(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    else:
        return -9999

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

def metodaBisekcjiDokladnosc (wspolczynniki, a, b, dokladnosc):
    srodek = (a + b) / 2
    wartoscSrodka = 0
    while abs(rozwiazRowanianie(wspolczynniki, (a + b) / 2)) > dokladnosc:



        wartoscA = rozwiazRowanianie(wspolczynniki, a)
        wartoscB = rozwiazRowanianie(wspolczynniki, b)
        wartoscSrodka = rozwiazRowanianie(wspolczynniki, srodek)

        if wartoscSrodka == 0:
            return srodek
        elif (wartoscA > 0 and wartoscSrodka < 0) or (wartoscA < 0 and wartoscSrodka > 0):
            b = srodek
        elif (wartoscB > 0 and wartoscSrodka < 0) or (wartoscB < 0 and wartoscSrodka > 0):
            a = srodek
        srodek = (a + b) / 2
    return [srodek,wartoscSrodka]

def metodaBisekcjiIloscIteracji (wspolczynniki, a, b, iloscIteracji):
    licznik = 0
    srodek = (a + b) / 2

    while (licznik < iloscIteracji):
        licznik += 1

        wartoscA = rozwiazRowanianie(wspolczynniki, a)
        wartoscB = rozwiazRowanianie(wspolczynniki, b)
        wartoscSrodka = rozwiazRowanianie(wspolczynniki, srodek)

        if wartoscSrodka == 0:
            return [srodek, licznik]
        elif (wartoscA > 0 and wartoscSrodka < 0) or (wartoscA < 0 and wartoscSrodka > 0):
            b = srodek
        elif (wartoscB > 0 and wartoscSrodka < 0) or (wartoscB < 0 and wartoscSrodka > 0):
            a = srodek
        srodek = (a + b) / 2
    return [srodek, licznik]

def pochodnaWielomian(wspolczynniki):
    stopien = len(wspolczynniki) - 1
    noweWspolczynniki = []
    for i in range(stopien):
        noweWspolczynniki.append(wspolczynniki[i]*stopien)
        stopien -= 1
    return noweWspolczynniki

def pochodnaTrygonometrycznej(wspolczynniki):
    #wspolczynniki = [funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,]
    noweWspolczynniki = wspolczynniki
    if wspolczynniki[0] == "sin":
        noweWspolczynniki[0] = "cos"
        return noweWspolczynniki
    elif wspolczynniki[0] == "cos":
        noweWspolczynniki[0] = "sin"
        noweWspolczynniki[1] = wspolczynniki[1] * (-1)
        return noweWspolczynniki
    elif wspolczynniki[0] == "tan":
        noweWspolczynniki[0] = "sin/cos"
        return noweWspolczynniki
    else:
        return -9999

def pochodnaWykladniczej(wspolczynniki):
    noweWspolczynniki = []
    noweWspolczynniki.append(math.log(wspolczynniki[1]))
    noweWspolczynniki.append(wspolczynniki[1])
    noweWspolczynniki.append("x")
    noweWspolczynniki.append(wspolczynniki[3])
    noweWspolczynniki.append(0)
    return noweWspolczynniki

def getRandom():
    output = str(math.floor(random.random()*1000))
    return output
def pochodnaZlozen(kolejnoscFunkcji):
    pochodneFunkcji = []
    kolejnoscPochodnych = []
    for i in range(len(kolejnoscFunkcji)):
        funkcja = collection[kolejnoscFunkcji[i]][1]
        keyFunkcja = kolejnoscFunkcji[i][0]
        match (keyFunkcja):
            case '0':  # trygonometrycnza -
                key = '0' + getRandom()
                kolejnoscPochodnych.append(key)
                collection[key] = [0,pochodnaTrygonometrycznej(funkcja)]
            case '1':  # wykladniczza -
                key = '1' + getRandom()
                kolejnoscPochodnych.append(key)
                collection[key] = [0,pochodnaWykladniczej(funkcja)]
            case "2":  # wielomian -
                key = '2' + getRandom()
                kolejnoscPochodnych.append(key)
                collection[key] = [0,pochodnaWielomian(funkcja)]
            case _:
                return -9999
    print(kolejnoscPochodnych)
    return kolejnoscPochodnych
# test = pochodnaZlozen(['0','1','2'])
# a = [1,2,3]
# print(a[1:])
# fun = ['d','g','f']
# poch = ['dp','gp','fp']
#
# for i in range(len(poch)):
#     print(poch[i])
#     print(fun[i+1:])

def obliczWartoscPochodnychZlozen(kolejnoscFunkcji,kolejnoscPochodnych,x):
    wartosc = 1
    for i in range(len(kolejnoscPochodnych)):
        pochodna = kolejnoscPochodnych[i]
        funkcje = kolejnoscFunkcji[i+1:]
        wartoscFunkcjiZlozonych = rozwiazRowanianie(funkcje,x)
        wartoscPochodnej = rozwiazRowanianie(pochodna,wartoscFunkcjiZlozonych)
        wartosc *= wartoscPochodnej
    print(wartosc)



