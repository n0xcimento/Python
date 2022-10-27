
'''
Write a script that uses the encryption key composed in Exercise 5.11 to encrypt “Help me.”

They were encrypted by calculating the position of each of its letters in the regular alphabet.
This position was used to select the corresponding letter in the encryption key.
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_key(arg):
    '''It receives a text string and generate a encription key based on those letters that
    appear only one time on passed argument'''

    # buffer will store the encription key produced
    buffer = ''

    for ch in alphabet:
        if arg.count(ch) == 1:
            buffer += ch

    for ch in alphabet:
        if ch not in buffer:
            buffer += ch

    return buffer


def encrypt(arg, en_key):
    '''It receives a string message to encrypt and a encryption key'''

    # buffer will contain the produced encrypt message
    buffer = ''

    for ch in arg:
        if ch in alphabet:
            # message's letter is used to index on alphabet and used the index in encryption key
            buffer += en_key[alphabet.index(ch)]

    return buffer


extract_book_text = 'During the second world war, messages were often encrypted\
based on an extract of a book.'

msg = 'help me'

print('\'help me\' on encrypt are:', end=' ')
print(encrypt(msg, encrypt_key(extract_book_text)))