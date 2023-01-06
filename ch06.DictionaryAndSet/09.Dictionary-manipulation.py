
'''
    Script that shows the user a list of dictionary manipulation options to choose
    from. Based on the choice, the corresponding manipulation is performed, and the result
    is shown on the screen.
'''

def abbreviation_country(country, key):
    return country[key]


def displayAll_2column(dict_list):

    for k,v in dict_list.items():
        print(f'{k:<15}{v}')


def new_or_change(dict_list, key_value):
    k, v = key_value.split(' ')
    dict_list[k] = v


def invert_keyValue(dict_list):
    tmp = {v:k for k,v in dict_list.items()}
    return tmp

def value2uppercase(dict_list):

    for k, v in dict_list.items():
        dict_list[k] = v.upper()


def menu():

    choice = int(input('\
            [1] Show abbreviation of country\n\
            [2] Display all key-values in two column\n\
            [3] New or change key-value\n\
            [4] Invert the key-vale dictionary\n\
            [5] Abbreviation to Uppercase\n\
            [0] Exit\n: '))
    return choice


def main():
    tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

    choice = menu()
    while choice:

        if choice == 1:
            country = str(input('Country: ')).capitalize()
            print(abbreviation_country(tlds, country))

        elif choice == 2:
            displayAll_2column(tlds)

        elif choice == 3:
            key_value = str(input('Enter [Country Abbr] form: '))
            new_or_change(tlds, key_value)
            displayAll_2column(tlds)

        elif choice == 4:
            tlds = invert_keyValue(tlds)
            displayAll_2column(tlds)

        elif choice == 5:
            value2uppercase(tlds)
            displayAll_2column(tlds)
        else:
            print('[ Invalid option! ]')

        choice = menu()


if __name__ == '__main__':
    main()