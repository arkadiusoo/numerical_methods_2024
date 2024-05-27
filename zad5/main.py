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
            nodes = int(input("Podaj liczbę węzłów potrzebną do całkowania: "))
            wybor2 = input("Jezeli chcesz wpisac dokladnosc - napisz liczbe jako float,\njezeli stopien wielomianu aproksymacji - napisz liczbe jako int\n\twartosc: ")
            if "." in wybor2:
                accuracy = float(wybor2)
                degree = 1
                approx_func = mf.approximate_function(f, degree, a, b, nodes)
                error = mf.calculate_approximation_error(f, approx_func, a, b, nodes)
                while error > accuracy:
                    degree += 1
                    approx_func = mf.approximate_function(f, degree, a, b, nodes)
                    error = mf.calculate_approximation_error(f, approx_func, a, b, nodes)
                    if degree == 100:
                        raise ValueError("Przesadziles!")

                mf.graph(f, approx_func, a, b, error, degree)

            else:
                degree = int(wybor2)
                approx_func = mf.approximate_function(f,degree,a,b,nodes)
                error = mf.calculate_approximation_error(f,approx_func,a,b,nodes)
                mf.graph(f,approx_func,a,b,error,degree)

        case "2":

            a1 = 0
            b1 = 3

            a2 = -3
            b2 = 5
            norms = ["L2", "Chebyshev", "L2_weighted"]
            nodes = [3,6,9]
            for i in range(3):
                nodes1 = nodes[i]
                norm = norms[i]
                print("\n\t***Funkcja f4")
                fig, axes = mf.plt.subplots(2, 2, figsize=(14, 10))
                axes = axes.flatten()

                for i in range(4):
                    approx_func = mf.approximate_function(mf.f4, i+1,a1,b1,nodes1)
                    error = mf.calculate_approximation_error(mf.f4,approx_func,a1,b1,nodes1, norm)
                    print("Blad {}: {}".format(i+1,error))
                    mf.graph(mf.f4,approx_func,a1,b1,error,i+1,axes[i], norm)
                mf.plt.tight_layout()
                mf.plt.savefig("./plots/func4_plot_with_{}_nodes_with_norm_{}.png".format(nodes1,norm))
                mf.plt.show()

                wait_for_plots()

                print("\n\t***Funkcja f5")
                fig, axes = mf.plt.subplots(2, 2, figsize=(14, 10))
                axes = axes.flatten()
                for i in range(4):
                    approx_func = mf.approximate_function(mf.f5, i+1,a2,b2,nodes1)
                    error = mf.calculate_approximation_error(mf.f5,approx_func,a2,b2,nodes1,norm)
                    print("Blad {}: {}".format(i+1,error))
                    mf.graph(mf.f5,approx_func,a2,b2,error,i+1,axes[i], norm)
                mf.plt.tight_layout()
                mf.plt.savefig("./plots/func5_plot_with_{}_nodes_with_norm_{}.png".format(nodes1,norm))
                mf.plt.show()
                wait_for_plots()

                print("\n\t***Funkcja f6")
                fig, axes = mf.plt.subplots(2, 2, figsize=(14, 10))
                axes = axes.flatten()

                for i in range(4):
                    approx_func = mf.approximate_function(mf.f6, i + 1, a2, b2, nodes1)
                    error = mf.calculate_approximation_error(mf.f6, approx_func, a2, b2, nodes1, norm)
                    print("Blad {}: {}".format(i + 1, error))
                    mf.graph(mf.f6, approx_func, a2, b2, error, i + 1,axes[i], norm)
                mf.plt.tight_layout()
                mf.plt.savefig("./plots/func6_plot_with_{}_nodes_with_norm_{}.png".format(nodes1,norm))
                mf.plt.show()
        case "3":
            break
        case _:
            if os.name == 'nt':
                os.system("cls")
            else:
                os.system("clear")

print("\nMilego dnia!")
