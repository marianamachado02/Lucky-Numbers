from tkinter import *
import tkinter.font as font
from turtle import bgcolor
from PIL import ImageTk, Image
import random
import tkinter.messagebox


#Configurar a janela
janela = Tk()
janela.title("imagens/Lucky Numbers") 
janela.iconbitmap('imagens/icon.ico')
janela.configure(bg='#b5cffe')
janela.geometry('1000x600')

def limpar_ecra(janela):
    for widget in janela.winfo_children():
        widget.destroy()

def Menu_jogo():
    limpar_ecra(janela)
    menu_font = font.Font(family='04b')
    texto_menu = Label(janela, text='MENU:', font=("04b", 40), fg='#156435', bg='#b5cffe')
    texto_menu.place(x=400, y=100)
    texto_A = Label(janela, text='A:    Jogar uma Partida;', font=("arial", 10), bg='#b5cffe')
    texto_A.place(x=350, y=215)
    texto_B = Label(janela, text='B:    Carregar uma partida a partir de um ficheiro;', font=("arial", 10), bg='#b5cffe')
    texto_B.place(x=350, y=245)
    texto_C = Label(janela, text='C:    Apresentar uma descrição do jogo;', font=("arial", 10),bg='#b5cffe')
    texto_C.place(x=350, y=275)
    texto_D= Label(janela, text='D:     Sair da aplicação.', font=("arial", 10), bg='#b5cffe')
    texto_D.place(x=350, y=305)

    botao_A= Button(janela, text='A', font=("arial", 10), bg='#b5cffe', command=exit)
    botao_A.place(x=350, y=210)
    botao_B= Button(janela,text='B', font=("arial", 10),bg='#b5cffe', command=exit)
    botao_B.place(x=350, y=240)
    Botao_C= Button(janela, text='C', font=("arial", 10),bg='#b5cffe', command=exit)
    Botao_C.place(x=350, y=270)
    Botao_D= Button(janela, text='D', font=("arial", 10),bg='#b5cffe', command=exit)
    Botao_D.place(x=350, y=300)

imagem = PhotoImage(file=('imagens/Lucky-logo.png')) 
img= Label(image=imagem, bg='#b5cffe')
img.place(x=100, y=5)
botao= Button(janela, text='START', font=("arial", 10, font.BOLD), command=Menu_jogo())
botao.place(x=440, y=500)

janela.mainloop()