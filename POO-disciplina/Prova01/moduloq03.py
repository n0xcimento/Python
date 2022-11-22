from time import strftime

class BatimentosCardiacos:
        
    def __init__(self, nome=None, sobrenome=None, mes=None, dia=None, ano=None):
        self.nome=nome
        self.sobreNome=sobrenome
        self.nascimento={'mes':mes, 'dia':dia, 'ano':ano}

    def setNome(self, nome:str):
        self.nome=nome

    def getNome(self):
        return self.nome

    def setsobreNome(self, sobrenome:str):
        self.sobreNome=sobrenome

    def getsobreNome(self):
        return self.sobreNome

    def setNascimento(self, mes:int, dia:int, ano:int):
        self.nascimento['mes']=mes
        self.nascimento['dia']=dia
        self.nascimento['ano']=ano

    def getNascimento(self):
        # print(self.nascimento['mes'], self.nascimento['dia'], self.nascimento['ano'])
        return self.nascimento

    def idadeAnos(self):
        anoAtual=int(strftime('%Y'))
        mesAtual=int(strftime('%m'))
        diaAtual=int(strftime('%d'))

        idade=anoAtual - self.nascimento['ano']
        
        if(mesAtual == self.nascimento['mes'] and diaAtual < self.nascimento['dia']):
            idade-=1
        return idade

    def freqCardiacaMax(self):
        return 220 - self.idadeAnos()

    def freqCardiacaAlvo(self):
        interv=[]
        interv.append(self.freqCardiacaMax()*50/100)
        interv.append(self.freqCardiacaMax()*80/100)
        return interv