def sum_a_b(a,b):
    print (id (a))
    a += 1
    print (id(a))
    print (id(b))
    c = a+b
    print (id(c))
    return c

num1 = 10
num2 = 5
print (sum_a_b(num1, num2))
print (id(num1))
print (id(num2))
