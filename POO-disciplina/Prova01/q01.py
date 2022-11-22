from moduloq01 import Pais
from os  import system

def menu(x):
    
    while 0xc:
        xmode=int(input('\n1. Alterar\n2. Consultar\n0. Outro País\n: '))

        if xmode == 1:
            while 0xc:
                system('clear') #LINUX
                # system('cls') #windows

                print('MENU: Alterar | PAÍS: {}'.format(x.getNome()))                
                print('1. Nome')
                print('2. Código')
                print('3. População')
                print('4. Dimensaõ')
                print('5. Países Limítrofes')
                smode=int(input('0. voltar\n: '))

                if smode == 1:
                    nome=str(input('Novo Nome: '))
                    x.setNome(nome)

                elif smode == 2:
                    code=str(input('Novo Código: '))
                    x.setCodigo(code)
                
                elif smode == 3:
                    pop=int(input('Nova Quantide População: '))
                    x.setPopul(pop)
                
                elif smode == 4:
                    dim=float(input('Nova Dimensaõ: '))
                    x.setDimen(dim)

                elif smode == 5:
                    # print('Adicionar País')
                    x.paisFronteira()
                else:
                    break

        elif xmode == 2:
            while 0xc:
                system('clear') #LINUX
                # system('cls') #windows

                print('MENU: Consula | PAÍS: {}'.format(x.getNome()))
                print('1. Nome')
                print('2. Código')
                print('3. População')
                print('4. Dimensaõ')
                print('5. Mesmo País?')
                print('6. Países Limítrofes?')
                print('7. Densidade Populacional')
                print('8. Vizinhos Comuns')
                print('9. Países vizinhos ordenados')
                gmode=int(input('0. Voltar\n: '))
                

                if gmode == 1:
                    print(x.getNome())

                elif gmode == 2:
                    print(x.getCodigo())
                
                elif gmode == 3:
                    print(x.getPopul())
                
                elif gmode == 4:
                    print('{} m^2'.format(x.getDimen()))

                elif gmode == 5:
                    code=str(input('\nCódigo do País para verificar: ')).upper()
                    x.compPais(code)

                elif gmode == 6:
                    name=str(input('\nNome do País para verificar: ')).capitalize()
                    x.proxPais(name)

                elif gmode == 7:
                    print(x.densPopul())

                elif gmode == 8:
                    print()
                    for p in lpaises:
                        if p.getCodigo() == x.getCodigo():
                            continue
                        print('{0} - {1}'.format(p.getCodigo(), p.getNome()))

                    code = str(input('\nCódigo do País para verificar os vizinhos comuns\n: ')).upper()
                    
                    for p in lpaises:
                        if p.getCodigo() == code:
                            x.comumPais(p)

                elif gmode == 9:
                    print('\nPaíses vizinhos do {} em ordem alfabética:'.format(x.getNome()))
                    x.ordenaPFront()

                else:
                    break

                input('\n[ Tecle ENTER para continaur ] ')
                system('clear') #LINUX
                # system('cls') #windows

        else:
            return


lpaises=[]
print('INFORME AS SEGUINTES INFORMAÇÕES DE 3 PAÍSES')
for i in range(3):
    p=Pais()
    p.setNome(str(input('\nNome do {} País: '.format(i+1))))
    p.setCodigo(input('Código do Pais: '))
    p.setPopul(int(input('População do País (inteiro): ')))
    p.setDimen(float(input('Dimensão do País: ')))

    print('\nPaíses limítrofes com {} | [0] Continuar'.format(p.getNome()))
    p.paisFronteira()
    lpaises.append(p)

while 0xc:
    system('clear')
    for i in range(len(lpaises)):
        print('{0}. {1}'.format(i+1, lpaises[i].getNome()))

    op=int(input('\nPaís para ALTERAR ou CONSULTAR informações | [0] Sair\n: '))    
    if op == 0:
        break
    else:
        menu(lpaises[op-1])