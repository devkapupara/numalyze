from math import *

def romberg(f, a, b, n):
    h = (b-a)
    R = [[0]*n,[0]*n]
    R[0][0] = h/2*(f(a)+ f(b))
    print(f'{R[0][0]:.9f}\n')

    for i in range(2, n+1):
        R[1][0] = 0.5*(R[0][0] + h*(sum([f(a+(k-0.5)*h) for k in range(1, 2**(i-2)+1)])))

        for j in range(2, i+1):
            R[1][j-1] = R[1][j-2]+(R[1][j-2]-R[0][j-2])/(4**(j-1)-1)

        for k in range(i):
            print(f'{R[1][k]:.9f}', end= " ")
        print("\n")

        h = h/2

        for j in range(1, i+1):
            R[0][j-1] = R[1][j-1]

if __name__ == '__main__':
    f = lambda x: (1 + (cos(x))**2)**0.5

    a = 0
    b = 48
    n = 10

    romberg(f, a, b, n)
