'''
Write a function insertion sort implementing the described algorithm. Use a list of 10 unique
and randomly picked numbers between 0 and 100 to test this function. Display the unsorted and
the sorted list to evaluate the validity of your function.
'''

import random

def insertion_sort(_list):
    for i in range(1, len(_list)):
        key = _list[i]

        j = i - 1
        while j >= 0 and _list[j] > key:
            _list[j + 1] = _list[j]
            j = j - 1

        _list[j + 1] = key

    return _list


ul = [ random.randrange(0, 100) for x in range(10)]

print(ul)

print(insertion_sort(ul))