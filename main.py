#### JOGOTECA ####
# DESENVOLVIDO POR ARTHUR RAMPANI #


import os
from jogo_da_advinhação import*
from jogo_forca import*
from joga_da_velha import*
from TabuadaExtreme import*
from pedra_papel_tesoura import*
os.system("cls")
def main():
    pessoa = int(input("Qual a sua idade? "))
    if pessoa >=18:
        print("Você está liberado para jogar")
        print("*****************************")
        print("*    BEM VINDO À JOGOTECA   *")
        print("*          JOGOS            *")
        print("*   1- JOGO DA ADVINHAÇÃO   *")
        print("*   2-  JOGO DA FORCA       *")
        print("*   3-  JOGO DA VELHA       *")
        print("*   4- TABUADA EXTREME      *")
        print("*   5-    JOKENPO           *")
        print("*****************************")
    else:
        print("Sai daqui muleke")
    jogo_escolhido = int(input("Em qual dos jogos deseja jogar? "))

    if jogo_escolhido == 1: #JOGO DA ADVINHAÇÃO
        jogo_advinhacao()

    if jogo_escolhido == 2:
        forca()

    if jogo_escolhido == 3: 
        jogo_velha()

    if jogo_escolhido == 4:
        tabuada()

    if jogo_escolhido == 5:
        pedra_papel_tesoura()
main()
while True:
    print("1 - SIM")
    print("2 - NÃO")
    jogar_denovo = int(input("Você quer jogar denovo? "))
    if jogar_denovo == 1:
        main()
    else:
        exit()