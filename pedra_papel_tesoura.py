import random
print("BEM VINDO AO JOGO JOKENPO")
print("1 - PEDRA")
print("2 - PAPEL")
print("3 - TESOURA")
numero_escolhido = int(input("digite um número: "))
numero_do_pc = random.randint(1,3)
if numero_do_pc == 1:
    numero_do_pc = "PEDRA"
if numero_do_pc == 2:
    numero_do_pc = "PAPEL"
if numero_do_pc == 3:
    numero_do_pc = "TESOURA"
if numero_escolhido == 1:
    numero_escolhido = "PEDRA"
if numero_escolhido == 2:
    numero_escolhido = "PAPEL"
if numero_escolhido == 3:
    numero_escolhido = "TESOURA"
if numero_do_pc == "PEDRA" and numero_escolhido == "PEDRA":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("EMPATADO!")
if numero_do_pc == "PEDRA" and numero_escolhido == "PAPEL":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("VOCÊ GANHOU!")
if numero_do_pc == "PAPEL" and numero_escolhido == "PEDRA":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("O COMPUTADOR GANHOU")
if numero_do_pc == "PEDRA" and numero_escolhido == "TESOURA":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("O COMPUTADOR GANHOU!")
if numero_do_pc == "TESOURA" and numero_escolhido == "PEDRA":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("VOCÊ GANHOU")
if numero_do_pc == "PAPEL" and numero_escolhido == "TESOURA":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("VOCÊ GANHOU!")
if numero_do_pc == "TESOURA" and numero_escolhido == "PAPEL":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("O COMPUTADOR GANHOU")
if numero_do_pc == "PAPEL" and numero_escolhido == "PAPEL":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("EMPATADO")
if numero_do_pc == "TESOURA" and numero_escolhido == "TESOURA":
    print(f"o computador escolheu {numero_do_pc} e você escolheu {numero_escolhido}")
    print("EMPATADO")