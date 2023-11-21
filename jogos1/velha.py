from random import *

campos = [['A1', 'B2', 'C3'],
          ['A1', 'B2', 'C3'],
          ['A1', 'B2', 'C3']]

  
casas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

COP = [] #casas_ocupadas_jogador
COM = [] #casas_ocupadas_maquina

rodadas = 9


velha = False
vitoria = False
derrota = False

def verifica_casa():
    if jogada_jogador = 1:
        COP.append('A1')
    else:
        if jogada_jogador = 2:
            COP.append('A2')
        else:
            if jogada_jogador = 3:
                COP.append('A3')
            else:
                if jogada_jogador = 4:
                    COP.append('B1')
                else:
                    if jogada_jogador = 5:
                        COP.append('B2')
                    else:
                        if jogada_jogador = 6:
                            COP.append('B3')
                        else:
                            if jogada_jogador = 7:
                                COP.append('C1')
                            else:
                                if jogada_jogador = 8:
                                    COP.append('C2')
                                else:
                                    if jogada_jogador = 9:
                                        COP.append('C3')
    if jogada_maquina = 1:
        COM.append('A1')
    else:
        if jogada_maquina = 2:
            COM.append('A2')
        else:
            if jogada_maquina = 3:
                COM.append('A3')
            else:
                if jogada_maquina = 4:
                    COM.append('B1')
                else:
                    if jogada_maquina = 5:
                        COM.append('B2')
                    else:
                        if jogada_maquina = 6:
                            COM.append('B3')
                        else:
                            if jogada_maquina = 7:
                                COM.append('C1')
                            else:
                                if jogada_maquina = 8:
                                    COM.append('C2')
                                else:
                                    if jogada_maquina = 9:
                                        COM.append('C3')

    
#jogador#


while rodadas > 0 or not velha and not vitoria and not derrota:
        
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')

    jogada_jogador = int(input('Digite uma casa: '))


    
    while jogada_jogador > 9 and jogada_jogador < 1 and jogada_jogador in casas_ocupadas:

        

        print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
        print('-----|-----|-----')
        print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
        print('-----|-----|-----')
        print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
        jogada_jogador = int(input('Digite uma casa: '))
        
    while jogada_jogador not in casas or jogada_jogador < 1 or jogada_jogador > 9:
            jogada_jogador = int(input('Digite uma casa: '))
            
    COP.append(jogada_jogador)
    
    
    



    casas[jogada_jogador - 1] = 'X'
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  \n')
    ###########



if 'A1' in COM and 'A2' in COM and 'A3' in COM or 'B1' in COM and 'B2' in COM and 'B3' in COM or 'C1' in COM and 'C2' in COM and 'C3' in COM or 'A1' in COM and 'B1' in COM and 'C1' in COM or 'A2' in COM and 'B2' in COM and 'C2' in COM or 'A3' in COM and 'B3' in COM and 'C3' in COM or 'A1' in COM and 'B2' in COM and 'C3' in COM or 'A3' in COM and 'B2' in COM and 'C1' in COM:
    derrota == True
    print('A maquina venceu')
    rodadas = 0
else:
    if 'A1' in COP and 'A2' in COP and 'A3' in COP or 'B1' in COP and 'B2' in COP and 'B3' in COP or 'C1' in COP and 'C2' in COP and 'C3' in COP or 'A1' in COP and 'B1' in COP and 'C1' in COP or 'A2' in COP and 'B2' in COP and 'C2' in COP or 'A3' in COP and 'B3' in COP and 'C3' in COP or 'A1' in COP and 'B2' in COP and 'C3' in COP or 'A3' in COP and 'B2' in COP and 'C1' in COP:
    
        vitoria == True 
        print('Você venceu')
        rodadas = 0
    else:
        if COP + COM == 9:
            velha == True
            print('Velha')
            rodadas = 0
    


    #maquina#
    jogada_maquina = randint(1,10)
    while jogada_maquina not in casas:
        jogada_maquina = randint(1,10)
        
    print(f'A maquina jogou: {jogada_maquina}')

    COM.append(jogada_maquina)

    casas[jogada_maquina - 1] = 'O'


    
    
if 'A1' in COM and 'A2' in COM and 'A3' in COM or 'B1' in COM and 'B2' in COM and 'B3' in COM or 'C1' in COM and 'C2' in COM and 'C3' in COM or 'A1' in COM and 'B1' in COM and 'C1' in COM or 'A2' in COM and 'B2' in COM and 'C2' in COM or 'A3' in COM and 'B3' in COM and 'C3' in COM or 'A1' in COM and 'B2' in COM and 'C3' in COM or 'A3' in COM and 'B2' in COM and 'C1' in COM:
    derrota == True
    print('A maquina venceu')
    rodadas = 0
else:
    if 'A1' in COP and 'A2' in COP and 'A3' in COP or 'B1' in COP and 'B2' in COP and 'B3' in COP or 'C1' in COP and 'C2' in COP and 'C3' in COP or 'A1' in COP and 'B1' in COP and 'C1' in COP or 'A2' in COP and 'B2' in COP and 'C2' in COP or 'A3' in COP and 'B3' in COP and 'C3' in COP or 'A1' in COP and 'B2' in COP and 'C3' in COP or 'A3' in COP and 'B2' in COP and 'C1' in COP:
    
        vitoria == True 
        print('Você venceu')
        rodadas = 0
    else:
        if COP + COM == 9:
            velha == True
            print('Velha')
            rodadas = 0






            
# A  1  |  2  |  3  
# - ----|-----|-----
# B  1  |  2  |  3  
# - ----|-----|-----
# C  1  |  2  |  3  


# velha se soma = 7 ou 56 ou  448 ou 73 ou 146 ou 292 ou 273 ou 84