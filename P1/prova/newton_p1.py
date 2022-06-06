from math import exp

def newton(x, tol=1e-5):
    """
    Função que calcula o valor de x com a precisão de 10^-5
    :param f: função
    :param x: valor inicial
    :return: valor de x
    """

    def f(x):
        return 5 - 20*(exp(-0.2*x) - exp(-0.75*x))

    def df(x):
        return 4*exp(-0.2*x) - 15*exp(-0.75*x)

    k = 0

    while abs(f(x)) > tol:
        x = x - f(x)/df(x)
        k += 1
        print(x, f(x), k)
    return x

print(newton(1))

def f(x):
    return 5 - 20*(exp(-0.2*x) - exp(-0.75*x))
