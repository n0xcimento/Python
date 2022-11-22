
'''
Write a function that accepts a string as input and isolates the different unique letters ignoring punctuation,
spaces, and case sensitivity. The function should check if the encryption key contains all
letters of the alphabet. If not, the missing letters should be added to the key.
'''

def encrypt_key(arg):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    buffer = ''
    for ch in alphabet:
        if arg.count(ch) == 1:
            buffer += ch

    for ch in alphabet:
        if ch not in buffer:
            buffer += ch

    return buffer


extract = 'during the second world war, messages were often encrypted \
based on an extract of a book.'
print(encrypt_key(extract))