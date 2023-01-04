
'''
    A function that receives a list of email addresses and display only the unique addresses.
    The function uses a set to get the unique email addresses from the list.
'''

def remove_duplicate_addresses(addr_list):
    unique_addr = set(addr_list)

    for addr in unique_addr:
        print(addr)



addresses = ['abc@hotmail.com', 'xyz@gmail.com', 'cube@outlook.com', 'abc@hotmail.com', 'scrim@gmail.com']

remove_duplicate_addresses(addresses)