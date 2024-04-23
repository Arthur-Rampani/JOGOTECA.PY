#Como eu coloquei todas as funcoes em outro arquivo preciso importa-lo
from jogodaforca.funcoes_forca import * 
def forca():
    #chamei a funcao escolha_palavra e armezenei o seu retorno 
    palavra_secreta = escolha_de_palavra()
    #Chamando a função criando_mascara
    palavra = criando_mascara(palavra_secreta)
    #Pergunto ao usuário a letra

    vidas = 6
    while vidas > 0:
        letra_escolhida = input("Chute uma letra: ").upper()
        if letra_escolhida not in palavra_secreta:
            vidas -= 1
            if vidas == 0:
                print("VOCÊ PERDEU")
                print(f"A palavra era {palavra_secreta}")
                exit()
        preenche = preenche_mascara(palavra_secreta,letra_escolhida,palavra)
        print(*preenche)
        if "_" not in preenche:
            print("VOCÊ GANHOU!")
            exit()
        if letra_escolhida == palavra_secreta.upper():
            print("VOCÊ GANHOU!")
            exit()