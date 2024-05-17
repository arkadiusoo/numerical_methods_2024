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



