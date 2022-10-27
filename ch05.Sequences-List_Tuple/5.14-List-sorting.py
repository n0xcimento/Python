'''
Write a function is_sorted that compares the results from your insertion_sort
function in Exercise 5.8 to the result from the built-in sorted function.
'''

def insertion_sort(_list):
    '''It sorts the passed list in ascending order'''

    for i in range(1, len(_list)):
        key = _list[i]

        j = i - 1
        while j >= 0 and _list[j] > key:
            _list[j + 1] = _list[j]
            j = j - 1

        _list[j + 1] = key

    return _list


def is_sorted(arg):
    '''It compares the results from insertion_sort to the result from the
    built-in sorted function'''

    return insertion_sort(arg) == sorted(arg)


ul = [4,6,3,9,1,2,11,0]

# print(insertion_sort(ul))
print(is_sorted(ul))