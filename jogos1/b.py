def jogar():

    import random
    import time
    import sys


    print('\n')
    print('|||PEDRA PAPEL TESOURA|||')
    oponente = random.randint(1, 3)
    
    print('\n')

    print('[1] Pedra')
    print('[2] Papel')
    print('[3] Tesoura\n')
    player_str = input('Escolha seu lado: ')
    player = int(player_str)

    if(player < 1 or player > 3):
        print('VALOR INVALIDO, FINALIZANDO!\n')
        sys.exit()


    print('\n')



    if player == 1:
        print('Você escolheu Pedra!\n')

    elif player == 2:
        print('Você escolheu Papel!\n')

    elif player == 3:
        print('Você escolheu Tesoura!\n')

    elif player > 3:
        print('VALOR INVALIDO, FINALIZANDO!\n')
        sys.exit()





    time.sleep(1)


    print('O oponente ainda está escolhendo...')

    time.sleep(2)

    print('O oponente está pronto!')

    time.sleep(1)

    print('PEDRA...')
    time.sleep(1)
    print('PAPEL...')
    time.sleep(1)
    print('TESOURA!')
    time.sleep(1)




    if player == 1 and oponente == 3:
        print('    Você	 Máquina')
        print('                  _    _')
        print('    ____         (_)  / )')
        print('  _/  _ \\         | (_/ ')
        print(' / _ - _ \\       _+/  ')
        print(' \\_______/      //|\\')
        print('                // ||')
        print('               (/  |/ ')
        print('\n')
        print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
        print('   └┐┌┘├┤ ││││  ├┤ │ │')
        print('    └┘ └─┘┘└┘└─┘└─┘└─┘')

    elif player == 2 and oponente == 1:
        print('     Você	 Máquina')
        print('    _____         ____')
        print('   O_____O      _/  _ \\')
        print('   /     /     / _ - _ \\')
        print('  /____ /      \\_______/')
        print(' O_____O')
        print('\n')
        print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
        print('   └┐┌┘├┤ ││││  ├┤ │ │')
        print('    └┘ └─┘┘└┘└─┘└─┘└─┘')

    elif player == 3 and oponente == 2:
        print('     Você	 Máquina')
        print('    _    _')
        print('   (_)  / )       _____')
        print('     | (_/       O_____O')
        print('    _+/          /     /')
        print('   //|\\         /____ /')
        print('  // ||        O_____O')
        print(' (/  |/ ')
        print('\n')
        print('   ┬  ┬┌─┐┌┐┌┌─┐┌─┐┬ ┬')
        print('   └┐┌┘├┤ ││││  ├┤ │ │')
        print('    └┘ └─┘┘└┘└─┘└─┘└─┘')




    if  player == 1 and oponente == 2:
        print('    Você	 Máquina')
        print('    ____	 _____')
        print('  _/  _ \\       O_____O')
        print(' / _ - _ \\      /     /')
        print(' \\_______/     /____ /')
        print('               O_____O')
        print('\n')
        print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
        print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
        print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')

    elif player == 2 and oponente == 3:
        print('     Você	 Máquina')
        print('                  _    _')
        print('    _____        (_)  / )')
        print('   O_____O         | (_/')
        print('   /     /        _+/')
        print('  /____ /        //|\\')
        print(' O_____O        // ||')
        print('               (/  |/')
        print('\n')
        print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
        print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
        print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')

    elif player == 3 and oponente == 1:
        print('     Você	 Máquina')
        print('    _    _')
        print('   (_)  / )       ____')
        print('     | (_/      _/  _ \\')
        print('    _+/        / _ - _ \\')
        print('   //|\\        \\_______/')
        print('  // ||')
        print(' (/  |/ ')
        print('\n')
        print('   ┌─┐┌─┐┬─┐┌┬┐┌─┐┬ ┬ ')
        print('   ├─┘├┤ ├┬┘ ││├┤ │ │ ')
        print('   ┴  └─┘┴└──┴┘└─┘└─┘ ')




    if  player == 1 and oponente == 1:
        print('    Você	Máquina')
        print('    ____	 ____')
        print('  _/  _ \\      _/    \\')
        print(' / _ - _ \\    / _ - _ \\')
        print(' \\_______/    \\_______/ ')
        print('\n')
        print('   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐ ')
        print('   ├┤ │││├─┘├─┤ │ ├┤  ')
        print('   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘ ')

    elif player == 2 and oponente == 2:
        print('    Você	Máquina')
        print('    _____         _____')
        print('   O_____O       O_____O')
        print('   /     /       /     /')
        print('  /____ /       /____ /')
        print(' O_____O       O_____O')
        print('\n')
        print('   ┌─┐┌┬┐┌─┐┌─┐┌┬┐┌─┐')
        print('   ├┤ │││├─┘├─┤ │ ├┤  ')
        print('   └─┘┴ ┴┴  ┴ ┴ ┴ └─┘')

    elif player == 3 and oponente == 3:
        print('     Você	 Máquina')
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


if(__name__ == '__main__'):
    jogar()
