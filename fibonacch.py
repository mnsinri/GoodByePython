from inorilib import Minase
minase = Minase()
f = minase.fibonacch()
fib = []

N = int(input('Print fibonacch from 1 to N :'))

for i in range(N) :
    fib.append(f.__next__())

print(fib)
