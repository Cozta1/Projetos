from random import *

campos = [['A1', 'B2', 'C3'],
          ['A1', 'B2', 'C3'],
          ['A1', 'B2', 'C3']]

  
casas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# COP = [] #casas_ocupadas_jogador
# COM = [] #casas_ocupadas_maquina

rodadas = 9


velha = False
vitoria = False
derrota = False

def vitoria():
     
    for i in range(3):
        soma = campos[i][0] + campos[i][1] + campos[i][2]
        if soma == 3 or soma == -3:
            return 1
        
    for i in range(3):
        soma = campos[0][i] + campos[1][i] + campos[2][i]
        if soma == 3 or soma == -3:
            return 1
        
    diagonal1 = campos[0][0] + campos[1][1] + campos[2][2]
    diagonal2 = campos[0][2] + campos[1][1] + campos[2][0]
    if diagonal1 == 3 or diagonal1 == -1 or diagonal2 == 3 or diagonal2 == -3:
        return 1
    return 0
#jogador#


while vitoria() == 0:
        
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')

    jogador1 = int(input('Digite uma casa: '))


    
    while jogador1 > 9 and jogador1 < 1 and jogador1 in casas_ocupadas:

        

        print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
        print('-----|-----|-----')
        print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
        print('-----|-----|-----')
        print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
        jogador1 = int(input('Digite uma casa: '))
        
    while jogador1 not in casas or jogador1 < 1 or jogador1 > 9:
            jogador1 = int(input('Digite uma casa: '))
            

    
    
    



    casas[jogador1 - 1] = 1
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  \n')
    ###########


    jogador2 = int(input('Digite uma casa: '))

    while jogador2 > 9 and jogador2 < 1 and jogador2 in casas_ocupadas:

        

        print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
        print('-----|-----|-----')
        print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
        print('-----|-----|-----')
        print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
        jogador2 = int(input('Digite uma casa: '))
        
    while jogador2 not in casas or jogador2 < 1 or jogador2 > 9:
            jogador2 = int(input('Digite uma casa: '))
            
    COP.append(-1)
    
    
    



    casas[jogador2 - 1] = -1
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  \n')





# while rodadas > 0 or not velha and not vitoria and not derrota:
        
#     print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
#     print('-----|-----|-----')
#     print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
#     print('-----|-----|-----')
#     print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')

#     jogador1 = int(input('Digite uma casa: '))


    
#     while jogador1 > 9 and jogador1 < 1 and jogador1 in casas_ocupadas:

        

#         print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
#         print('-----|-----|-----')
#         print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
#         print('-----|-----|-----')
#         print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
#         jogador1 = int(input('Digite uma casa: '))
        
#     while jogador1 not in casas or jogador1 < 1 or jogador1 > 9:
#             jogador1 = int(input('Digite uma casa: '))
            
#     COP.append( 1)
    
    
    



#     casas[jogador1 - 1] = 1
#     print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
#     print('-----|-----|-----')
#     print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
#     print('-----|-----|-----')
#     print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  \n')
#     ###########


#     jogador2 = int(input('Digite uma casa: '))

#     while jogador2 > 9 and jogador2 < 1 and jogador2 in casas_ocupadas:

        

#         print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
#         print('-----|-----|-----')
#         print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
#         print('-----|-----|-----')
#         print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
#         jogador2 = int(input('Digite uma casa: '))
        
#     while jogador2 not in casas or jogador2 < 1 or jogador2 > 9:
#             jogador2 = int(input('Digite uma casa: '))
            
#     COP.append(-1)
    
    
    



#     casas[jogador2 - 1] = -1
#     print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
#     print('-----|-----|-----')
#     print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
#     print('-----|-----|-----')
#     print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  \n')





    





            
# A  1  |  2  |  3  
# - ----|-----|-----
# B  1  |  2  |  3  
# - ----|-----|-----
# C  1  |  2  |  3  


# velha se soma = 7 ou 56 ou  448 ou 73 ou 146 ou 292 ou 273 ou 84