from random import *

campos = [1, 2, 4, 8, 16, 32, 64, 128, 256]
casas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
casas_ocupadas = []

rodadas = 9

soma_jogador = 0
soma_maquina = 0

velha = False
vitoria = False
derrota = False

def teste_velha():
    somas = [7, 56, 448, 73, 146, 292, 273, 84]
    if soma_maquina in somas:
        derrota == True
        print('A maquina venceu')
        rodadas = 0
    else:
        if soma_jogador in somas:
           vitoria == True 
           print('Você venceu')
           rodadas = 0
        else:
            if len(casas_ocupadas) == 9:
                velha == True
                print('Velha')
                rodadas = 0
#jogador#


while rodadas > 0 and not velha and not vitoria and not derrota:
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
            
    casas_ocupadas.append(jogada_jogador)
    
    
    

    soma_jogador = soma_jogador + int(campos[jogada_jogador - 1])


    casas[jogada_jogador - 1] = 'X'
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  \n')
    ###########

    teste_velha()
    
   

    #maquina#
    jogada_maquina = randint(1,10)
    while jogada_maquina not in casas:
        jogada_maquina = randint(1,10)
        
    print(f'A maquina jogou: {jogada_maquina}')
    soma_maquina = soma_maquina + campos[jogada_maquina - 1]
  

    casas[jogada_maquina - 1] = 'O'
    
    teste_velha()






            
#   1  |  2  |  4  
# -----|-----|-----
#   8  |  16  |  32  
# -----|-----|-----
#   64  |  128  |  256  


# velha se soma = 7 ou 56 ou  448 ou 73 ou 146 ou 292 ou 273 ou 84