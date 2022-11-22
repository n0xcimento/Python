from moduloq03 import BatimentosCardiacos

def menu():

	while 0xc:
	    xmode=int(input('\n1. Alterar\n2. Consultar\n0. sair\n: '))

	    if xmode == 1:
	        smode=int(input('\n1. Nome\n2. Sobrenome\n3. Data de Nascimento\n: '))
	        
	        if smode == 1:
	            px.setNome(str(input('Novo Nome: ')).capitalize())

	        elif smode == 2:
	            px.setsobreNome(str(input('Novo Sobrenome: ')).capitalize())

	        elif smode == 3:
	            dia=int(input('Dia: '))
	            mes=int(input('Mês: '))
	            ano=int(input('Ano: '))

	            px.setNascimento(mes, dia, ano)

	    elif xmode == 2:
	        gmode=int(input('\n1. Nome\n2. Sobrenome\n3. Data de Nascimento\n4. Idade | Freq. Cardíaca Máxima | Fre. Cardíacas Alvo\n: '))

	        if gmode == 1:
	            print('\n',px.getNome())

	        elif gmode == 2:
	            print('\n',px.getsobreNome())

	        elif gmode == 3:
	            aux=px.getNascimento()
	            
	            dia=aux['dia']
	            mes=aux['mes']
	            ano=aux['ano']

	            print('\n',dia,'/', mes,'/', ano)

	        elif gmode == 4:
	            idade=px.idadeAnos()
	            fcm=px.freqCardiacaMax()
	            fca=px.freqCardiacaAlvo()
	            print('\nidade: {}\nFreq. Cardíaca Máxima: {}\nFreq. Cardíaca Alvo: {}-{}'.format(idade, fcm, fca[0],fca[1]))

	    elif xmode == 0:
	    	break




print('+ Batimentos Cardíacos +\nINFORME AS SEGUINTES INFORMAÇÕES DE UMA PESSOA')
nome=str(input('Nome: ').capitalize())
sobrenome=str(input('Sobrenome: ').capitalize())
dia=int(input('Dia de nascimento: '))
mes=int(input('Mês de nascimento: '))
ano=int(input('Ano de nascimento: '))

px=BatimentosCardiacos(nome, sobrenome, mes, dia, ano)

menu()