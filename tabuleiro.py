from tkinter import *
import random
import tkinter.messagebox

janela=Tk()
janela.title("Lucky Numbers") 
janela.iconbitmap('imagens/icon.ico')
janela.configure(bg='#b5cffe')
janela.geometry('1000x600')

verde_de_1= PhotoImage(file='imagens/1_de_verde.png')
verde_de_2= PhotoImage(file='imagens/2_de_verde.png')
verde_de_3 = PhotoImage(file='imagens/3_de_verde.png')
verde_de_4 = PhotoImage(file='imagens/4_de_verde.png')
verde_de_5= PhotoImage(file='imagens/5_de_verde.png')
verde_de_6= PhotoImage(file='imagens/6_de_verde.png')
verde_de_7= PhotoImage(file='imagens/7_de_verde.png')
verde_de_8= PhotoImage(file='imagens/8_de_verde.png')
verde_de_9= PhotoImage(file='imagens/9_de_verde.png')
verde_de_10= PhotoImage(file='imagens/10_de_verde.png')
verde_de_11= PhotoImage(file='imagens/11_de_verde.png')
verde_de_12= PhotoImage(file='imagens/12_de_verde.png')
verde_de_13= PhotoImage(file='imagens/13_de_verde.png')
verde_de_14= PhotoImage(file='imagens/14_de_verde.png')
verde_de_15= PhotoImage(file='imagens/15_de_verde.png')
verde_de_16= PhotoImage(file='imagens/16_de_verde.png')
verde_de_17= PhotoImage(file='imagens/17_de_verde.png')
verde_de_18= PhotoImage(file='imagens/18_de_verde.png')
verde_de_19= PhotoImage(file='imagens/19_de_verde.png')
verde_de_20= PhotoImage(file='imagens/20_de_verde.png')

vermelho_de_1= PhotoImage(file='imagens/1_de_vermelho.png')
vermelho_de_2= PhotoImage(file='imagens/2_de_vermelho.png')
vermelho_de_3= PhotoImage(file='imagens/3_de_vermelho.png')
vermelho_de_4= PhotoImage(file='imagens/4_de_vermelho.png')
vermelho_de_5= PhotoImage(file='imagens/5_de_vermelho.png')
vermelho_de_6= PhotoImage(file='imagens/6_de_vermelho.png')
vermelho_de_7= PhotoImage(file='imagens/7_de_vermelho.png')
vermelho_de_8= PhotoImage(file='imagens/8_de_vermelho.png')
vermelho_de_9= PhotoImage(file='imagens/9_de_vermelho.png')
vermelho_de_10= PhotoImage(file='imagens/10_de_vermelho.png')
vermelho_de_11= PhotoImage(file='imagens/11_de_vermelho.png')
vermelho_de_12= PhotoImage(file='imagens/12_de_vermelho.png')
vermelho_de_13= PhotoImage(file='imagens/13_de_vermelho.png')
vermelho_de_14= PhotoImage(file='imagens/14_de_vermelho.png')
vermelho_de_15= PhotoImage(file='imagens/15_de_vermelho.png')
vermelho_de_16= PhotoImage(file='imagens/16_de_vermelho.png')
vermelho_de_17= PhotoImage(file='imagens/17_de_vermelho.png')
vermelho_de_18= PhotoImage(file='imagens/18_de_vermelho.png')
vermelho_de_19= PhotoImage(file='imagens/19_de_vermelho.png')
vermelho_de_20= PhotoImage(file='imagens/20_de_vermelho.png')

global trevos , jogador, bot
trevos=[verde_de_1,verde_de_2,verde_de_3,verde_de_4,verde_de_5,verde_de_6,verde_de_7,verde_de_8,verde_de_9,verde_de_10,verde_de_11,verde_de_12,verde_de_13,verde_de_14,verde_de_15,verde_de_16,verde_de_17,verde_de_18,verde_de_19,verde_de_20,vermelho_de_1,vermelho_de_2,vermelho_de_3,vermelho_de_4,vermelho_de_5,vermelho_de_6,vermelho_de_7,vermelho_de_8,vermelho_de_9,vermelho_de_10,vermelho_de_11,vermelho_de_12,vermelho_de_13,vermelho_de_14,vermelho_de_15,vermelho_de_16,vermelho_de_17,vermelho_de_18,vermelho_de_19,vermelho_de_20]
jogador=[]
bot=[]

