def simpsons(f, a, b, n):
    odd_input = False
    if n % 2 == 1:
        odd_input = True
        n += 1
    h = (b-a)/n

    total = f(a) + f(b)
    x = a+h

    for i in range(n-1):
        coeff = 2 if (i & 1) else 4
        total += coeff * f(x)
        x += h

    return total*h/3, odd_input

if __name__ == '__main__':
    f = lambda x: exp(x**2)
    a = int(input("Enter lower limit of integration: "))
    b = int(input("Enter upper limit of integration: "))
    n = int(input("Number of intervals: "))
    simpsons(f, a, b, n)
