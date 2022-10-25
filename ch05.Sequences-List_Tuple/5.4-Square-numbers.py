
'''
Write a program that
can visualize that 16 is a square number. Use a loop to create a 4-by-4 list containing zeros.
Display each element of this list in tabular format. Use the column indices as headings
across the top, and the row indices to the left of each row.
'''

l = [[0]*4 for x in range(4)]

print(f'\t[0]\t[1]\t[2]\t[3]')
for i, row in enumerate(l):
    print(f'[{i}]\t', end=' ')
    for column in row:
        print(f'{column}\t', end=' ')
    print()