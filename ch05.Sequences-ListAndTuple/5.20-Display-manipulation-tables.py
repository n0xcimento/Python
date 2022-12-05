
'''
Define a function named display_table that receives a two-dimensional list containing the results of the
different multiplication tables. The column and row headings should contain the numbers 1 through 10.
'''

def display_table(table):
    # header column
    for c in range(1,10):
        print(f'   [{c}]', end='')
    print()

    for indx, row in enumerate(table):
        # row number
        print(f'[{indx+1}] ', end='')

        for item in row:
            print(f'{item:<6d}', end='')
        print()

def multiplication_table():
    '''
    Generate a quadratic multiplication table through 1 to 10
    '''
    return [[l*c for l in range(1,10)] for c in range(1,10)]


display_table(multiplication_table())