
'''
    Script the uses a dictionary to sumarize the frequency of each letter in a given text.
'''

def letter_frequency(txt):
    letters = list(txt.lower())

    frequency = dict()

    for ch in letters:

        if ch in frequency:
            frequency[ch] += 1
        elif ch.isalnum():
            frequency[ch] = 1

    print(f'{"letter":<10}Frequency')
    for k, v in frequency.items():
        print(f'{k:<10}{v}')


txt = 'The Python Standard Library already contains the counting functionality'

letter_frequency(txt)