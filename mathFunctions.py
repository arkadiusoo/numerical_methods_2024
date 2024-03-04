def schematHornera (wspolczynniki, x):

    wynik = 0

    for i in range(len(wspolczynniki)):
        wynik = wynik * x + wspolczynniki[i]
    return wynik


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

print(metodaBisekcjiDokladnosc([2,0,-1,-5],0, 100, 0.1))
print(metodaBisekcjiIloscIteracji([2,0,-1,-5],0, 100, 100))


