rodadas = 9

vitoria1 = False
vitoria2 = False
velha = False


campos = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

casas_ocupadas = []

casas = [1, 2, 3, 4, 5, 6, 7, 8, 9]


while vitoria1 == False and vitoria2 == False and velha == False and rodadas > 0:
    
    print(f'\nRodadas restantes: {rodadas}')
    
    print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
    print('-----|-----|-----')
    print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
    print('-----|-----|-----')
    print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')

    jogador1 = int(input('Digite uma casa: '))
    
    while jogador1 not in casas or jogador1 < 1 or jogador1 > 9:
        
        print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
        print('-----|-----|-----')
        print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
        print('-----|-----|-----')
        print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
        
        jogador1 = int(input('Digite uma casa: '))
        
        
    
    if jogador1 == 1:
        campos[0][0] = 1
    else:
        if jogador1 == 2:
            campos[0][1] = 1
        else:
            if jogador1 == 3:
                campos[0][2] = 1
                
            else:
                if jogador1 == 4:
                    campos[1][0] = 1
                else:
                    if jogador1 == 5:
                        campos[1][1] = 1
                    else:
                        if jogador1 == 6:
                            campos[1][2] = 1
                        else:
                            if jogador1 == 7:
                                campos[2][0] = 1
                            else:
                                if jogador1 == 8:
                                    campos[2][1] = 1
                                else:
                                    if jogador1 == 9:
                                        campos[2][2] = 1
    
    
    casas_ocupadas.append(casas[jogador1 - 1])            
    casas[jogador1 - 1] = 'X'
    
    
    for i in range(3):
        soma = campos[i][0] + campos[i][1] + campos[i][2]
        if soma == 3:
            vitoria1 = True
        else:
            if soma == -3:
                vitoria2 = True
        
        
    for i in range(3):
        soma = campos[0][i] + campos[1][i] + campos[2][i]
        if soma == 3:
            vitoria1 = True
        else:
            if soma == -3:
                vitoria2 = True
        
        
    diagonal1 = campos[0][0] + campos[1][1] + campos[2][2]
    diagonal2 = campos[0][2] + campos[1][1] + campos[2][0]
    if diagonal1 == 3 or diagonal2 == 3:
        vitoria1 = True
    else:
        if diagonal1 == -1 or diagonal2 == -3:
            vitoria2 = True
        
    rodadas -= 1
    
    
    
    if vitoria1 == True:
        print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
        print('-----|-----|-----')
        print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
        print('-----|-----|-----')
        print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
        
        print('Jogador 1 Ganhou!')
    else:
        if vitoria2 == True:
            print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
            print('-----|-----|-----')
            print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
            print('-----|-----|-----')
            print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
        
            print('Jogador 2 Ganhou!')
            
        else:
            if rodadas == 0:
                velha = True
                print('Velha, sem ganhador')
                
            
            
            
#################################################################################################################
    
    
    
    if vitoria1 == True:
        print('\n')
    else:
        
        print(f'\nRodadas restantes: {rodadas}')
        
        print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
        print('-----|-----|-----')
        print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
        print('-----|-----|-----')
        print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')

        jogador2 = int(input('Digite uma casa: '))
        
        while jogador2 not in casas or jogador2 < 1 or jogador2 > 9:
            
            print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
            print('-----|-----|-----')
            print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
            print('-----|-----|-----')
            print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
            
            jogador2 = int(input('Digite uma casa: '))
            
            
        
        if jogador2 == 1:
            campos[0][0] = -1
        else:
            if jogador2 == 2:
                campos[0][1] = -1
            else:
                if jogador2 == 3:
                    campos[0][2] = -1
                    
                else:
                    if jogador2 == 4:
                        campos[1][0] = -1
                    else:
                        if jogador2 == 5:
                            campos[1][1] = -1
                        else:
                            if jogador2 == 6:
                                campos[1][2] = -1
                            else:
                                if jogador2 == 7:
                                    campos[2][0] = -1
                                else:
                                    if jogador2 == 8:
                                        campos[2][1] = -1
                                    else:
                                        if jogador2 == 9:
                                            campos[2][2] = -1
        
        
        casas_ocupadas.append(casas[jogador2 - 1])            
        casas[jogador2 - 1] = 'O'
        
        
        for i in range(3):
            soma = campos[i][0] + campos[i][1] + campos[i][2]
            if soma == 3:
                vitoria1 = True
            else:
                if soma == -3:
                    vitoria2 = True
            
            
        for i in range(3):
            soma = campos[0][i] + campos[1][i] + campos[2][i]
            if soma == 3:
                vitoria1 = True
            else:
                if soma == -3:
                    vitoria2 = True
            
            
        diagonal1 = campos[0][0] + campos[1][1] + campos[2][2]
        diagonal2 = campos[0][2] + campos[1][1] + campos[2][0]
        if diagonal1 == 3 or diagonal2 == 3:
            vitoria1 = True
        else:
            if diagonal1 == -1 or diagonal2 == -3:
                vitoria2 = True
            
        rodadas -= 1
        
        
        
        if vitoria1 == True:
            print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
            print('-----|-----|-----')
            print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
            print('-----|-----|-----')
            print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
            
            print('Jogador 1 Ganhou!')
        else:
            if vitoria2 == True:
                print(f'\n  {casas[0]}  |  {casas[1]}  |  {casas[2]}  ')
                print('-----|-----|-----')
                print(f'  {casas[3]}  |  {casas[4]}  |  {casas[5]}  ')
                print('-----|-----|-----')
                print(f'  {casas[6]}  |  {casas[7]}  |  {casas[8]}  ')
            
                print('Jogador 2 Ganhou!')
                
            else:
                if rodadas == 0:
                    velha = True
                    print('Velha, sem ganhador')
            