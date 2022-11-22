from moduloq02 import Continente
# from os import system


def menu(x):

	while 0xc:
		xmode=int(input('\n1. Adicionar Países\n2. Consultar\n0. Sair\n: '))

		if xmode == 1:
			op='a'
			while op != 'v':
				nome=str(input('\nNome do País: ')).capitalize()
				pop=int(input('População do País: '))
				dim=float(input('Dimensão do País: '))
				x.adicPais(nome,pop,dim)
				op=str(input('\n[a]dicionar país / [v]oltar | [a/v]: '))

		elif xmode == 2:

			gmode=int(input('\n1. Dimensão Total Continente\n2. População Total Continente\n3. Pais Maior População\n'
				'4. Pais Menor População\n5. Pais Maior Dimensão\n6. Pais Menor Dimensão\n7. Razão País Maior e Menor Dimensão\n: '))

			if gmode == 1:
				print('\n',x.dimenTotal())

			elif gmode == 2:
				print('\n',x.populTotal())

			elif gmode == 3:
				print('\n',x.paisMaiorPopul()['nome'])

			elif gmode == 4:
				print('\n',x.paisMenorPopul()['nome'])

			elif gmode == 5:
				print('\n',x.paisMaiorDimen()['nome'])

			elif gmode == 6:
				print('\n',x.paisMenorDimen()['nome'])

			elif gmode == 7:
				print('\n',x.razaoDimenMaiorMenor())			

		elif xmode == 0:
			break


cont=Continente(str(input('Nome Continente: ')).capitalize())

menu(cont)