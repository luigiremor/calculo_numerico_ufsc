from math import exp

def secante(a, b, tol=1e-5):
    """
    Função que calcula o valor de x com a precisão de 10^-5
    :param f: função
    :param a: limite inferior
    :param b: limite superior
    :return: valor de x
    """ 

    def f(x):
        return 5 - 20*(exp(-0.2*x) - exp(-0.75*x))

    k = 0

    while abs(f(b)) > tol:
        x = (a*f(b) - b*f(a))/(f(b) - f(a))
        a = b
        b = x
        k += 1
        print(x, f(x), k)
    return x

print(secante(1, 2))