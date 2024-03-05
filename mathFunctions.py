import math

collection = {
    "0" : ["3sin(2x)", ["sin", 3, 2, 0,0]], #[funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,]
    "1" : ["(2^3x-6)+11", [2,3,-6,11]], #podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY

}

def potegowanie (x,potega):
    wynik = 1
    for i in range(potega):
        wynik *=x
    return wynik
def rozwiazWielomioan (wspolczynniki, x):
    wynik = 0
    for i in range(len(wspolczynniki)):
        wynik = wynik * x + wspolczynniki[i]
    return wynik


def rozwiazWykladnicze(wspolczynniki, x):
    #wspolczynniki = [podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY]
    # return potegowanie(wspolczynniki[0],wspolczynniki[1] * x+ wspolczynniki[2]) + wspolczynniki[3]
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

def rozwiazRownanie(iloscZlozen, kolejnoscFunkcji):

    return 0

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




