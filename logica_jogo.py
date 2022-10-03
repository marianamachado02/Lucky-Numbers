import random
from collections import Counter

def contar(tabela):
    #Contar quantos 0 existem na tabela
    vezes= sum(value == 0 for value in tabela.values())
    return vezes

def printar(tabela):
    #Imprimir a tabela:
    print(tabela[1] ,tabela[2]  ,tabela[3]  ,tabela[4],'\n')
    print(tabela[5] ,tabela[6]  ,tabela[7]  ,tabela[8],'\n')
    print(tabela[9] ,tabela[10]  ,tabela[11]  ,tabela[12],'\n')
    print(tabela[13] ,tabela[14]  ,tabela[15]  ,tabela[16],'\n')

def diagonais(tabela, lista, saco):
    #Definir as diagonais
    diagonal_1=random.randint(1,5)
    lista.remove(diagonal_1)
    tabela[1]=diagonal_1

    diagonal_2=random.randint(6,10)
    lista.remove(diagonal_2)
    
    tabela[6]=diagonal_2

    diagonal_3=random.randint(11,15)
    lista.remove(diagonal_3)
    
    tabela[11]=diagonal_3

    diagonal_4=random.randint(16,20)
    lista.remove(diagonal_4)
    
    tabela[16]=diagonal_4

