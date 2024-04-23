#### JOGOTECA ####
# DESENVOLVIDO POR ARTHUR RAMPANI #


import os
from jogo_da_advinhação import*
from jogo_forca import*
from joga_da_velha import*
from Tabuada_extreme import*
os.system("cls")

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
    tabuada_extrema()