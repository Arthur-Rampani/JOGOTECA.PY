def jogo_velha():
    marcacoes = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    jogador = "X"
    contador = 0
    while True: # jogo
        while True: #Pergunta a jogada até ser uma jogada válida
            #Exibe o tabuleiro
            print(f"{marcacoes[0]:^5}|{marcacoes[1]:^5}|{marcacoes[2]:^5}|")
            print(f"{marcacoes[3]:^5}|{marcacoes[4]:^5}|{marcacoes[5]:^5}|")
            print(f"{marcacoes[6]:^5}|{marcacoes[7]:^5}|{marcacoes[8]:^5}|")
            print(f"É a vez do {jogador}")
            #Pergunta qual é a jogada
            jogada = int(input("Faça a sua jogada: "))
            # verificar se a jogada é válida
            if marcacoes[jogada-1] == "X" or marcacoes[jogada-1] == "O":
                print("Jogada inválida!")
            else:
                break
        #Grava a jogada
        if jogada == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            marcacoes[jogada - 1] = jogador
        #Fazendo o X ganhar
        if marcacoes[0] == 'X' and marcacoes[1] == marcacoes[2] == 'X':
            print("O X ganhou!")
            exit()
        elif marcacoes[0] == 'X' and marcacoes[4] == 'X' and marcacoes[8] == 'X':
            print("O X ganhou!")
            exit()
        if marcacoes[0] == 'X' and marcacoes[3] == 'X' and marcacoes[6] == 'X':
            print("O X ganhou!")
            exit()
        if marcacoes[1] == 'X' and marcacoes[4] == 'X' and marcacoes [7] == 'X':
            print("O X ganhou!")
            exit()
        if marcacoes[2] == 'X' and marcacoes[5] == 'X' and marcacoes[8] == 'X':
            print("O X ganhou!")
        elif marcacoes[2] == 'X' and marcacoes[4] == 'X' and marcacoes[6] == 'X':
            print("O X ganhou!")
        if marcacoes[3] == 'X' and marcacoes[4] == 'X' and marcacoes[5] == 'X':
            print("O X ganhou!")
        if marcacoes[6] == 'X' and marcacoes[7] == 'X' and marcacoes[8] == 'X':
            print("O X ganhou!")
        #Fazendo o O ganhar
        if marcacoes[0] == 'O' and marcacoes[1] == marcacoes[2] == 'O':
            print("O O ganhou!")
            exit()
        elif marcacoes[0] == 'O' and marcacoes[4] == 'O' and marcacoes[8] == 'O':
            print("O O ganhou!")
            exit()
        if marcacoes[0] == 'O' and marcacoes[3] == 'O' and marcacoes[6] == 'O':
            print("O O ganhou!")
            exit()
        if marcacoes[1] == 'O' and marcacoes[4] == 'O' and marcacoes [7] == 'O':
            print("O O ganhou!")
            exit()
        if marcacoes[2] == 'O' and marcacoes[5] == 'O' and marcacoes[8] == 'O':
            print("O O ganhou!")
            exit()
        elif marcacoes[2] == 'O' and marcacoes[4] == 'O' and marcacoes[6] == 'O':
            print("O O ganhou!")
            exit()
        if marcacoes[3] == 'O' and marcacoes[4] == 'O' and marcacoes[5] == 'O':
            print("O O ganhou!")
            exit()
        if marcacoes[6] == 'O' and marcacoes[7] == 'O' and marcacoes[8] == 'O':
            print("O O ganhou!")
            exit()
        contador = contador + 1
        if contador == 9:
            print("DEU VELHA!")
            exit()
        #Alternei o jogador
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"