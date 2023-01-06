
'''
    A script where two sets of colors are created and a function that use either
    the comparison operator or mathematical set operators to display some results. 
'''

def greaterSet(set1, set2):
    if len(set1) > len(set2):
        print('More elements in Set1')
    elif len(set1) < len(set2):
        print('More elements in Set2')
    elif len(set1) == len(set2):
        print('Same quantity in Set1 and Set2')


def operations(set1, set2):
    print(f'\n\t| Union: {set1 | set2}\n\
        & Intersection: {set1 & set2}\n\
        - Difference: {set1 - set2}\n\
        ^ S. Difference: {set1 ^ set2}')


def main():
    colors1 = {'red', 'yellow', 'blue', 'orange', 'black', 'gray', 'white'}
    colors2 = {'gray', 'black', 'white', 'red', 'blue'}

    print(colors1)
    print(colors2)
    greaterSet(colors1, colors2)

    operations(colors1, colors2)


if __name__ == '__main__':
    main()