import math
import random

bazaFunkcji = [
    ['tryg',"sin", 1, 1, 0,0,], # sin(x)
    ['wyk',1,2,1,1,+11], # 2^(x+1) + 11
    ['wielo',1,0,-2,-2] # x^3 - 2x - 2
]


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
    if len(kolejnoscFunkcji) != 1:
        kolejnoscFunkcji = list(reversed(kolejnoscFunkcji))
    wynik = 0
    for i in range(len(kolejnoscFunkcji)):
        funkcja = kolejnoscFunkcji[i][1:]
        keyFunkcja = kolejnoscFunkcji[i][0]

        if i != 0:
            match (keyFunkcja):
                case "tryg":  # trygonometrycnza -
                    wynik = rozwiazTrygonometryczne(funkcja, wynik)
                case "wyk":  # wykladniczza -
                    wynik = rozwiazWykladnicze(funkcja, wynik)
                case "wielo":  # wielomian -
                    wynik = rozwiazWielomioan(funkcja, wynik)
                case _:
                    return -9999
        else:
            match (keyFunkcja):
                case "tryg":  # trygonometrycnza -
                    wynik = rozwiazTrygonometryczne(funkcja, x)
                case "wyk":  # wykladniczza -
                    wynik = rozwiazWykladnicze(funkcja, x)
                case "wielo":  # wielomian -
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
        funkcja = kolejnoscFunkcji[i][1:]
        keyFunkcja = kolejnoscFunkcji[i][0]
        match (keyFunkcja):
            case "tryg":  # trygonometrycnza -
                pochodna = pochodnaTrygonometrycznej(funkcja)
                pochodna.insert(0,"tryg")
                kolejnoscPochodnych.append(pochodna)
            case "wyk":  # wykladniczza -
                pochodna = pochodnaWykladniczej(funkcja)
                pochodna.insert(0,"wyk")
                kolejnoscPochodnych.append(pochodna)
            case "wielo":  # wielomian -
                pochodna = pochodnaWielomian(funkcja)
                pochodna.insert(0,"wielo")
                kolejnoscPochodnych.append(pochodna)
            case _:
                return -9999
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
    print(kolejnoscFunkcji)
    for i in range(len(kolejnoscPochodnych)):
        pochodna = [kolejnoscPochodnych[i]]
        funkcje = kolejnoscFunkcji[i+1:]
        wartoscFunkcjiZlozonych = rozwiazRowanianie(funkcje,x)
        wartoscPochodnej = rozwiazRowanianie(pochodna,wartoscFunkcjiZlozonych)
        wartosc *= wartoscPochodnej
        text = "\t\ti = {}\npochodna = {} \t| wartosc pochodnej = {}\nfunkcje = {}\t| wartoscfucnkjiZlozonych = {}".format(i,pochodna,wartoscPochodnej,funkcje,wartoscFunkcjiZlozonych)
        print(text)
    return wartosc

# funkcje = bazaFunkcji
#
# pochodne = pochodnaZlozen(funkcje[2])
# print("funkcje: {}\npochodne: {}".format(funkcje,pochodne))
# test = obliczWartoscPochodnychZlozen(funkcje,pochodne,2)
# testb = rozwiazRowanianie(pochodne,1)
# print(testb)
# print(rozwiazRowanianie(pochodne,2.004))