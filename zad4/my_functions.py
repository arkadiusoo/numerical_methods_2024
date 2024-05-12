
def Simpson(f, a, b, eps):
    n = 2  # zaczynamy od dwoch przedzialow (musi byc parzysta ilosc)
    previous_result = None
    result = 0


    while previous_result is None or abs(result - previous_result) >= eps:
        previous_result = result
        h = (b - a) / n
        result = f(a) + f(b)

        # tutaj obliczamy sume wszystki wartosci punktow z odpowiednia logika
        for i in range(1, n):
            x = a + i * h
            if i % 2 == 0:
                result += 2 * f(x)
            else:
                result += 4 * f(x)

        result *= h / 3
        n *= 2  # podwajamy liczbe przedzialow dla nastepnej iteracji

    return result


