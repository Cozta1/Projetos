def jogar():

    print('$$$$$$$$$$$$$$$')
    print('jogo da forca!')
    print('$$$$$$$$$$$$$$$\n')

    arquivo = open('palavras.txt', 'r')
    palavras = []


    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    from random import randint
    numero = randint(0, len(palavras))
    palavra = palavras[numero].upper()

    letras_certas = ['_' for letra in palavra]

    enforcou = False
    acertou = False

    erros = 0

    print(letras_certas)

    while(not enforcou and not acertou):

        chute = input('\nLetra:')
        chute = chute.strip().upper()
        if(chute in palavra):
            index = 0
            for letra in palavra:
                if(chute == letra):
                    letras_certas [index] = letra
                index += 1
        else:
            erros += 1
            print("  _______     ")
            print(" |/      |    ")

            if (erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if (erros == 2):
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")

            if (erros == 3):
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if (erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if (erros == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if (erros == 6):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if (erros == 7):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

            print(" |            ")
            print("_|___         ")

            print('errou! tentativas restantes {}'.format(7 - erros))

        enforcou = erros == 7
        acertou = '_' not in letras_certas

        print(letras_certas)

    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print('\nDERROTA!\n')

        print("Você foi enforcado!")
        print("A palavra era {}".format(palavra))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    print('Fim de jogo')

if(__name__ == '__main__'):
    jogar()