import random
#Esta funcao escolhe uma palavra aleatoria

def escolha_de_palavra(): #Para saber qual e a palavra
    print("JOGO DA FORCA")
    print("1 - POKEMON")
    print("2 - NOMES")
    print("3 - OBJETOS")
    dificuldade = int(input("QUAL LISTA VOCÊ DESEJA USAR: "))
    if dificuldade == 1:
        arquivo = open("jogodaforca/pokemons.txt","r",encoding = "utf8")
    if dificuldade == 2:
        arquivo = open("jogodaforca/nomes.txt","r",encoding = "utf8")
    if dificuldade == 3:
        arquivo = open("jogodaforca/objetos.txt","r",encoding = "utf8")
    lista_pokemon = arquivo.readlines()
    arquivo.close()
    palavra_escolhida = random.choice(lista_pokemon)
    palavra_escolhida_limpa = palavra_escolhida.strip()
    #print(palavra_escolhida_limpa)
    return palavra_escolhida_limpa


def criando_mascara(palavra:str) -> list: #Para mostrar as underlines com base nas letras 
    letras = (len(palavra)) #Para saber quantas letras foram
    mascara = [] #Uma lista vazia para armazenar as underlines

    mascara = []
    for x in range(letras):
        mascara.append("_")
    return mascara

def preenche_mascara(palavra_secreta:str,letra_escolhida:str,mascara):
    indice = 0
    for letra in palavra_secreta:
        if letra_escolhida == letra:
            mascara[indice] = letra_escolhida
        indice +=1
        if "_" not in mascara:
            print("Você venceu")
            break

    return mascara

