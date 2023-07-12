import random

def jogar():
    print("\n*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")

    numero_secreto = random.randrange(1,101)    #variavel que irá receber um numero "aleatório" que o usuario terá q adivinhar

    rodada= 1   #variavel com o minimo de rodadas
    total_de_tentativas= 0  #variavel que irá armazenar a dificuldade que sera o max de jogadas
    pontos = 500    #pontuação que irá diminuir conforme o numero q o jogador digitar estiver longe do numero_secreto

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("\tDefina o nível: "))  #variavel que irá receber o nivel

    if (nivel == 1):    #Se o nivel for igual a 1 o jogador terá 20 tentativas
        total_de_tentativas = 20
    elif (nivel == 2):  #Se o nivel for igual a 2 o jogador terá 10 tentativas
        total_de_tentativas = 10
    elif (nivel == 3):  #Se o nivel for igual a 3 o jogador terá 5 tentativas
        total_de_tentativas = 5
    else:   #Tratamento se o usuario digitar um numero diferente dos ditos acima
        print("Numero não atribuido a nenhum nivel")

    for rodada in range(1, total_de_tentativas +1):
        print(f"\nTentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um numero entre 1 e 100: "))
        print("\nvocê digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 0 e 100!")
            continue

        correto = chute == numero_secreto
        maior   = chute > numero_secreto

        if(correto):
            print(f"\nParabéns!!! Você acertou! Sua pontuação foi de {pontos} pontos!\n")
            break
        else:
            if(maior):
                print("Que pena!!! Seu chute foi maior que o número secreto. Tente novamente!")
                if(rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. Sua pontuação foi de {pontos} pontos!")
            else:
                print("Que pena!!! Seu chute foi menor que o número secreto. Tente novamente!")
                if(rodada == total_de_tentativas):
                    print(f"O número secreto era {numero_secreto}. Sua pontuação foi de {pontos} pontos!")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("\tFim do jogo!!!\n")

    print("*********************************")
    print("*      Obrigado por jogar!      *")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()