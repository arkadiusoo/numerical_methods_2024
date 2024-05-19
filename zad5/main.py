import my_functions as mf
import os
import time
text0 = "\t\t***Witaj w programie służącym do aproksymacji***"
text1 = "Wybierz w metode w jaki sposob chcesz wprowadzic dane:\n\t1 - recznie wprowadze\n\t2 - sprawko\n\t3 - zakoncz program\nTwoj wybor: "

def wait_for_plots():
    time.sleep(5)
print(text0)
while True:
    wybor1 = input(text1)



    match wybor1:
        case "1":
            f = mf.create_function_from_user_input()
            if f == None:
                continue
            a = int(input("Podaj poczatek przedziału aproksymacji: "))
            b = int(input("Podaj koniec przedziału aproksymacji: "))
            degree = int(input("Podaj żądany stopień wielomianu aproksymującego: "))
            nodes = int(input("Podaj liczbę węzłów potrzebną do całkowania: "))

            approx_func = mf.approximate_function(f,degree,a,b,nodes)
            error = mf.calculate_approximation_error(f,approx_func,a,b,nodes)
            mf.graph(f,approx_func,a,b,error,degree)

        case "2":
            a1 = 0
            b1 = 3

            a2 = -3
            b2 = 5

            nodes1 = 4

            print("\n\t***Funkcja f4")
            for i in range(3):
                approx_func = mf.approximate_function(mf.f4, i+1,a1,b1,nodes1)
                error = mf.calculate_approximation_error(mf.f4,approx_func,a1,b1,nodes1)
                print("Blad {}: {}".format(i+1,error))
                mf.graph(mf.f4,approx_func,a1,b1,error,i+1)

            wait_for_plots()

            print("\n\t***Funkcja f5")
            for i in range(3):
                approx_func = mf.approximate_function(mf.f5, i+1,a2,b2,nodes1)
                error = mf.calculate_approximation_error(mf.f5,approx_func,a2,b2,nodes1)
                print("Blad {}: {}".format(i+1,error))
                mf.graph(mf.f5,approx_func,a2,b2,error,i+1)

            wait_for_plots()
            print("\n\t***Funkcja f6")

            for i in range(3):
                approx_func = mf.approximate_function(mf.f6, i + 1, a2, b2, nodes1)
                error = mf.calculate_approximation_error(mf.f6, approx_func, a2, b2, nodes1)
                print("Blad {}: {}".format(i + 1, error))
                mf.graph(mf.f6, approx_func, a2, b2, error, i + 1)

        case "3":
            break
        case _:
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")





print("\nMilego dnia!")
