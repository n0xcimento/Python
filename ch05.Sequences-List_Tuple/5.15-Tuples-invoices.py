from operator import itemgetter

# Sample hardware data table
invoice_list = [('83', 'Electric sander', 7, 57.98), ('24', 'Power saw', 18, 99.99),
('7', 'Sledge hammer', 11, 21.50), ('77', 'Hammer', 76, 11.99), ('39', 'Jig saw', 3, 79.50)]


print('[raw tuples]')
print(f'{"Number":<8}{"Description":<16}{"Quantity":<16}Price')
for f0, f1, f2, f3 in invoice_list:
    print(f'{f0:<8}{f1:<16}{f2:<16}{f3}')


# a) Use function sorted with a key argument to sort the tuples by part description, then display the results.
sorted_by_description = sorted(invoice_list, key=itemgetter(1))
print('\n[Sorted by Description field]')
print(f'{"Number":<8}{"Description":<16}{"Quantity":<16}Price')
for f0,f1,f2,f3 in sorted_by_description:
    print(f'{f0:<8}{f1:<16}{f2:<16}{f3}')


# b) Use the sorted function with a key argument to sort the tuples by price, then display the results.
sorted_by_price = sorted(invoice_list, key=(itemgetter(3)))
print('\n[Sorted by Price field]')
print(f'{"Number":<8}{"Description":<16}{"Quantity":<16}Price')
for f0,f1,f2,f3 in sorted_by_price:
    print(f'{f0:<8}{f1:<16}{f2:<16}{f3}')


# c) Map each invoice tuple to a tuple containing the part description and quantity; display the results.
description_qty = [(f1,f2) for f0,f1,f2,f3 in invoice_list]
sorted_by_quantity = sorted(description_qty, key=itemgetter(1))
print('\n[Map fields and sorted by Quantity]')
print(f'{"Description":<16}{"Quantity"}')
for f0, f1 in sorted_by_quantity:
    print(f'{f0:<16}{f1}')


# d) Map each invoice tuple to a tuple containing the part description and the value of the invoice; sort the results by the invoice value
description_value = [(f1,f3) for f0,f1,f2,f3 in invoice_list]
sorted_by_value = sorted(description_value, key=itemgetter(1))
print('\n[Map fields and sorted by Value]')
print(f'{"Description":<16}{"Value"}')
for f0, f1 in sorted_by_value:
    print(f'{f0:<16}{f1}')


# e) Modify Part (d) to filter the results to invoice values in the range $200 to $500.
description_value = [(f1,f3) for f0,f1,f2,f3 in invoice_list if ( 200 <= f3 <= 500 )]
sorted_by_value = sorted(description_value, key=itemgetter(1))
print('\n[Map fields and sorted by Value, such that Value in the $200 to $500 range]')
print(f'{"Description":<16}{"Value"}')
for f0, f1 in sorted_by_value:
    print(f'{f0:<16}{f1}')


total_value_invoices = 0
print(f'\n{"Number":<8}{"Description":<16}{"Quantity":<16}Price')
for f0,f1,f2,f3 in invoice_list:
    print(f'{f0:<8}{f1:<16}{f2:<16}{f3}')
    total_value_invoices += f3

print(f'{"[Total price:":<40}{total_value_invoices:.2f}]')