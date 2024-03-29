# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
Fib1 = 0
Fib2 = 1
FibMax = 4000000
FibNext = int()
FibSum = int()
while FibNext < FibMax:
    FibNext = Fib1 + Fib2
    Fib1 = Fib2
    Fib2 = FibNext
    if FibNext %2 == 0:
        FibSum += FibNext
    print (FibNext)
print(FibSum)