from .evaluate import Evaluator

def trapezoidal(expr, a, b, n):
    f = Evaluator(expr)
    a, b, n = f.parse_arguments(a,b,n)
    h = (b-a)/n

    total = (f.evaluate(a)+f.evaluate(b))/2
    x = a + h

    for i in range(n-1):
        total += f.evaluate(x)
        x += h

    return total*h, f.get_latex()

def simpsons(expr, a, b, n):
    odd_input = False
    f = Evaluator(expr)
    a, b = f.parse_arguments(a,b)
    if n % 2 == 1:
        odd_input = True
        n += 1
    h = (b-a)/n

    total = f.evaluate(a) + f.evaluate(b)
    x = a+h

    for i in range(n-1):
        coeff = 2 if (i & 1) else 4
        total += coeff * f.evaluate(x)
        x += h

    return total*h/3, odd_input, f.get_latex()

def romberg(expr, a, b, n):
    f = Evaluator(expr)
    a, b = f.parse_arguments(a,b)
    h = (b-a)
    R = [[0]*n,[0]*n]
    R[0][0] = h/2*(f.evaluate(a)+ f.evaluate(b))
    result = [[] for i in range(n)]
    result[0].append(R[0][0])

    for i in range(2, n+1):
        R[1][0] = 0.5*(R[0][0] + h*(sum([f.evaluate(a+(k-0.5)*h) for k in range(1, 2**(i-2)+1)])))

        for j in range(2, i+1):
            R[1][j-1] = R[1][j-2]+(R[1][j-2]-R[0][j-2])/(4**(j-1)-1)

        result[i-1] = R[1].copy()
        h = h/2

        for j in range(1, i+1):
            R[0][j-1] = R[1][j-1]
    return result, f.get_latex()

if __name__ == '__main__':
    f = lambda x: (1 + (cos(x))**2)**0.5

    a = 0
    b = 48
    n = 10

    romberg(f, a, b, n)
    # f = lambda x: exp(x**2)
    # a = int(input("Enter lower limit of integration: "))
    # b = int(input("Enter upper limit of integration: "))
    # n = int(input("Number of intervals: "))
    # romberg(f, a, b, n)
