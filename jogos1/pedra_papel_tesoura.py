def jogo():
    
    import random

    print('\n')
    print('PEDRA PAPEL TESOURA\n')


    print('[1] Pedra')
    print('[2] Papel')
    print('[3] Tesoura\n')
    player = int(input('Faça sua escolha: '))

    while player > 3 or player < 1:
        print('VALOR INVALIDO, TENTE NOVAMENTE!\n') 
        print('[1] Pedra')
        print('[2] Papel')
        print('[3] Tesoura\n')
        player = int(input('Escolha seu lado: '))

        
    if player == 1:
        print('Você escolheu Pedra!\n')
    else:
        if player == 2:
            print('Você escolheu Papel!\n')
        else:
            if player == 3:
                print('Você escolheu Tesoura!\n')
                    
    maquina = random.randint(1, 3)

    if player == 1:
        if maquina == 1:
            print('Jogador	 Maquina')
            print('Pedra  X  Pedra\n')
            print('Empate')
        else:
            if maquina == 2:
                print('Jogador	 Maquina')
                print('Pedra  X  Papel\n')
                print('Maquina venceu')
            else:
                print('Jogador	 Maquina')
                print('Pedra  X  Tesoura\n')
                print('Jogador Venceu')        
    else:   
        if player == 2:
            if maquina == 1:
                print('Jogador	 Maquina')
                print('Papel  X  Pedra\n')
                print('Jogador Venceu') 
            if maquina == 2:
                print('Jogador	 Maquina')
                print('Papel  X  Papel\n')
                print('Empate')
            else:
                print('Jogador	 Maquina')
                print('Papel  X  Tesoura\n')
                print('Maquina venceu')
        else:
            if player == 3:
                if maquina == 1:
                    print('Jogador	 Maquina')
                    print('Tesoura  X  Pedra\n')
                    print('Maquina venceu')
                else:
                    if maquina == 2:
                        print('Jogador	 Maquina')
                        print('Tesoura  X  Papel\n')
                        print('Jogador Venceu')
                    else:
                        print('Jogador	 Maquina')
                        print('Tesoura  X  Tesoura\n')
                        print('Empate')
                        
jogo()



print('\n[1] Sim')
print('[2] Não')
replay = int(input('Jogar Novamente? '))

while replay == 1:
    jogo()
    print('\n[1] Sim')
    print('[2] Não')
    replay = int(input('Jogar Novamente? '))