fib  = 1
fib2 = 2
fibber = []
fibber.append(fib)
fibber.append(fib2)
result = 2
while (fibber[-1] < 4000000):
    x = fibber[-2] + fibber[-1]
    fibber.append(x)
    if (x % 2 == 0):
        result += x
print result, fibber
