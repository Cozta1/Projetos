import random

arquivo = open("br-sem-acentos.txt")
linhas = arquivo.readlines()
palavra = ''

while len(palavra) < 5 or len(palavra) > 10:
    sorteio = random.randint(0, len(linhas))
    palavra = linhas[sorteio]
    palavra = palavra.upper().strip()
arquivo.close()

letras_certas = ['_' for letra in palavra]
letras_erradas = []

enforcou = False
acertou = False

erros = 0

print(*letras_certas)

while not enforcou and not acertou:

    chute = input('\nLetra:')
    while  len(chute) > 1:
        chute = input('\nLetra:')
    chute = chute.strip().upper()
    if chute in palavra:
        index = 0
        for letra in palavra:
            if chute == letra:
                letras_certas [index] = letra
            index += 1
            
    else:
        if chute not in letras_erradas:
            letras_erradas.append(chute)
            erros += 1

        print(f'errou! tentativas restantes {7 - erros}\n')
        print('Letras erradas:', *letras_erradas)
    enforcou = erros == 7
    acertou = '_' not in letras_certas

    print(*letras_certas)

if acertou:
    print("Parabéns, você acertou!")
    print(f"A palavra era {palavra}")
else:
    print('\nDERROTA!\n')

    print("Você foi enforcado!")
    print(f"A palavra era {palavra}")