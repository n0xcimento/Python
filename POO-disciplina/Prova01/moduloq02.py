class Continente:
	
#a
	def __init__(self, nome='SemNome'):
		self.nome=nome
		self.paises=[]

#b
	def adicPais(self, nome, popul, dimen):
		novo_pais={'nome':nome, 'populacao':popul, 'dimensao':dimen}

		self.paises.append(novo_pais)

#c
	def dimenTotal(self):
		somaTotal=0.0
		for cont in self.paises:
			somaTotal+=cont['dimensao']

		return somaTotal
		# print(somaTotal)

#d
	def populTotal(self):
		somaTotal=0.0
		for cont in self.paises:
			somaTotal+=cont['populacao']

		return somaTotal
		# print(somaTotal)
#e
#f
	def paisMaiorPopul(self):
		aux=self.paises.copy()
		aux.sort(key=lambda x: x['populacao'])
		return aux[-1]

#g
	def paisMenorPopul(self):
		aux=self.paises.copy()
		aux.sort(key=lambda x: x['populacao'])
		return aux[0]

#h
	def paisMaiorDimen(self):
		aux=self.paises.copy()
		aux.sort(key=lambda x: x['dimensao'])
		return aux[-1]

#i
	def paisMenorDimen(self):
		aux=self.paises.copy()
		aux.sort(key=lambda x: x['dimensao'])
		return aux[0]

#j
	def razaoDimenMaiorMenor(self):
		maiorDimen=self.paisMaiorDimen()
		menorDimen=self.paisMenorDimen()
		return maiorDimen['dimensao']/menorDimen['dimensao']