def jogar_tabela(num, tabela, mesa1):
    #Jogar. npc é quem joga, num é o trevo, tabela é o tabela de quem joga e mesa1 é a mesa
    print('Onde deseja colocar o trevo', num)
    posicao=int(input('Posição:'))
    try:
        while (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                print('Erro! Insira uma nova posicao')
                posicao=int(input('Posição:'))
    except:
        if posicao == 5 or posicao ==9:
            if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                print('Erro! Insira uma nova posicao')
        elif posicao == 8 or posicao == 12:
            if (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-2] and tabela[posicao-2]!=0 ) or (num<tabela[posicao-3] and tabela[posicao-3]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0):
                print('Erro! Insira uma nova posicao')
        elif posicao ==1:
            if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0):
                print('Erro! Insira uma nova posicao')
        elif posicao>1 and posicao <=4:
            if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ):
                print('Erro! Insira uma nova posicao')
        elif posicao == 16:
            if (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                print('Erro! Insira uma nova posicao')
        elif posicao > 12:
            if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                print('Erro! Insira uma nova posicao')
    
    try:
        if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
            if tabela[posicao]==0:
                tabela[posicao]=num
                print(printar(tabela))
            elif tabela[posicao]!=0:
                tirar= tabela[posicao]
                
                mesa1.append(tirar)
                tabela[posicao]=num
                print(printar(tabela))
    except:
        if posicao == 5 or posicao == 9:
            if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                if tabela[posicao]==0:
                    tabela[posicao]=num
                    print(printar(tabela))
                elif tabela[posicao]!=0:
                    tirar= tabela[posicao]
                    mesa1.append(tirar)
                    tabela[posicao]=num
                    print(printar(tabela))
        elif posicao == 8 or posicao == 12:
            if (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                if tabela[posicao]==0:
                    tabela[posicao]=num
                    print(printar(tabela))
                elif tabela[posicao]!=0:
                    tirar= tabela[posicao]
                    mesa1.append(tirar)
                    tabela[posicao]=num
                    print(printar(tabela))
        elif posicao == 1:
            if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0):
                if tabela[posicao]==0:
                    tabela[posicao]=num
                    print(printar(tabela))
                elif tabela[posicao]!=0:
                    tirar= tabela[posicao]
                    mesa1.append(tirar)
                    tabela[posicao]=num
                    print(printar(tabela))
        elif posicao>1 and posicao<=4:
            if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ):
                if tabela[posicao]==0:
                    tabela[posicao]=num
                    print(printar(tabela))
                elif tabela[posicao]!=0:
                    tirar= tabela[posicao]
                    mesa1.append(tirar)
                    tabela[posicao]=num
                    print(printar(tabela))
        elif posicao==16:
            if (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                if tabela[posicao]==0:
                    tabela[posicao]=num
                    print(printar(tabela))
                elif tabela[posicao]!=0:
                    tirar= tabela[posicao]
                    
                    mesa1.append(tirar)
                    tabela[posicao]=num
                    print(printar(tabela))
        elif posicao >12:
            if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                if tabela[posicao]==0:
                    tabela[posicao]=num
                    print(printar(tabela))
                elif tabela[posicao]!=0:
                    tirar= tabela[posicao]
                    
                    mesa1.append(tirar)
                    tabela[posicao]=num
                    print(printar(tabela))
        

    return tabela

def jogar_jogador(saco, tabela, mesa):
    #Jogar, saco é o saco, tabela de quem joga, quem joga e mesa
    print('Deseja tirar um trevo do saco ou utilizar um trevo da mesa?\n1-saco\n2-mesa\n3-salvar')
    escolha=int(input(''))

    if escolha==1:
        trevo=random.choice(saco)
        print(trevo)

        print('Deseja inserir o trevo no tabela ou na mesa?\n 1-tabela\n2-mesa')
        escolha_jogo =int(input(''))
        if escolha_jogo ==1:
            jogar_tabela(trevo,tabela, mesa)
        if escolha_jogo ==2:
            mesa.append(trevo)
    elif escolha==2:
        if len(mesa)!=0:
            print(mesa)
            print('Escolha o numero da mesa que quer utilizar:')
            numero=int(input(''))
            
            while numero not in mesa:
                print('Escolha outro numero')
                numero=int(input(''))
            
            mesa.remove(numero)
            jogar_tabela(numero,tabela,mesa)
    elif escolha==3:
        tabela_j = tabela
        file = open('original.txt','w')
        file.write("%s\n" %(saco))
        file.write("%s\n"%(tabela_j))
        file.write("%s"%(mesa))
        file.close()

    else:
        print('Erro! Não existem trevos na mesa.\nTerá de usar um trevo do saco')
        trevo=random.choice(saco)
        print(printar(tabela))
        print(trevo)

        print('Deseja inserir o trevo no tabela ou na mesa?\n 1-tabela\n2-mesa')
        num=int(input(''))
        if num==1:
            jogar_tabela(trevo,tabela,mesa)
        if num==2:
            mesa.append(trevo)

    return tabela
            
def bot_jogar(mesa, saco, tabela):
    escolha=random.randint(1,2)

    if escolha==1:
        if len(mesa)!=0:
            numero=random.choice(mesa)

            posicao=random.randint(1,16)

        try:
            while (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                posicao=random.randint(1,16)
        except:
            if posicao == 5 or posicao ==9:
                if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                    posicao=random.randint(1,16)
            elif posicao == 8 or posicao == 12:
                if (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                    posicao=random.randint(1,16)
            elif posicao ==1:
                if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0):
                    posicao=random.randint(1,16)
            elif posicao>1 and posicao <=4:
                if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ):
                    posicao=random.randint(1,16)
            elif posicao == 16:
                if (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                    posicao=random.randint(1,16)
            elif posicao > 12:
                if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                    pposicao=random.randint(1,16)
        
        try:
            if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                if tabela[posicao]==0:
                    tabela[posicao]=num
                    print(printar(tabela))
                elif tabela[posicao]!=0:
                    tirar= tabela[posicao]
                    mesa.append(tirar)
                    tabela[posicao]=num
                    print(printar(tabela))
        except:
            if posicao == 5 or posicao == 9:
                if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                    if tabela[posicao]==0:
                        tabela[posicao]=num
                        print(printar(tabela))
                    elif tabela[posicao]!=0:
                        tirar= tabela[posicao]
                        mesa.append(tirar)
                        tabela[posicao]=num
                        print(printar(tabela))
            elif posicao == 8 or posicao == 12:
                if (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                    if tabela[posicao]==0:
                        tabela[posicao]=num
                        print(printar(tabela))
                    elif tabela[posicao]!=0:
                        tirar= tabela[posicao]
                        mesa.append(tirar)
                        tabela[posicao]=num
                        print(printar(tabela))
            elif posicao == 1:
                if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0):
                    if tabela[posicao]==0:
                        tabela[posicao]=num
                        print(printar(tabela))
                    elif tabela[posicao]!=0:
                        tirar= tabela[posicao]
                        mesa.append(tirar)
                        tabela[posicao]=num
                        print(printar(tabela))
            elif posicao>1 and posicao<=4:
                if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ):
                    if tabela[posicao]==0:
                        tabela[posicao]=num
                        print(printar(tabela))
                    elif tabela[posicao]!=0:
                        tirar= tabela[posicao]
                        mesa.append(tirar)
                        tabela[posicao]=num
                        print(printar(tabela))
            elif posicao==16:
                if (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                    if tabela[posicao]==0:
                        tabela[posicao]=num
                        print(printar(tabela))
                    elif tabela[posicao]!=0:
                        tirar= tabela[posicao]
                        
                        mesa.append(tirar)
                        tabela[posicao]=num
                        print(printar(tabela))
            elif posicao >12:
                if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                    if tabela[posicao]==0:
                        tabela[posicao]=num
                        print(printar(tabela))
                    elif tabela[posicao]!=0:
                        tirar= tabela[posicao]
                        
                        mesa.append(tirar)
                        tabela[posicao]=num
                        print(printar(tabela))

    if escolha==2:
        trevo=random.choice(saco)
        print(printar(tabela))
        print(trevo)

        num=random.randint(1,2)

        if num==1:
            posicao=random.randint(1,16)

            try:
                while (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                    posicao=random.randint(1,16)
            except:
                if posicao == 5 or posicao ==9:
                    if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                        posicao=random.randint(1,16)
                elif posicao == 8 or posicao == 12:
                    if (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                        posicao=random.randint(1,16)
                elif posicao ==1:
                    if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0):
                        posicao=random.randint(1,16)
                elif posicao>1 and posicao <=4:
                    if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num>tabela[posicao+4] and tabela[posicao+4]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ):
                        posicao=random.randint(1,16)
                elif posicao == 16:
                    if (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                        posicao=random.randint(1,16)
                elif posicao > 12:
                    if (num>tabela[posicao+1] and tabela[posicao+1]!=0 ) or (num<tabela[posicao-1] and tabela[posicao-1]!=0 ) or (num<tabela[posicao-4] and tabela[posicao-4]!=0 ):
                        pposicao=random.randint(1,16)
            
            try:
                if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                    if tabela[posicao]==0:
                        tabela[posicao]=num
                        print(printar(tabela))
                    elif tabela[posicao]!=0:
                        tirar= tabela[posicao]
                        mesa.append(tirar)
                        tabela[posicao]=num
                        print(printar(tabela))
            except:
                if posicao == 5 or posicao == 9:
                    if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                        if tabela[posicao]==0:
                            tabela[posicao]=num
                            print(printar(tabela))
                        elif tabela[posicao]!=0:
                            tirar= tabela[posicao]
                            mesa.append(tirar)
                            tabela[posicao]=num
                            print(printar(tabela))
                elif posicao == 8 or posicao == 12:
                    if (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                        if tabela[posicao]==0:
                            tabela[posicao]=num
                            print(printar(tabela))
                        elif tabela[posicao]!=0:
                            tirar= tabela[posicao]
                            mesa.append(tirar)
                            tabela[posicao]=num
                            print(printar(tabela))
                elif posicao == 1:
                    if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0):
                        if tabela[posicao]==0:
                            tabela[posicao]=num
                            print(printar(tabela))
                        elif tabela[posicao]!=0:
                            tirar= tabela[posicao]
                            mesa.append(tirar)
                            tabela[posicao]=num
                            print(printar(tabela))
                elif posicao>1 and posicao<=4:
                    if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num<tabela[posicao+4] or tabela[posicao+4]==0) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ):
                        if tabela[posicao]==0:
                            tabela[posicao]=num
                            print(printar(tabela))
                        elif tabela[posicao]!=0:
                            tirar= tabela[posicao]
                            mesa.append(tirar)
                            tabela[posicao]=num
                            print(printar(tabela))
                elif posicao==16:
                    if (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                        if tabela[posicao]==0:
                            tabela[posicao]=num
                            print(printar(tabela))
                        elif tabela[posicao]!=0:
                            tirar= tabela[posicao]
                            
                            mesa.append(tirar)
                            tabela[posicao]=num
                            print(printar(tabela))
                elif posicao >12:
                    if (num<tabela[posicao+1] or tabela[posicao+1]==0 ) and (num>tabela[posicao-1] or tabela[posicao-1]==0 ) and (num>tabela[posicao-4] or tabela[posicao-4]==0):
                        if tabela[posicao]==0:
                            tabela[posicao]=num
                            print(printar(tabela))
                        elif tabela[posicao]!=0:
                            tirar= tabela[posicao]
                            
                            mesa.append(tirar)
                            tabela[posicao]=num
                            print(printar(tabela))
        if num==2:
            mesa.append(trevo)

    return tabela

def guardar(saco,tabela_j,mesa):
    file = open('original.txt','w')
    file.write("%s\n" %(saco))
    file.write("%s\n"%(tabela_j))
    file.write("%s"%(mesa))
    file.close()

def carregar_partida():
    file =open('original.txt','r')
    Guardado = file.readlines()
    file.close()
    return (Guardado)
    