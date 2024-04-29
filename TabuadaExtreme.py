import random
def tabuada():
    print('BEM VINDO A TABUADA EXTREME')
    print('SE VOCE NAO FOR BURRO, ISSO SERÁ FACIL')

    print('Você está pronto para iniciar?')
    começar = int(input('Digite 1 para o sofrimento começar! '))

    #descobrindo os numeros aleatorios

    if começar == 1:
        numero1 = random.randint(1, 10)
        numero2 = random.randint(1,10)

    #descobrindo qual vai ser a operação
            
    soma_aleatoria = random.randint(1, 4)
    if soma_aleatoria == 1:
        resultado = numero1*numero2
        operador = 'multiplição'
        print(f'você deve fazer uma multiplicação! ')
    elif soma_aleatoria == 2:
        resultado = numero1+numero2
        operador = 'soma'
        print(f'você deve fazer uma soma! ')
    elif soma_aleatoria == 3:
        resultado = numero1 - numero2
        operador = 'subtração'
        print(f'você deve fazer uma subtração! ')
    elif soma_aleatoria == 4:
        resultado = numero1 / numero2
        operador = 'divisão'
        print(f'você deve fazer uma divisão! ')
    print(f'o primeiro numero é {numero1}')
    print(f'o segundo numero é {numero2}')

        #calculando os pontos do usuario

    pontos = 0

        #descobrindo a resposta do usuário

    resposta = float(input(f'qual o resultado da {operador} {numero1} entre {numero2}: '))
    if resposta == resultado:
        while resposta == resultado:
            print('Acertou')
            print('')
            pontos += 1
            ######
                        
                        
            numero1 = random.randint(1, 10)
            numero2 = random.randint(1,10)

            #descobrindo qual vai ser a operação
                    
            soma_aleatoria = random.randint(1, 4)
            if soma_aleatoria == 1:
                resultado = numero1*numero2
                operador = 'multiplição'
                print(f'você deve fazer uma multiplicação! ')
            elif soma_aleatoria == 2:
                resultado = numero1+numero2
                operador = 'soma'
                print(f'você deve fazer uma soma! ')
            elif soma_aleatoria == 3:
                    resultado = numero1 - numero2
                    operador = 'subtração'
                    print(f'você deve fazer uma subtração! ')
            elif soma_aleatoria == 4:
                resultado = numero1 / numero2
                operador = 'divisão'
                print(f'você deve fazer uma divisão! ')
            print(f'o primeiro numero é {numero1}')
            print('')
            print(f'o segundo numero é {numero2}')
            print('')
            resposta = float(input(f'qual o resultado da {operador} {numero1}  entre {numero2} '))
            if resposta != resultado:
                print('')
                print('Errou burro')
                print('')
                print(f'você fez {pontos} pontos!')