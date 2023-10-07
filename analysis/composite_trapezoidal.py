def trapezoidal(f, a, b, n):
	h = (b-a)/n

	total = (f(a)+f(b))/2
	x = a + h

	for i in range(n-1):
	    total += f(x)
	    x += h

	return total*h

if __name__ == '__main__':
	f = lambda x: x**3

	a = int(input("Enter lower limit of integration: "))
	b = int(input("Enter upper limit of integration: "))
	n = int(input("Enter n: "))
	print(trapezoidal(f, a, b, n))
