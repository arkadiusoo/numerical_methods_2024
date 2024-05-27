import matplotlib.pyplot as plt
import numpy as np
import math
import sympy as sp

def horner(coeffs, x):
    result = 0
    for coeff in reversed(coeffs):
        result = result * x + coeff
    return result

def gauss_legendre(f, a, b, n):
    nodes, weights = np.polynomial.legendre.leggauss(n)

    integral = 0.0
    for i in range(n):
        x = 0.5 * (b - a) * nodes[i] + 0.5 * (b + a)
        integral += weights[i] * f(x)

    integral *= 0.5 * (b - a)
    return integral

def legendre_poly(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        pnm1, pn = 1, x
        for k in range(2, n+1):
            pnp1 = ((2*k-1)*x*pn - (k-1)*pnm1) / k
            pnm1, pn = pn, pnp1
        return pn

def approximate_function(func, degree, a, b, nodes):

    # local functions for numerator and denominator
    def make_numerator_function(n):
        def numerator_function(x):
            x_scaled = (2*x - a - b) / (b - a)  # scalling
            return func(x) * legendre_poly(n, x_scaled)
        return numerator_function

    def make_denominator_function(n):
        def denominator_function(x):
            x_scaled = (2*x - a - b) / (b - a)  # scalling
            return legendre_poly(n, x_scaled) ** 2
        return denominator_function

    coeffs = []
    for k in range(degree + 1):
        func_numerator = make_numerator_function(k)
        func_denominator = make_denominator_function(k)

        # Obliczenia całek przy użyciu kwadratur Gaussa-Legendre'a
        numerator = gauss_legendre(func_numerator, a, b, nodes)
        denominator = gauss_legendre(func_denominator, a, b, nodes)

        ck = numerator / denominator
        coeffs.append(ck)

    def approx_poly(x):
        x_scaled = (2*x - a - b) / (b - a)
        return horner(coeffs, x_scaled)

    return approx_poly


def calculate_approximation_error(func, approx_func, a, b, n): #RMSE (L2)
    def error_function(x):
        return (func(x) - approx_func(x)) ** 2

    error_integral = gauss_legendre(error_function, a, b, n)
    return math.sqrt(error_integral)


def graph(func, approx_func, a, b, error,degree):
    x_values = np.linspace(a, b, 300)
    original_values = [func(x) for x in x_values]
    approx_values = [approx_func(x) for x in x_values]

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, original_values, label='Original Function')
    plt.plot(x_values, approx_values, label='Approximated Function', linestyle='--')
    plt.legend()
    plt.title("Function Approximation [degree: {}]".format(degree))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)

    # Dodaj tekst z błędem aproksymacji
    plt.text(0.95, 0.01, 'Approximation Error (RMSE): {}'.format(error),
             verticalalignment='bottom', horizontalalignment='right',
             transform=plt.gca().transAxes,  # Wykorzystanie osi wykresu do pozycjonowania tekstu
             color='red', fontsize=12)

    plt.show()


def f1(x):
    # Prosta funkcja wielomianowa: x^2 - 2x + 1
    return x**2 - 2*x + 1
def f2(x):
    # Prosta funkcja trygonometryczna: sin(x)
    return math.sin(x)
def f3(x):
    # Prosta funkcja wykładnicza: e^x
    return math.exp(x)
def f4(x):
    # Bardziej skomplikowana funkcja wielomianowa: x^3 - 2x^2 + x - 5
    return x**3 - 2*x**2 + x - 5
def f5(x):
    # Skomplikowana funkcja trygonometryczna: sin(x^2) + cos(x)
    return math.sin(x**2) + math.cos(x)
def f6(x):
    # Skomplikowana funkcja wykładnicza: e^(sin(x)) + e^(-x)
    return math.exp(math.sin(x)) + math.exp(-x)

def create_function_from_user_input():
    # Pozwala użytkownikowi wpisać wyrażenie matematyczne
    user_input = input("Wprowadź swoją funkcję używając 'x' jako zmiennej (np. 'x**2 + sin(x)'): ")

    # Definiuje symbol x
    x = sp.symbols('x')

    # Próba parsowania wprowadzonego wyrażenia
    try:
        # Parse the input using sympy
        user_expr = sp.sympify(user_input)
    except sp.SympifyError:
        print("Wystąpił błąd podczas parsowania wyrażenia.")
        return None

    # Definicja funkcji Pythona
    def user_defined_function(x_value):
        # Wylicza wartość funkcji dla konkretnego x
        return user_expr.subs(x, x_value)

    return user_defined_function

