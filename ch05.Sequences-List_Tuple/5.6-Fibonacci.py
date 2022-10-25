
'''
Define a function fib that receives three
consecutive numbers of the Fibonacci series and returns the three subsequent values. Then,
call the function three times starting with the numbers 0, 1, and 1 and restarting the func-
tion each time with the resulting numbers of the previous iteration.
'''

def fib(n1, n2, n3):
    n4 = n2 + n3
    n5 = n3 + n4
    n6 = n4 + n5
    return [n4, n5, n6]


a, b, c = fib(0, 1, 1)
print(a, b, c)
a, b, c = fib(a, b, c)
print(a, b, c)
a, b, c = fib(a, b, c)
print(a, b, c)