
'''
Write a function that receives a list and returns a list containing only unique
values.
'''

def duplicate_elimination(_list):
    temp = list()

    for i in _list:
        if i not in temp:
            temp.append(i)

    return temp


l = list(range(100))
l += range(100)
l += range(100)

print(duplicate_elimination(l))