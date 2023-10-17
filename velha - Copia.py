from random import *

campos = [1, 2, 4, 8, 16, 32, 64, 128, 256]
casas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

rodadas = 9

soma_jogador = 0
soma_maquina = 0

velha = False
vitoria = False
derrota = False


#jogador#


while rodadas > 0 and not velha and not vitoria and not derrota:
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')

    jogada_jogador = int(input('Digite uma casa: '))


    while jogada_jogador > 9 and jogada_jogador < 1:

        

        print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
        print('-----|-----|-----')
        print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
        print('-----|-----|-----')
        print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
        jogada_jogador = int(input('Digite uma casa: '))
        
    casa_jogada_j = jogada_jogador - 1


    soma_jogador = soma_jogador + int(campos[casa_jogada_j])


    casas[casa_jogada_j] = 'X'
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  \n')
    ###########

    print('A maquina jogou: ')

    #maquina#
    jogada_maquina = randint(1,10)
    

    casa_jogada_m = jogada_maquina - 1


    # while casaM.__contains__('X') and casaM.__contains__('O'):
    #     jogada_maquina = randint(1,10)


    soma_maquina = soma_maquina + int(campos[casa_jogada_m])
  

    casas[casa_jogada_m] = 'O'





#   1  |  2  |  4  
# -----|-----|-----
#   8  |  16  |  32  
# -----|-----|-----
#   64  |  128  |  256  


# velha se soma = 7 ou 56 ou  448 ou 73 ou 146 ou 292 ou 273 ou 84