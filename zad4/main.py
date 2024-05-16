def select_function():
    print("Select the function to integrate:")
    print("1: f(x) = x^2")
    print("2: f(x) = sin(x)")
    print("3: f(x) = e^x")
    choice = input("Enter choice (1-3): ")
    if choice == '1':
        return lambda x: x**2
    elif choice == '2':
        return lambda x: np.sin(x)
    elif choice == '3':
        return lambda x: np.exp(x)
    else:
        raise ValueError("Invalid function choice")

def main():
    f = select_function()
    a = float(input("Enter the lower bound of the integral (a): "))
    b = float(input("Enter the upper bound of the integral (b): "))
    eps = float(input("Enter the desired accuracy (epsilon): "))
    method = input("Choose the method (S for Simpson, G for Gauss-Legendre): ")
    if method.upper() == 'S':
        result = simpson_composite(f, a, b, eps)
        print("Result of Simpson's Composite method:", result)
    elif method.upper() == 'G':
        n = int(input("Enter the number of nodes for Gauss-Legendre (2-5): "))
        result = gauss_legendre_quadrature(f, a, b, n)
        print("Result of Gauss-Legendre method:", result)
    else:
        raise ValueError("Invalid method choice")

if __name__ == "__main__":
    main()