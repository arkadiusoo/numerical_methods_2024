
def difference_quotient(nodes_x, nodes_y):
    if len(nodes_x) == 2:
        return (nodes_y[1] - nodes_y[0]) / (nodes_x[1] - nodes_x[0])
    else:
        divisor = nodes_x[-1] - nodes_x[0]
        return (difference_quotient(nodes_x[1:], nodes_y[1:]) - difference_quotient(nodes_x[:-1], nodes_y[:-1])) / divisor

