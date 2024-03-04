def schematHornera (wspolczynniki, stopien, x):
    wynik = wspolczynniki[0]

    for wspolczynnik in wspolczynniki[1:]:
        wynik = wynik*x + wspolczynnik[wspolczynniki.index()]

    return wynik


