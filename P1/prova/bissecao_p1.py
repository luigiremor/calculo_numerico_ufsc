from math import exp

def bisecao(a, b, tol=1e-5):
    """
    Função que calcula o valor de x com a precisão de 10^-5
    :param f: função
    :param a: limite inferior
    :param b: limite superior
    :return: valor de x
    """ 
    k = 0
    a = float(a)
    b = float(b)

    def f(x):
        return 5 - 20*(exp(-0.2*x) - exp(-0.75*x))
    
    f_a = f(a)
    f_x = f((a+b)/2)


    while abs(f_x) > tol:
        k += 1
        x = (a + b) / 2
        f_x = f(x)

        if f_a * f_x < 0:
            b = x
        else:
            a = x
            f_a = f_x
            
        print(x, k, f_x)
    return x

print(bisecao(0, 1))
