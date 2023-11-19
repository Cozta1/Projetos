import random

print('\n')
print('|||PEDRA PAPEL TESOURA|||\n')


print('[1] PvP')
print('[2] Player Vs IA\n')
modo = int(input('Escolha o modo de jogo: '))

print('[1] Pedra')
print('[2] Papel')
print('[3] Tesoura\n')
player = int(input('Escolha seu lado: '))


if modo == 1:
    
    print('[1] Pedra')
    print('[2] Papel')
    print('[3] Tesoura\n')
    oponente = int(input('Jogador 1 escolha seu lado: '))

    print('\n')
        
    if player < 1 or player > 3:
        print('VALOR INVALIDO, FINALIZANDO!\n') 
    else:
            
        if player == 1:
            print('Você escolheu Pedra!\n')
        else:
            if player == 2:
                print('Você escolheu Papel!\n')
            else:
                if player == 3:
                    print('Você escolheu Tesoura!\n')


    if player == 1 and oponente == 3:
        print('    Jogador 1	 Jogador 2')
        print('                  _    _')
        print('    ____         (_)  / )')
        print('  _/  _ \\         | (_/ ')
        print(' / _ - _ \\       _+/  ')
        print(' \\_______/      //|\\')
        print('                // ||')
        print('               (/  |/ ')
        print('\n')
        print('        Jogador 1     ')
        print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
        print('   └┐┌┘├┤ ││││  ├┤ │ │')
        print('    └┘ └─┘┘└┘└─┘└─┘└─┘')

    if player == 2 and oponente == 1:
        print('     Jogador 1	 Jogador 2')
        print('    _____         ____')
        print('   O_____O      _/  _ \\')
        print('   /     /     / _ - _ \\')
        print('  /____ /      \\_______/')
        print(' O_____O')
        print('\n')
        print('        Jogador 1     ')
        print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
        print('   └┐┌┘├┤ ││││  ├┤ │ │')
        print('    └┘ └─┘┘└┘└─┘└─┘└─┘')

    if player == 3 and oponente == 2:
        print('     Jogador 1	 Jogador 2')
        print('    _    _')
        print('   (_)  / )       _____')
        print('     | (_/       O_____O')
        print('    _+/          /     /')
        print('   //|\\         /____ /')
        print('  // ||        O_____O')
        print(' (/  |/ ')
        print('\n')
        print('        Jogador 1     ')
        print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
        print('   └┐┌┘├┤ ││││  ├┤ │ │')
        print('    └┘ └─┘┘└┘└─┘└─┘└─┘')

    if  player == 1 and oponente == 2:
        print('    Jogador 1	 Jogador 2')
        print('    ____	 _____')
        print('  _/  _ \\       O_____O')
        print(' / _ - _ \\      /     /')
        print(' \\_______/     /____ /')
        print('               O_____O')
        print('\n')
        print('        Jogador 2     ')
        print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
        print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
        print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')

    if player == 2 and oponente == 3:
        print('     Jogador 1	 Jogador 2')
        print('                  _    _')
        print('    _____        (_)  / )')
        print('   O_____O         | (_/')
        print('   /     /        _+/')
        print('  /____ /        //|\\')
        print(' O_____O        // ||')
        print('               (/  |/')
        print('\n')
        print('        Jogador 2     ')
        print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
        print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
        print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')

    if player == 3 and oponente == 1:
        print('     Jogador 1	 Jogador 2')
        print('    _    _')
        print('   (_)  / )       ____')
        print('     | (_/      _/  _ \\')
        print('    _+/        / _ - _ \\')
        print('   //|\\        \\_______/')
        print('  // ||')
        print(' (/  |/ ')
        print('\n')
        print('        Jogador 2     ')
        print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
        print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
        print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')

    if  player == 1 and oponente == 1:
        print('    Jogador 1	Jogador 2')
        print('    ____	 ____')
        print('  _/  _ \\      _/    \\')
        print(' / _ - _ \\    / _ - _ \\')
        print(' \\_______/    \\_______/ ')
        print('\n')
        print('   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐ ')
        print('   ├┤ │││├─┘├─┤ │ ├┤  ')
        print('   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ ')

    if player == 2 and oponente == 2:
        print('    Jogador 1	Jogador 2')
        print('    _____         _____')
        print('   O_____O       O_____O')
        print('   /     /       /     /')
        print('  /____ /       /____ /')
        print(' O_____O       O_____O')
        print('\n')
        print('   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐')
        print('   ├┤ │││├─┘├─┤ │ ├┤  ')
        print('   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘')

    if player == 3 and oponente == 3:
            print('     Jogador 1	 Jogador 2')
            print('    _    _       _    _')
            print('   (_)  / )     (_)  / )')
            print('     | (_/        | (_/')
            print('    _+/          _+/')
            print('   //|\\         //|\\')
            print('  // ||        // ||')
            print(' (/  |/       (/  |/')
            print('\n')
            print('   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐')
            print('   ├┤ │││├─┘├─┤ │ ├┤  ')
            print('   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘')
                
