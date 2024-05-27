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
        for k in range(2, n + 1):
            pnp1 = ((2 * k - 1) * x * pn - (k - 1) * pnm1) / k
            pnm1, pn = pn, pnp1
        return pn


def approximate_function(func, degree, a, b, nodes):
    def make_numerator_function(n):
        def numerator_function(x):
            x_scaled = (2 * x - a - b) / (b - a)  # scaling
            return func(x) * legendre_poly(n, x_scaled)

        return numerator_function

    def make_denominator_function(n):
        def denominator_function(x):
            x_scaled = (2 * x - a - b) / (b - a)  # scaling
            return legendre_poly(n, x_scaled) ** 2

        return denominator_function

    coeffs = []
    for k in range(degree + 1):
        func_numerator = make_numerator_function(k)
        func_denominator = make_denominator_function(k)

        numerator = gauss_legendre(func_numerator, a, b, nodes)
        denominator = gauss_legendre(func_denominator, a, b, nodes)

        # Debug print statements
        print(f"Degree {k}: Numerator = {numerator}, Denominator = {denominator}")

        if denominator == 0:
            print(f"Warning: Denominator is zero for degree {k}. Skipping this term.")
            ck = 0
        else:
            ck = numerator / denominator

        coeffs.append(ck)

    print("Coefficients:", coeffs)

    def approx_poly(x):
        x_scaled = (2 * x - a - b) / (b - a)
        return horner(coeffs, x_scaled)

    return approx_poly


def calculate_approximation_error(func, approx_func, a, b, n, norm='L2'):
    if norm == 'L2':
        def error_function(x):
            return (func(x) - approx_func(x)) ** 2

        error_integral = gauss_legendre(error_function, a, b, n)
        return math.sqrt(error_integral)

    elif norm == 'Chebyshev':
        def error_function(x):
            return np.abs(func(x) - approx_func(x))

        nodes, _ = np.polynomial.legendre.leggauss(n)
        nodes = 0.5 * (b - a) * nodes + 0.5 * (b + a)
        max_error = np.max(error_function(nodes))
        return max_error

    elif norm == 'L2_weighted':
        def error_function(x):
            return (func(x) - approx_func(x)) ** 2

        def weight_function(x):
            # przykładowa funkcja wagowa
            return 1 / (1 + x ** 2)

        def weighted_error_function(x):
            return weight_function(x) * error_function(x)

        error_integral = gauss_legendre(weighted_error_function, a, b, n)
        return math.sqrt(error_integral)

    else:
        raise ValueError("Unsupported norm type. Use 'L2', 'Chebyshev', or 'L2_weighted'.")


def graph(func, approx_func, a, b, error, degree, ax, norm="L2"):
    x_values = np.linspace(a, b, 300)
    original_values = [func(x) for x in x_values]
    approx_values = [approx_func(x) for x in x_values]

    ax.plot(x_values, original_values, label='Original Function')
    ax.plot(x_values, approx_values, label='Approximated Function', linestyle='--')
    ax.legend()
    ax.set_title("Function Approximation [degree: {}]".format(degree))
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)

    # Dodaj tekst z błędem aproksymacji
    ax.text(0.95, 0.01, 'Approximation Error ({}): {:.5f}'.format(norm, error),
            verticalalignment='bottom', horizontalalignment='right',
            transform=ax.transAxes,  # Wykorzystanie osi wykresu do pozycjonowania tekstu
            color='red', fontsize=12)


def f1(x):
    return x ** 2 - 2 * x + 1


def f2(x):
    return math.sin(x)


def f3(x):
    return math.exp(x)


def f4(x):
    return x ** 3 - 2 * x ** 2 + x - 5


def f5(x):
    return math.sin(x ** 2) + math.cos(x)


def f6(x):
    return math.exp(math.sin(x)) + math.exp(-x)


def create_function_from_user_input():
    user_input = input("Wprowadź swoją funkcję używając 'x' jako zmiennej (np. 'x**2 + sin(x)'): ")

    x = sp.symbols('x')

    try:
        user_expr = sp.sympify(user_input)
    except sp.SympifyError:
        print("Wystąpił błąd podczas parsowania wyrażenia.")
        return None

    def user_defined_function(x_value):
        return user_expr.subs(x, x_value)

    return user_defined_function

