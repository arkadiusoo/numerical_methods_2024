import numpy as np
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





def wielomian_Legendre(n, x):
    # iteracyjne wyliczenie wartosci wielomianu Legendre'a w punkcie x
    if n == 0:
        return 1
    elif n == 1:
        return x
    poprzednia_wartosc_minus_dwie_iteracje, poprzednia_wartosc = 1, x
    for k in range(2, n + 1):
        aktualna_wartosc = ((2 * k - 1) * x * poprzednia_wartosc - (k - 1) * poprzednia_wartosc_minus_dwie_iteracje) / k
        poprzednia_wartosc_minus_dwie_iteracje, poprzednia_wartosc = poprzednia_wartosc, aktualna_wartosc
    return poprzednia_wartosc


def pochodna_wielomianu_Legendre(n, x):
    # oblicza wartosc pochodnej n-tego wielomianu Legendre'a w punkcie x
    if n == 0:
        return 0
    return n / (x * x - 1) * (x * wielomian_Legendre(n, x) - wielomian_Legendre(n - 1, x))


def find_roots(n, tolerance=1e-10, max_iter=1000):
    """Znajdź miejsca zerowe n-tego wielomianu Legendre'a metodą Newtona."""
    roots = []
    initial_guesses = [np.cos(np.pi * (4 * k - 1) / (4 * n + 2)) for k in range(1, n + 1)]
    for x0 in initial_guesses:
        x = x0
        for _ in range(max_iter):
            fx = wielomian_Legendre(n, x)
            dfx = pochodna_wielomianu_Legendre(n, x)
            if abs(dfx) < tolerance:
                break
            x_new = x - fx / dfx
            if abs(x_new - x) < tolerance:
                roots.append(x_new)
                break
            x = x_new
    return roots


def gauss_legendre_quadrature(f, a, b, n):
    """Oblicz całkę funkcji f na przedziale [a, b] używając kwadratury Gaussa-Legendre'a."""
    nodes = find_roots(n)
    weights = [2 / ((1 - x ** 2) * (pochodna_wielomianu_Legendre(n, x) ** 2)) for x in nodes]

    adjusted_nodes = [0.5 * (x + 1) * (b - a) + a for x in nodes]
    adjusted_weights = [0.5 * w * (b - a) for w in weights]

    result = sum(adjusted_weights[i] * f(adjusted_nodes[i]) for i in range(n))
    return result


# Przykładowe użycie:
def example_function(x):
    return x ** 2  # Funkcja do całkowania, x^2


a = 0  # Dolna granica całkowania
b = 1  # Górna granica całkowania
n = 5  # Liczba punktów

integral_result = gauss_legendre_quadrature(example_function, a, b, n)
print("Wynik całkowania:", integral_result)
