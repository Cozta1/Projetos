from tkinter import messagebox, Tk, Label, Entry, Button
from tkinter import ttk
import tkinter as tk

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



if __name__ == '__main__':
    window = Tk()
    window.title("JOGOS")

    window_width = 600
    window_height = 400
    window.resizable(False, False)

    # get the screen dimension
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    label = ttk.Label(window)
    label['text'] = 'Hi, there'
    label.pack()

    def select(option):
        print(option)


    ttk.Button(window, text='Rock', command=lambda: select('Rock')).pack()
    ttk.Button(window, text='Paper',command=lambda: select('Paper')).pack()
    ttk.Button(window, text='Scissors', command=lambda: select('Scissors')).pack()



    window.mainloop()