else:
    if modo == 2:
        oponente = random.randint(1, 3)

        if player < 1 or player > 3:
            print('VALOR INVALIDO, FINALIZANDO!\n') 
        else:
                
            if player == 1:
                print('Você escolheu Pedra!\n')
            else:
                if player == 2:
                    print('Você escolheu Papel!\n')
                else:
                    if player == 3:
                        print('Você escolheu Tesoura!\n')


        if player == 1 and oponente == 3:
            print('    Jogador 1	 Jogador 2')
            print('                  _    _')
            print('    ____         (_)  / )')
            print('  _/  _ \\         | (_/ ')
            print(' / _ - _ \\       _+/  ')
            print(' \\_______/      //|\\')
            print('                // ||')
            print('               (/  |/ ')
            print('\n')
            print('        Jogador 1     ')
            print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
            print('   └┐┌┘├┤ ││││  ├┤ │ │')
            print('    └┘ └─┘┘└┘└─┘└─┘└─┘')

        if player == 2 and oponente == 1:
            print('     Jogador 1	 Jogador 2')
            print('    _____         ____')
            print('   O_____O      _/  _ \\')
            print('   /     /     / _ - _ \\')
            print('  /____ /      \\_______/')
            print(' O_____O')
            print('\n')
            print('        Jogador 1     ')
            print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
            print('   └┐┌┘├┤ ││││  ├┤ │ │')
            print('    └┘ └─┘┘└┘└─┘└─┘└─┘')

        if player == 3 and oponente == 2:
            print('     Jogador 1	 Jogador 2')
            print('    _    _')
            print('   (_)  / )       _____')
            print('     | (_/       O_____O')
            print('    _+/          /     /')
            print('   //|\\         /____ /')
            print('  // ||        O_____O')
            print(' (/  |/ ')
            print('\n')
            print('        Jogador 1     ')
            print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
            print('   └┐┌┘├┤ ││││  ├┤ │ │')
            print('    └┘ └─┘┘└┘└─┘└─┘└─┘')

        if  player == 1 and oponente == 2:
            print('    Jogador 1	 Jogador 2')
            print('    ____	 _____')
            print('  _/  _ \\       O_____O')
            print(' / _ - _ \\      /     /')
            print(' \\_______/     /____ /')
            print('               O_____O')
            print('\n')
            print('        Jogador 2     ')
            print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
            print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
            print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')

        if player == 2 and oponente == 3:
            print('     Jogador 1	 Jogador 2')
            print('                  _    _')
            print('    _____        (_)  / )')
            print('   O_____O         | (_/')
            print('   /     /        _+/')
            print('  /____ /        //|\\')
            print(' O_____O        // ||')
            print('               (/  |/')
            print('\n')
            print('        Jogador 2     ')
            print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
            print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
            print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')

        if player == 3 and oponente == 1:
            print('     Jogador 1	 Jogador 2')
            print('    _    _')
            print('   (_)  / )       ____')
            print('     | (_/      _/  _ \\')
            print('    _+/        / _ - _ \\')
            print('   //|\\        \\_______/')
            print('  // ||')
            print(' (/  |/ ')
            print('\n')
            print('        Jogador 2     ')
            print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
            print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
            print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')

        if  player == 1 and oponente == 1:
            print('    Jogador 1	Jogador 2')
            print('    ____	 ____')
            print('  _/  _ \\      _/    \\')
            print(' / _ - _ \\    / _ - _ \\')
            print(' \\_______/    \\_______/ ')
            print('\n')
            print('   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐ ')
            print('   ├┤ │││├─┘├─┤ │ ├┤  ')
            print('   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ ')

        if player == 2 and oponente == 2:
            print('    Jogador 1	Jogador 2')
            print('    _____         _____')
            print('   O_____O       O_____O')
            print('   /     /       /     /')
            print('  /____ /       /____ /')
            print(' O_____O       O_____O')
            print('\n')
            print('   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐')
            print('   ├┤ │││├─┘├─┤ │ ├┤  ')
            print('   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘')

        if player == 3 and oponente == 3:
            
            print('     Jogador 1	 Jogador 2')
            print('    _    _       _    _')
            print('   (_)  / )     (_)  / )')
            print('     | (_/        | (_/')
            print('    _+/          _+/')
            print('   //|\\         //|\\')
            print('  // ||        // ||')
            print(' (/  |/       (/  |/')
            print('\n')
            print('   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐')
            print('   ├┤ │││├─┘├─┤ │ ├┤  ')
            print('   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘')
    else:
        print('Modo inválido')
