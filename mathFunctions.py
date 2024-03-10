import math
collection = {
    "0" : ["3sin(2x)", ["sin", 3, 2, 0,0]], #trygonometryczna funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,
    "1" : ["(2^0.5x - 6) + 11", [2,3,-6,-11]], #wykladnicza podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY
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
    return (pow(wspolczynniki[0],(wspolczynniki[1] * x) + wspolczynniki[2])+ wspolczynniki[3])
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
    return srodek


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
    return [srodek, licznik]

# testTrygo = rozwiazTrygonometryczne(collection["0"][1],0)
#
# testRozwRow1=rozwiazRowanianie(["0"],0)
#
# testBisekcjaIt = metodaBisekcjiIloscIteracji(["0"],-100,100,1000)
# print("czysta trygo = {} | rozwiazRow = {} | bisekcjaIteracje = {}".format(testTrygo,testRozwRow1, testBisekcjaIt))
#
# testWyk = rozwiazWykladnicze(collection["1"][1], 3.153143872879099)
# testRozwRow2 = rozwiazRowanianie(["1"],3.153143872879099)
# testBisekcjaIt2 = metodaBisekcjiIloscIteracji(["1"],-100,100,1000)
# print("czysta wyk = {} | rozwiazRow = {} | bisekcjaIteracje = {}".format(testWyk,testRozwRow2,testBisekcjaIt2))
#
# testWielo = rozwiazWielomioan(collection["2"][1], 1.7692923542386314)
# testRozwRow3 = rozwiazRowanianie(["2"],1.7692923542386314)
# testBisekcjaIt3 = metodaBisekcjiIloscIteracji(["2"],-100,100,1000)
# print("czysta wielo = {} | rozwiazRow = {} | bisekcjaIteracje = ".format(testWielo,testRozwRow3),testBisekcjaIt3)

# miejsceZeroweRowanania3 = metodaBisekcjiIloscIteracji(["2"],-100,100,1000)[0]
# print(miejsceZeroweRowanania3)

# wielkiTest2 = metodaBisekcjiIloscIteracji(["0","1","2"],-100.0,100.0,1000)
# print(wielkiTest2)
z1 = rozwiazWielomioan(collection["2"][1],0.0)
z2 = rozwiazWykladnicze(collection["1"][1],z1)
z3 = rozwiazTrygonometryczne(collection["0"][1],z2)
print("z3 = {}".format(z3))
wielkiTest3 = metodaBisekcjiDokladnosc(["0","1","2"],-1.0,2.0,0.0001)
print("wielkiTest3 = {}".format(wielkiTest3))
# test = rozwiazWielomioan(collection["2"][1],100.0)
# print(test)
#1.681854248046875