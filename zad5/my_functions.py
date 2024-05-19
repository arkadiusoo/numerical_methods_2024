import matplotlib.pyplot as plt
import numpy as np
import math

def horner(coeffs, x):
    result = 0
    for coeff in reversed(coeffs):
        result = result * x + coeff
    return result

def gauss_legendre(f, a, b, n):
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

def graph(original,approx,a,b):
    x_values = np.linspace(a, b, 300)
    original_values = [original(x) for x in x_values]
    approx_values = [approx(x) for x in x_values]

    plt.plot(x_values, original_values, label='Original Function')
    plt.plot(x_values, approx_values, label='Approximated Function', linestyle='--')
    plt.legend()
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
