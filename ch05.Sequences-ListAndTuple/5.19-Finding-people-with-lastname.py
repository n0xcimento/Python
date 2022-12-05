'''
Create a list of tuples containing first and last names. Use filter to locate the tuples containing the last name Jones. Ensure that
several tuples in your list have that last name.
'''

people = [('yuri', 'nascimento'), ('gustavo', 'jones'), ('stefany', 'borges'), ('marcos', 'jones'), ('cris', 'maria'), ('stefan', 'jones'),
('stefany', 'jones')]

def jones_person(tuplee):
    '''Get a tuple containing 2 string items and checking if last item is "jones"'''

    return tuplee.__getitem__(1) == 'jones'


# Only people containing last name jones
jones_people = filter(lambda x: x.__getitem__(1) == 'jones', people)
# jones_people = filter(jones_person, people)

for a in jones_people:
    print(a)