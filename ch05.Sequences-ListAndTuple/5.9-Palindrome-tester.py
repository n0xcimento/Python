'''
Write a function is_palindrome that takes a string and returns True if it’s a palindrome
and False otherwise. Use a stack to help determine whether a string is a palindrome.
'''

def is_palindrome(arg):
    stack = list()

    for a in arg:
        stack.append(a)

    for a in arg:
        if a != stack.pop():
            return False

    return True


txt = 'rararararar'

print(f'{txt} Palindrome? {is_palindrome(txt)}')