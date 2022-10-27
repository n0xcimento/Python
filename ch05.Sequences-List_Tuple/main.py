
invoice_list = [('83', 'Electric sander', 7, 57.98), ('24', 'Power saw', 18, 99.99),
('7', 'Sledge hammer', 11, 21.50), ('77', 'Hammer', 76, 11.99), ('39', 'Jig saw', 3, 79.50)]


# print(invoice_list)
for idd, desc, qty, pr in invoice_list:
    
    print(f'{idd}\t{desc}\t{qty}\t{pr}')
