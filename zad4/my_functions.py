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
            return new_result
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
        return None  # Unsupported number of nodes

    # Change of variable x = ((b-a)/2) * t + (b+a)/2
    # Integral over [a, b] is (b-a)/2 times the integral over [-1, 1]
    integral = 0.0
    for i in range(n):
        x = 0.5 * (b - a) * nodes[i] + 0.5 * (b + a)
        integral += weights[i] * f(x)

    integral *= 0.5 * (b - a)
    return integral

