import random

def jogo_advinhacao():
    print("JOGO MORTAL")
    print("ESCOLHA A DIFICULDADE")
    print("1 - FÁCIL: 1-5")
    print("2 - MÉDIO: 1-20")
    print("3 - DIFÍCIL: 1-50")
    print("4 - SENAI: 1-100")
    dificuldade = int(input("Selecione a dificuldade: "))
    tentativas = 0
    if dificuldade == 1:
        numero_min = 1
        numero_max = 5
    if dificuldade == 2:
        numero_min = 1
        numero_max = 20
    if dificuldade == 3:
        numero_min = 1
        numero_max = 50
    if dificuldade == 4:
        numero_min = 1
        numero_max = 100
    # gerando número aleatório
    numero_aleatorio = random.randint(numero_min, numero_max)
    print("Você tem 5 vidas")
    # msostrando os números
    while True:
        tentativas = tentativas + 1
        if tentativas == 5:
            print("VOCÊ PERDEU")
            break
        chute = int(input("qual seu chute? "))
        if chute > numero_max:
            print("OLHA DIREITO")
        if chute == numero_aleatorio:
            print("PARABÉNS")
            print(f"voce conseguiu em {tentativas} tentativas")
            break
        if chute < numero_aleatorio:
            print("aumente mais")
        if chute > numero_aleatorio:
            print("diminua")