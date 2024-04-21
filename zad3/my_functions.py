from sympy import symbols, expand, simplify
def difference_quotient(nodes_x, nodes_y):
    if len(nodes_x) == 2:
        return (nodes_y[1] - nodes_y[0]) / (nodes_x[1] - nodes_x[0])
    else:
        divisor = nodes_x[-1] - nodes_x[0]
        return (difference_quotient(nodes_x[1:], nodes_y[1:]) - difference_quotient(nodes_x[:-1], nodes_y[:-1])) / divisor

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
        while i < border -1:
            if nodes_x[i] < 0:
                temp += "*(x+{})".format(nodes_x[i])
            else:
                temp += "*(x-{})".format(nodes_x[i])
            i+=1
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

def horner (coeffs, x):
    # coefficients starts from the highest power
    output = 0
    for i in range(len(coeffs)):
        output = output * x + coeffs[i]
    return output