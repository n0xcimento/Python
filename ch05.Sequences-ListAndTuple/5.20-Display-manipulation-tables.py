
'''
Define a function named display_table that receives a two-dimensional list containing the results of the
different multiplication tables. The column and row headings should contain the numbers 1 through 10.
'''

def display_table(twoD_list):
    # index column
    for c in range(1,10):
        print(f'     [{c}]', end='')

    print()

    for indx, row in enumerate(twoD_list):
        print(f'[{indx+1}]x', end='') # index column

        for indxc, column in enumerate(row):
            if indxc != 0:
                print(f'{column:>8}', end='')
            else:
                print(f'{column:>3}', end='')

        print()


multi_table = [[l*c for l in range(1,10)] for c in range(1,10)]

display_table(multi_table)