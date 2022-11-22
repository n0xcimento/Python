from os import system

def include(xcursor):
	d=str(input('Descrição do produto: '))
	qty=int(input('Quantidade do produto: '))

	xcursor.execute("INSERT INTO produto (descript, quantity) VALUES ('{}',{});".format(d, qty))


def ls(xcursor):
	xcursor.execute('SELECT * FROM produto;')

	rows = xcursor.fetchall()

	print('{0}| {1}'.format(str('PRODUTO').ljust(40), 'QUANTIDADE'))
	print('-'*52)

	for x in rows:
		print('{0}{1}'.format(x[1].ljust(42), str(x[2])))


def add(xcursor):
	"""Adiciona quantidade de um produdo específico"""
	xcursor.execute('SELECT * FROM produto;')

	rows = xcursor.fetchall()

	print('{0}| {1}| {2}'.format(str('COD').ljust(4), str('PRODUTO').ljust(40), 'QUANTIDADE'))
	print('-'*58)

	codQty=dict()
	for x in rows:
		print('{0}{1}{2}'.format(str(x[0]).ljust(6), x[1].ljust(42), str(x[2])))
		codQty.setdefault(x[0], x[2])

	COD=int(input('\nInforme o COD do produto que deseja ADICIONAR ao estoque: '))

	if COD not in codQty:
		print('Produto Inexistente')
	else:
		addQty=int(input('Quantidade a ser ADICIONADA: '))

		xcursor.execute('UPDATE produto SET quantity = {} WHERE id = {};'.format(addQty + codQty[COD], COD))


def take(xcursor):
	xcursor.execute('SELECT * FROM produto;')

	rows = xcursor.fetchall()

	print('{0}| {1}| {2}'.format(str('COD').ljust(4), str('PRODUTO').ljust(40), 'QUANTIDADE'))
	print('-'*58)

	codQty=dict()
	for x in rows:
		print('{0}{1}{2}'.format(str(x[0]).ljust(6), x[1].ljust(42), str(x[2])))
		codQty.setdefault(x[0], x[2])

	COD=int(input('\nInforme o COD do produto que deseja RETIRAR do estoque: '))

	if COD not in codQty:
		print('Produto Inexistente')
	else:
		qtyTake=int(input('Quantidade a ser RETIRADA: '))

		if codQty[COD] - qtyTake >= 0:
			xcursor.execute('UPDATE Produto SET quantity = {} WHERE id = {};'.format(codQty[COD] - qtyTake, COD))
		else:
			print('Quantidade a ser RETIRADA ultrapassou a quantidade DISPONÍVEL no estoque!')


def remove(xcursor):
	xcursor.execute('SELECT * FROM produto;')

	rows = xcursor.fetchall()

	print('{0}| {1}| {2}'.format(str('COD').ljust(4), str('PRODUTO').ljust(40), 'QUANTIDADE'))
	print('-'*58)

	codQty=dict()
	for x in rows:
		print('{0}{1}{2}'.format(str(x[0]).ljust(6), x[1].ljust(42), str(x[2])))
		codQty.setdefault(x[0], x[2])

	COD=int(input('\nInforme o COD do produto que deseja EXCLUIR: '))

	if COD not in codQty:
		print('Produto Inexistente')
	else:
		xcursor.execute('DELETE FROM produto WHERE id = {}'.format(COD))
		print('Produto Excluído')



def menu(x):

	cursor = x.cursor()

	while 0xc:
		print('[1] INCLUIR Novo Produto')
		print('[2] LISTAR Todos Produtos')
		print('[3] ADICIONAR ao Estoque')
		print('[4] RETIRAR do Estoque')
		print('[5] EXCLUIR Produto')
		op=int(input('[6] SAIR\n: '))

		system('clear')

		if op == 1:
			print('INCLUIR NOVO PRODUTO')
			include(cursor)

		elif op == 2:
			print('LISTAR PRODUTOS')
			ls(cursor)

		elif op == 3:
			print('ADICIONAR AO ESTOQUE')
			add(cursor)

		elif op == 4:
			print('RETIRAR DO ESTOQUE')
			take(cursor)

		elif op == 5:
			print('EXCLUIR PRODUTO')
			remove(cursor)

		elif op == 6:
			break

		x.commit()
		input('\n[ Tecle ENTER para continuar ] ')
		# system('cls')   # WINDOWS
		system('clear') # LINUX

	print('Exiting...')