# Em vez de escrever a lista, poderiamos fazer:
#     cor=["vermelho", "verde"]
#     trevos=range(1,20)
#     # Isto define duas cores dos trevos e os valores

#     global area 
#     area=[]

#     for x in cor:
#         for y in trevos:
#             area.append(f'{x}_de_{y}')


click=True
count=0

botao_1=StringVar()
botao_2=StringVar()
botao_3=StringVar()
botao_4=StringVar()
botao_5=StringVar()
botao_6=StringVar()
botao_7=StringVar()
botao_8=StringVar()
botao_9=StringVar()
botao_10=StringVar()
botao_11=StringVar()
botao_12=StringVar()
botao_13=StringVar()
botao_14=StringVar()
botao_15=StringVar()
botao_16=StringVar()

def trevo_jogador():
    #escolha trevo
    trevo_escolhido=random.choice(trevos)
        #tirar trevo
    trevos.remove(trevo_escolhido)
        #adicionar ao jogador
    jogador.append(trevo_escolhido)
        
    return trevo_escolhido

def press(r,c):
    global click,count
    if click == True:
        labelPhoto = Label(janela, image=trevo_jogador(), width=100, height=100,bg='#b5cffe')
        labelPhoto.grid(row=r, column=c)
             

def tabuleiros():
        botao1=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b5cffe', textvariable=botao_1, command=lambda:press(2,1))
        botao2=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b7cffe', textvariable=botao_2, command=lambda:press(2,2))
        botao3=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b5cffe', textvariable=botao_3, command=lambda:press(2,3))
        botao4=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b1cffe', textvariable=botao_4, command=lambda:press(2,4))
        botao5=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b4cffe', textvariable=botao_5, command=lambda:press(3,1))
        botao6=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b5cffe', textvariable=botao_6, command=lambda:press(3,2))
        botao7=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b7cffe', textvariable=botao_7, command=lambda:press(3,3))
        botao8=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b5cffe', textvariable=botao_8, command=lambda:press(3,4))
        botao9=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b1cffe', textvariable=botao_9, command=lambda:press(4,1))
        botao10=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b4cffe', textvariable=botao_10, command=lambda:press(4,2))
        botao11=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b5cffe', textvariable=botao_11, command=lambda:press(4,3))
        botao12=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b7cffe', textvariable=botao_12, command=lambda:press(4,4))
        botao13=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b5cffe', textvariable=botao_13, command=lambda:press(5,1))
        botao14=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b1cffe', textvariable=botao_14, command=lambda:press(5,2))
        botao15=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b7cffe', textvariable=botao_15, command=lambda:press(5,3))
        botao16=Button(janela,height=9,width=19,bd=.5,relief='ridge',bg='#b5cffe', textvariable=botao_16, command=lambda:press(5,4))

        botao1.grid(row=2, column=1)
        botao2.grid(row=2, column=2)
        botao3.grid(row=2, column=3)
        botao4.grid(row=2, column=4)
        botao5.grid(row=3, column=1)
        botao6.grid(row=3, column=2)
        botao7.grid(row=3, column=3)
        botao8.grid(row=3, column=4)
        botao9.grid(row=4, column=1)
        botao10.grid(row=4, column=2)
        botao11.grid(row=4, column=3)
        botao12.grid(row=4, column=4)
        botao13.grid(row=5, column=1)
        botao14.grid(row=5, column=2)
        botao15.grid(row=5, column=3)
        botao16.grid(row=5, column=4)

        
saco= Button(janela, command=trevo_jogador)
saco.grid(row=0, column=1)

tabuleiros()

janela.mainloop()