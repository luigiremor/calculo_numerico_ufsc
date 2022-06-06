from math import exp

def falsa_posicao(a, b, tol=1e-5):
    """
    Função que calcula o valor de x com a precisão de 10^-5
    :param f: função
    :param a: limite inferior
    :param b: limite superior
    :return: valor de x
    """
    def f(x):
        return 5 - 20*(exp(-0.2*x) - exp(-0.75*x))

    a = float(a)
    b = float(b)

    f_a = f(a)
    f_x = 1 
    k = 0
    print(a, b, f(a), f(b))
    while abs(f_x) > tol:
        x = a - (f(a)*(b-a)/(f(b)-f(a)))
        f_x = f(x)
        if f_a * f_x < 0:
            b = x
        else:
            a = x
            f_a = f(x)
        k += 1

        print(x, f(x), k)
    return x

print(falsa_posicao(0, 1))

# def f(x):
#     return 10 - 20*(exp(-0.2*x) - exp(-0.75*x))

# def relation(a, b):
#     x = a - (f(a)*(b-a)/(f(b)-f(a)))
#     return x

# a = 0
# b = 1
# a = float(a)
# b = float(b)

# print(relation(a,b))
# f_x = 1 