import math
import sympy as sp

def calculate_simpson(function, a, b, number_of_subintervals):
    h = (b - a) / number_of_subintervals
    integral = function(a) + function(b)
    for i in range(1, number_of_subintervals):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * function(x_i)
        else:
            integral += 4 * function(x_i)
    integral *= h / 3
    return integral
def composite_simpson_with_precision(function, a, b, initial_subintervals, tolerance):
    number_of_subintervals = initial_subintervals
    if number_of_subintervals % 2 != 0:
        number_of_subintervals += 1  # number_of_subintervals must be even

    current_result = calculate_simpson(function, a, b, number_of_subintervals)
    while True:
        number_of_subintervals *= 2  # double number_of_subintervals
        new_result = calculate_simpson(function, a, b, number_of_subintervals)

        if abs(new_result - current_result) < tolerance:
            return new_result, number_of_subintervals
        current_result = new_result


def gauss_legendre(f, a, b, n):
    # Select nodes and weights based on the given n
    if n == 2:
        weights = [1.0, 1.0]
        nodes = [-0.5773502691896257, 0.5773502691896257]
    elif n == 3:
        weights = [0.5555555555555556, 0.8888888888888889, 0.5555555555555556]
        nodes = [-0.7745966692414834, 0.0, 0.7745966692414834]
    elif n == 4:
        weights = [0.3478548451374538, 0.6521451548625461, 0.6521451548625461, 0.3478548451374538]
        nodes = [-0.8611363115940526, -0.3399810435848563, 0.3399810435848563, 0.8611363115940526]
    elif n == 5:
        weights = [0.2369268850561891, 0.4786286704993665, 0.5688888888888889, 0.4786286704993665, 0.2369268850561891]
        nodes = [-0.9061798459386640, -0.5384693101056831, 0.0, 0.5384693101056831, 0.9061798459386640]
    else:
        return None

    integral = 0.0
    for i in range(n):
        x = 0.5 * (b - a) * nodes[i] + 0.5 * (b + a)
        integral += weights[i] * f(x)

    integral *= 0.5 * (b - a)
    return integral, n

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