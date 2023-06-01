import forca
import adivinhacao

def escolha_jogo():

    print('$$$$$$$$$$$$$$$$$$$')
    print('ESCOLHA O SEU JOGO!')
    print('$$$$$$$$$$$$$$$$$$$\n')

    print('[1] Adivinhação')
    print('[2] Forca\n')

    jogo = int(input('O jogo escolhido foi:'))

    if(jogo == 1):
        print('\nAbrindo adivinhação\n')
        adivinhacao.jogar()
    elif(jogo == 2):
        print('\nAbrindo forca\n')
        forca.jogar()

if(__name__ == '__main__'):
    escolha_jogo()