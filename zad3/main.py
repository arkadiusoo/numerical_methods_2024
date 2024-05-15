import my_functions as mf

text0 = "\t\t***Witaj w programie do interpolowania funkcji metoda Newtona***"
text1 = "Wybierz w metode w jaki sposob chcesz wprowadzic dane:\n\t1 - z pliku\n\t2 - recznie wprowadze\n\t3 - sprawko\n\t4 - zakoncz program\nTwoj wybor: "

print(text0)
while True:
    wybor1 = input(text1)



    match wybor1:
        case "1":
            node_amount, a,b,original_expr,x_value = mf.read_file("./funkcja.txt")
            nodes_x = mf.get_nodes(node_amount, a, b)
            nodes_y = mf.get_nodes_values(nodes_x, original_expr)
            difference_quotient = mf.difference_quotient(nodes_x, nodes_y)
            netwot_polynomial = mf.get_polynomial_newton_interpolation(nodes_x, nodes_y)
            converted_polynomial = mf.convert_polynomial(netwot_polynomial)
            coeffs = mf.get_coefficients(converted_polynomial)
            accuracy = mf.accuracy(nodes_x, nodes_y, x_value)
            y_value_4_x_value = mf.horner(coeffs, x_value)
            mowa_koncowa = "**********\nFunkcja interpolowana: {}\nWielomian interpolacyjny: {}\nPrzedzial: {}\nLiczba wezlow: {}\nWartosc obliczona za pomoca interpolacji dla punktu {}: {}\t o bledzie: {}\n\n".format(
                original_expr, converted_polynomial, [a, b], node_amount, x_value, y_value_4_x_value, accuracy,
                accuracy)
            print(mowa_koncowa)
            mf.plot_expression(original_expr, converted_polynomial, [a, b], nodes_x, nodes_y, x_value,
                               y_value_4_x_value)
        case "2":
            nodes_x = []
            nodes_y = []
            original_expr = ""
            x_value = 0
            node_amount = int(input("Podaj zadana ilosc wezlow: "))
            a = int(input("Podaj poczatek przedzialu: "))
            b = int(input("Podaj koniec przedzialu: "))
            original_expr = input("Podaj funkcje, ktora chcesz interpolowac: ")
            x_value = float(input("Podaj wartosc x, dla ktorego chcesz interpolowac: "))
            nodes_x = mf.get_nodes(node_amount, a, b)
            nodes_y = mf.get_nodes_values(nodes_x,original_expr)
            difference_quotient = mf.difference_quotient(nodes_x, nodes_y)
            netwot_polynomial = mf.get_polynomial_newton_interpolation(nodes_x, nodes_y)
            converted_polynomial = mf.convert_polynomial(netwot_polynomial)
            coeffs = mf.get_coefficients(converted_polynomial)
            accuracy = mf.accuracy(nodes_x, nodes_y, x_value)
            y_value_4_x_value = mf.horner(coeffs, x_value)
            mowa_koncowa = "**********\nFunkcja interpolowana: {}\nWielomian interpolacyjny: {}\nPrzedzial: {}\nLiczba wezlow: {}\nWartosc obliczona za pomoca interpolacji dla punktu {}: {}\t o bledzie: {}\n\n".format(original_expr,converted_polynomial,[a,b],node_amount,x_value,y_value_4_x_value,accuracy,accuracy)
            print(mowa_koncowa)
            mf.plot_expression(original_expr, converted_polynomial, [a,b],nodes_x, nodes_y,x_value,y_value_4_x_value)
        case '3':
                funkcje = ['sin(x)','cos(x)', 'Abs(x)', 'x+6', 'abs(sin(x))', '3*x**3+2*x+15']
                liczby_wezlow = [2,3,4]
                przedzial1 = [-3,4]
                przedzial2 = [-7,10]
                punkt1 = -1.2
                punkt2 = -4.7

                for funkcja in funkcje:
                    for l_w in liczby_wezlow:
                        # zestaw1
                        nodes_x1 = mf.get_nodes(l_w, przedzial1[0], przedzial1[1])
                        nodes_y1 = mf.get_nodes_values(nodes_x1,funkcja)
                        d_q1 = mf.difference_quotient(nodes_x1, nodes_y1)
                        n_t1 = mf.get_polynomial_newton_interpolation(nodes_x1, nodes_y1)
                        c_p1 = mf.convert_polynomial(n_t1)
                        coeffs1 = mf.get_coefficients(c_p1)
                        accuracy1 = mf.accuracy(nodes_x1, nodes_y1, punkt1)
                        punkt1_val = mf.horner(coeffs1, punkt1)
                        mowa_koncowa = "**********\nFunkcja interpolowana: {}\nWielomian interpolacyjny: {}\nPrzedzial: {}\nLiczba wezlow: {}\nWartosc obliczona za pomoca interpolacji dla punktu {}: {}\t o bledzie: {}\n\n".format(
                            funkcja, c_p1, przedzial1,l_w, punkt1, punkt1_val, accuracy1)
                        print(mowa_koncowa)
                        mf.plot_expression(funkcja,c_p1,przedzial1,nodes_x1,nodes_y1,punkt1,punkt1_val)

                        # zestaw2
                        nodes_x2 = mf.get_nodes(l_w, przedzial2[0], przedzial2[1])
                        nodes_y2 = mf.get_nodes_values(nodes_x2, funkcja)
                        nodes_x2 = mf.get_nodes(l_w, przedzial2[0], przedzial2[1])
                        nodes_y2 = mf.get_nodes_values(nodes_x2,funkcja)
                        d_q2 = mf.difference_quotient(nodes_x2, nodes_y2)
                        n_t2 = mf.get_polynomial_newton_interpolation(nodes_x2, nodes_y2)
                        c_p2 = mf.convert_polynomial(n_t2)
                        coeffs2 = mf.get_coefficients(c_p2)
                        accuracy2 = mf.accuracy(nodes_x2, nodes_y2, punkt2)
                        punkt2_val = mf.horner(coeffs2, punkt2)
                        mowa_koncowa = "**********\nFunkcja interpolowana: {}\nWielomian interpolacyjny: {}\nPrzedzial: {}\nLiczba wezlow: {}\nWartosc obliczona za pomoca interpolacji dla punktu {}: {}\t o bledzie: {}\n\n".format(
                            funkcja, c_p2, przedzial2,l_w, punkt2, punkt2_val, accuracy2)
                        print(mowa_koncowa)
                        mf.plot_expression(funkcja,c_p2,przedzial2,nodes_x2,nodes_y2,punkt2,punkt2_val)
                    temp = input("kliknij enter aby przejsc do nastepnej funkcji")


        case "4":
            break
        case _:
            raise Exception("Niepoprawny pierwszy wybor")





print("\nMilego dnia!")
