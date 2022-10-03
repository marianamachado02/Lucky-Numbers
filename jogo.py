import random
import os

from logica_jogo import *



#Definir variaveis globais
global saco, lista_jogador, lista_bot, mesa
saco=[]
lista_jogador=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista_bot=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mesa=[]


global tabela_jogador, tabela_bot
tabela_jogador={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0}

tabela_bot={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0}

#Definir valores inicias das diagonais
    #do jogador
diagonais(tabela_jogador, lista_jogador, saco)
    #do bot
diagonais(tabela_bot,lista_bot, saco)

saco = lista_jogador + lista_bot

def jogar():

    print('Insira o nome do jogador:')
    nome_do_jogador=str(input('Nome:'))

    #Define quem joga primeiro
    vez=random.randint(1,2)
    if vez==1:
        print(nome_do_jogador, 'vai jogar primeiro')
        #Enquanto houver 0 no tabuleiro, o jogo continua
        while contar(tabela_jogador)!=0 or contar(tabela_bot)!=0:
            print('Mesa:',mesa)
            print('\n\nTabuleiro jogador:', printar(tabela_jogador))
            jogar_jogador(saco, tabela_jogador,mesa)
            print('\n\nTabuleiro jogador:', printar(tabela_jogador))
            print('\n\nTabuleiro bot:', printar(tabela_bot),'\n\n')
            bot_jogar(mesa,saco,tabela_bot)
            print('\n\nTabuleiro bot:', printar(tabela_bot),'\n\n')
            guardar(saco, tabela_jogador, tabela_bot, mesa)
            os.system('pause')
            os.system('cls')

        if contar(tabela_jogador)==0:
            print('Jogador Ganhou!!!')

        elif contar(tabela_bot)==0:
            print('O bot ganhou :(')

    if vez==2:
        print('O bot vai jogar primeiro')
        while contar(tabela_jogador)!=0 or contar(tabela_bot)!=0:
            print('Mesa:',mesa)
            print('\n\nTabuleiro bot:', printar(tabela_bot))
            bot_jogar(mesa,saco,tabela_bot)
            print('\n\nTabuleiro bot:', printar(tabela_bot))
            print('\n\nTabuleiro jogador:', printar(tabela_jogador))
            jogar_jogador(saco,tabela_jogador,mesa)
            print('\n\nTabuleiro jogador:', printar(tabela_jogador))
            guardar(saco, tabela_jogador, tabela_bot, mesa)
            os.system('pause')
            os.system('cls')

jogar()
