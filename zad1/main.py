import mathFunctions as mf

flag = True

print("\t\t***Witaj w programie służącym do wynajdowania miejsca zerowego rownan nieliniowych***")
while flag:
    #pobieranie ilosci zlozen
    iloscZlozen = int(input("Podaj ilosc zlozen swojej funkcji: "))

    #pobieranie funkcji
    kolejnoscFunkcji = []
    for i in range(iloscZlozen+1):
        print("Funkcja nr {}".format(i+1))
        funkcja = mf.pobierzFunkcje()
        kolejnoscFunkcji.append(funkcja)

    #pobieranie przedzialu
    poczatekPrzedzialu = float(input("Podaj poczatek przedzialu, w ktorym szukamy miejsca zerowego: "))
    koniecPrzedzialu = float(input("Podaj koniec przedzialu, w ktorym szukamy miejsca zerowego: "))

    textWyborZatrzymania = "Wybierz w jaki sposob chcesz, aby algorytm sie zatrzymal:\n1 - za pomoca iteracji\n2 - za pomoca dokladnosci\n\tTwoj wybor:  "
    wyborZatrzymania = int(input(textWyborZatrzymania))

    match wyborZatrzymania:
        case 1:
            iloscIteracji = int(input("Podaj ilosc iteracji, po ktorych algorytm ma sie zatrzymac: "))
            bisekcjaIteracyjnie = mf.metodaBisekcjiIloscIteracji(kolejnoscFunkcji,poczatekPrzedzialu,koniecPrzedzialu,iloscIteracji) #[miejsceZerowe,jegoWartosc, liczbaIteracji]
            stycznejIteracje = mf.metodasStycznejIteracje(kolejnoscFunkcji,poczatekPrzedzialu,koniecPrzedzialu,iloscIteracji) #[miejsceZerowe,jegoWartosc, liczbaIteracji]
            mowaKoncowaBisekcja = ("\t\tMETODA BISEKCJI"
                           "\nDla podanej funkcji okreslonej na przedziale od {} do {}."
                           "\nZnaleziono miejsce zerowe w punkcie x = {}"
                           "\nPrzyblizona wartosc funkcji w tym punkcie wynosi {}"
                           "\nMetoda wykonala sie w {} iteracjach.".format(poczatekPrzedzialu,koniecPrzedzialu,bisekcjaIteracyjnie[0],bisekcjaIteracyjnie[1],bisekcjaIteracyjnie[2]))
            mowaKoncowaStycznych = ("\t\tMETODA STYCZNYCH"
                           "\nDla podanej funkcji okreslonej na przedziale od {} do {}."
                           "\nZnaleziono miejsce zerowe w punkcie x = {}"
                           "\nPrzyblizona wartosc funkcji w tym punkcie wynosi {}"
                           "\nMetoda wykonala sie w {} iteracjach.".format(poczatekPrzedzialu,koniecPrzedzialu,stycznejIteracje[0],stycznejIteracje[1],stycznejIteracje[2]))
            print("\tOUTPUT")
            print(mowaKoncowaBisekcja)
            print(mowaKoncowaStycznych)
            mf.wygenerujWykres(kolejnoscFunkcji,poczatekPrzedzialu,koniecPrzedzialu,bisekcjaIteracyjnie[0],stycznejIteracje[0])
        case 2:
            dokladnosc = float(input("Podaj dokladnosc, po osiagnieciu ktorej algorytm ma sie zatrzymac: "))
            bisekcjaDokladnosc = mf.metodaBisekcjiDokladnosc(kolejnoscFunkcji,poczatekPrzedzialu,koniecPrzedzialu,dokladnosc) #[miejsceZerowe,jegoWartosc]
            stycznejDokladnosc = mf.metodasStycznejDokladnosc(kolejnoscFunkcji,poczatekPrzedzialu,koniecPrzedzialu,dokladnosc) #[miejsceZerowe,jegoWartosc]

            mowaKoncowaBisekcja = ("\t\tMETODA BISEKCJI"
                           "\nDla podanej funkcji okreslonej na przedziale od {} do {}."
                           "\nZnaleziono miejsce zerowe w punkcie x = {}"
                           "\nPrzyblizona wartosc funkcji w tym punkcie wynosi {}"
                            "\nMetoda wykonala sie w {} iteracjach.".format(poczatekPrzedzialu,koniecPrzedzialu,bisekcjaDokladnosc[0],bisekcjaDokladnosc[1],bisekcjaDokladnosc[2]))
            mowaKoncowaStycznych = ("\t\tMETODA STYCZNYCH"
                           "\nDla podanej funkcji okreslonej na przedziale od {} do {}."
                           "\nZnaleziono miejsce zerowe w punkcie x = {}"
                           "\nPrzyblizona wartosc funkcji w tym punkcie wynosi {}"
                            "\nMetoda wykonala sie w {} iteracjach.".format(poczatekPrzedzialu,koniecPrzedzialu,stycznejDokladnosc[0],stycznejDokladnosc[1],stycznejDokladnosc[2]))
            print("\tOUTPUT")
            print(mowaKoncowaBisekcja)
            print(mowaKoncowaStycznych)
            mf.wygenerujWykres(kolejnoscFunkcji,poczatekPrzedzialu,koniecPrzedzialu,bisekcjaDokladnosc[0],stycznejDokladnosc[0])

        case _:
            raise Exception("Nieznany wybor")

    czyKontynuacja = int(input("Czy chcesz zakonczyc program?\n1 - tak\n2 - nie\n\tTwoj wybor: "))
    if czyKontynuacja !=2:
        flag = False





