'''
Starting with a list containing 1 through 10, use filter, map and sum to calculate the total of the
triples of the even integers from 2 through 10.

Reimplement code with list comprehensions rather than filter and map
'''

integers = list(range(1,10))

# Using map and filter 
ans = sum(map(lambda a: a*3, filter(lambda a: a % 2 == 0, integers)))
print(ans)

# Using list comprehension
ans = sum([3*x for x in integers if x % 2 == 0])
print(ans)