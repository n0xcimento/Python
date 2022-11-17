import operator

name_lastname = [('allana', 'alves'), ('alzenir', 'correa'), ('cristina sousa', ('yuri', 'nascimento'), ('felipe', 'borges'))]

def find_user(key):
    return key == 'nascimento'

print(name_lastname)
user = filter(find_user, operator.itemgetter(name_lastname, 1))

print(user)