from sympy import symbols, expand, simplify, sympify, lambdify
import numpy as np
import matplotlib.pyplot as plt
import copy


def difference_quotient(nodes_x, nodes_y):
    if len(nodes_x) == 2:
        return (nodes_y[1] - nodes_y[0]) / (nodes_x[1] - nodes_x[0])
    else:
        divisor = nodes_x[-1] - nodes_x[0]
        return (difference_quotient(nodes_x[1:], nodes_y[1:]) - difference_quotient(nodes_x[:-1],
                                                                                    nodes_y[:-1])) / divisor


def get_polynomial_newton_interpolation(nodes_x, nodes_y):
    polynomial = "{}".format(nodes_y[0])
    last_index = len(nodes_x)
    border = 2
    while border <= last_index:
        d_q = difference_quotient(nodes_x[:border], nodes_y[:border])
        if d_q < 0:
            temp = "{}".format(d_q)
        else:
            temp = "+{}".format(d_q)
        i = 0
        while i < border - 1:
            if nodes_x[i] < 0:
                temp += "*(x+{})".format(nodes_x[i])
            else:
                temp += "*(x-{})".format(nodes_x[i])
            i += 1
        polynomial += temp
        border += 1
    return polynomial


def convert_polynomial(polynomial):
    x = symbols('x')
    polynomial_str = polynomial
    # converts string to sympy expression
    polynomial_expr = expand(polynomial_str)
    # simplifies expression
    simplified_expr = simplify(polynomial_expr)
    return simplified_expr


def get_coefficients(polynomial):
    # converts string polynomial to sympy polynomial expression
    new_polynomial = polynomial.as_poly()
    coeff = new_polynomial.all_coeffs()
    return coeff


def horner(coeffs, x):
    # coefficients starts from the highest power
    output = 0
    for i in range(len(coeffs)):
        output = output * x + coeffs[i]
    return output

def accuracy(nodes_x, nodes_y, x):
    output = difference_quotient(nodes_x, nodes_y)
    for element in nodes_x:
        output *= (x - element)
    return output

def plot_expression(original_expr_str, interpolated_expr_str, x_range):
    x = symbols('x')

    original_expr = sympify(original_expr_str)
    interpolated_expr = sympify(interpolated_expr_str)

    original_func = lambdify(x, original_expr, modules=['numpy'])
    interpolated_func = lambdify(x, interpolated_expr, modules=['numpy'])

    x_values = np.linspace(x_range[0], x_range[1], 400)

    original_y_values = original_func(x_values)
    interpolated_y_values = interpolated_func(x_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, original_y_values, label='oryginalna funkcja: ' + original_expr_str)
    plt.plot(x_values, interpolated_y_values, label='wielomian interpolacyjny: ' + interpolated_expr_str,
             linestyle='--')
    plt.title('Porównanie funkcji oryginalnej i interpolowanej')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()
