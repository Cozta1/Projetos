import forca
import adivinhacao
import pedra_papel_tesoura

def escolha_jogo():

    print('$$$$$$$$$$$$$$$$$$$')
    print('ESCOLHA O SEU JOGO!')
    print('$$$$$$$$$$$$$$$$$$$\n')

    print('[1] Adivinhação')
    print('[2] Forca')
    print('[3] Pedra Papel Tesoura\n')

    jogo = int(input('O jogo escolhido foi:'))

    if(jogo == 1):
        print('\nAbrindo Adivinhação\n')
        adivinhacao.jogar()
    elif(jogo == 2):
        print('\nAbrindo Forca\n')
        forca.jogar()
    elif(jogo == 3):
        print('\nAbrindo Pedra Papel Tesoura\n')
        pedra_papel_tesoura.jogar()

if(__name__ == '__main__'):
    escolha_jogo()