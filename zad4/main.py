import my_functions as mf
import os

text0 = "\t\t***Witaj w programie do interpolowania funkcji metoda Newtona***"
text1 = "Wybierz w metode w jaki sposob chcesz wprowadzic dane:\n\t1 - recznie wprowadze\n\t2 - sprawko\n\t3 - zakoncz program\nTwoj wybor: "
newtonText = "\n***Wynik całkowania \n\t- dla metody: Newtona-Cotesa \n\t- na przedziale: od {} do {}\n\t- z dokladnoscia: {}\n\t- z liczba podprzedzialow: {}\n wynosi: {}"
gaussText = "\n***Wynik całkowania \n\t- dla metody: Gaussa-Laguerre’a\n\t- na przedziale: od {} do {} \n\t- z liczba wezlow: {}\n wynosi: {}"

print(text0)
while True:
    wybor1 = input(text1)



    match wybor1:
        case "1":
            f = mf.create_function_from_user_input()
            if f == None:
                continue
            a = int(input("Podaj dolną granicę całkowania: "))
            b = int(input("Podaj górną granicę całkowania: "))
            initialNodes = int(input("Podaj początkową liczbę węzłów dla metody Newtona-Cotesa: "))
            tolerance = float(input("Podaj dokladnosc dla metody Newtona-Cotesa: "))
            nodes = int(input("Podaj liczbę węzłów dla metody Gaussa-Laguerre’a: "))
            newtonOutput, subintervals = mf.composite_simpson_with_precision(f, a, b, initialNodes, tolerance)
            gaussOutput, nodes2 = mf.gauss_legendre(f, a, b, nodes)
            print(newtonText.format(a,b,tolerance,subintervals,newtonOutput))
            print(gaussText.format(a,b,nodes,gaussOutput))
            print("\n\n")

        case "2":
            initialNodes = 1

            tolerance1 = 0.1
            tolerance2 = 0.0001

            a1 = 0
            b1 = 2

            a2 = -3
            b2 = 7

            nodes1 = 2
            nodes2 = 5

            print("\n***1 - newton***")
            print(newtonText.format(a1, b1, tolerance1, subintervals1, newtonOutput1))
            print("\n***2 - newton***")
            print(newtonText.format(a2, b2, tolerance2, subintervals2, newtonOutput2))
            print("\n***3 - newton***")
            print(newtonText.format(a1, b1, tolerance1, subintervals3, newtonOutput3))
            print("\n***4 - newton***")
            print(newtonText.format(a2, b2, tolerance2, subintervals4, newtonOutput4))
            print("\n***5 - newton***")
            print(newtonText.format(a1, b1, tolerance1, subintervals5, newtonOutput5))
            print("\n***6 - newton***")
            print(newtonText.format(a2, b2, tolerance2, subintervals6, newtonOutput6))
            print("\n***koniec - newton***\n\n")
            for i in range(2,6):
                nodes1 = i
                print("*************nodes {}".format(nodes1))
                newtonOutput1,subintervals1 = mf.composite_simpson_with_precision(mf.f1, a1, b1, 1, tolerance1)
                gaussOutput1, n = mf.gauss_legendre(mf.f1, a1, b1, nodes1)

                newtonOutput2,subintervals2 = mf.composite_simpson_with_precision(mf.f2, a2, b2, 1, tolerance2)
                gaussOutput2, n = mf.gauss_legendre(mf.f2, a2, b2, nodes1)

                newtonOutput3, subintervals3 = mf.composite_simpson_with_precision(mf.f3, a1, b1, 1, tolerance1)
                gaussOutput3, n = mf.gauss_legendre(mf.f3, a1, b1, nodes1)

                newtonOutput4, subintervals4 = mf.composite_simpson_with_precision(mf.f4, a2, b2, 1, tolerance2)
                gaussOutput4, n = mf.gauss_legendre(mf.f4, a2, b2, nodes1)

                newtonOutput5, subintervals5 = mf.composite_simpson_with_precision(mf.f5, a1, b1, 1, tolerance1)
                gaussOutput5, n = mf.gauss_legendre(mf.f5, a1, b1, nodes1)

                newtonOutput6, subintervals6 = mf.composite_simpson_with_precision(mf.f6, a2, b2, 1, tolerance2)
                gaussOutput6, n = mf.gauss_legendre(mf.f6, a2, b2, nodes1)

                print("\n***1 - gauss***")

                print(gaussText.format(a1,b1,nodes1,gaussOutput1))

                print("\n***2 - gauss***")

                print(gaussText.format(a2, b2, nodes1, gaussOutput2))

                print("\n***3 - gauss***")

                print(gaussText.format(a1, b1, nodes1, gaussOutput3))

                print("\n***4 - gauss***")

                print(gaussText.format(a2, b2, nodes1, gaussOutput4))

                print("\n***5 - gauss***")

                print(gaussText.format(a1, b1, nodes1, gaussOutput5))

                print("\n***6 - gauss***")

                print(gaussText.format(a2, b2, nodes1, gaussOutput6))

                print("\n***koniec - gauss***\n\n")

        case "3":
            break
        case _:
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")





print("\nMilego dnia!")
