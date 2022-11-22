class Pais:
#a
    def __init__(self):
        self.codigo=""
        self.nome=""
        self.populacao=0
        self.dimensao=0.0
        self.pFronteira=[] #contém nomes de Pais

#b
    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getPopul(self):
        return self.populacao

    def getDimen(self):
        return self.dimensao


    def setCodigo(self, arg):
        self.codigo=arg.upper()

    def setNome(self, arg):
        self.nome=arg.capitalize()

    def setPopul(self, arg):
        self.populacao=arg

    def setDimen(self, arg):
        self.dimensao=arg

    def paisFronteira(self):
        # print('Países limítrofes com o {}!'.format(self.getNome()))
        while 0xc:
            p=str(input('Nome do País: '))
            if p == '0':
                break
            else:
                self.pFronteira.append(p.capitalize())
#c
    # verifica se é o mesmo país
    def compPais(self, code):
        if self.codigo == code:
            print('\nMesmo país')
        else:
            print('\nPaíses diferentes')

#d
    # países limítrofes
    def proxPais(self, name):
        if name in self.pFronteira:
            print('\nPais limítrofe')
        else:
            print('\nPaís não limítrofe')

#e
    def densPopul(self):
        return float(self.getPopul()/self.getDimen())

#f
    # países comuns entre dois países
    def comumPais(self, outro):

        comum=[]
        for p in outro.pFronteira:
            if p in self.pFronteira:
                comum.append(p)
        
        print('\nPaíses vizinhos comuns do {} e {}:'.format(self.getNome(), outro.getNome()))
        for i in comum:
            print(i)

#g
    # ordena todos os países que fazem fronteira
    def ordenaPFront(self): #ordena países limítrofes
        frontOrdem=[]
        
        for i in self.pFronteira:
            frontOrdem.append(i)

        frontOrdem.sort()
        for f in frontOrdem:
            print(f)