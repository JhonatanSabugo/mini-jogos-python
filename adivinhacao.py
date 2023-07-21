import random

def jogar():
    mensagem_boas_vindas()

    numero = numero_secreto()
    rodada= 1   #variavel com o minimo de rodadas
    total_de_tentativas= 0  #variavel que irá armazenar a dificuldade que sera o max de jogadas
    pontos = 500    #pontuação que irá diminuir conforme o numero q o jogador digitar estiver longe do numero_secreto

    total_de_tentativas = selecao_nivel()

    testa_numero(rodada, total_de_tentativas, numero, pontos)

    mensagem_fim_de_jogo()

def mensagem_boas_vindas():
    welcome = ("Bem vindo ao jogo de adivinhação!")

    # print("\n*********************************")
    # print("Bem vindo ao jogo de adivinhação!")
    # print("*********************************\n")  

    return welcome  

def numero_secreto():
    numero_secreto = random.randrange(1,101)    #variavel que irá receber um numero "aleatório" que o usuario terá q adivinhar
    return numero_secreto

def selecao_nivel(nivel= int):
    # print("(1) Fácil (2) Médio (3) Difícil")
    # nivel = int(input("\tDefina o nível: "))  #variavel que irá receber o nivel

    if (nivel == 1):    #Se o nivel for igual a 1 o jogador terá 20 tentativas
        total_de_tentativas = 20
    elif (nivel == 2):  #Se o nivel for igual a 2 o jogador terá 10 tentativas
        total_de_tentativas = 10
    elif (nivel == 3):  #Se o nivel for igual a 3 o jogador terá 5 tentativas
        total_de_tentativas = 5
    else:   #Tratamento se o usuario digitar um numero diferente dos ditos acima
        print("Numero não atribuido a nenhum nivel")

    return total_de_tentativas  

def testa_numero(rodada, total_de_tentativas, numero, pontos):
    for rodada in range(1, total_de_tentativas +1):
        print(f"\nTentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um numero entre 1 e 100: "))
        print("\nvocê digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 0 e 100!")
            continue

        correto = chute == numero
        maior   = chute > numero

        if(correto):
            mensagem_vitoria()
            print(f"\nSua pontuação foi de {pontos} pontos!\n")
            break
        else:
            if(maior):
                print("Que pena!!! Seu chute foi maior que o número secreto. Tente novamente!")
                if(rodada == total_de_tentativas):
                    mensagem_derrota()
                    print(f"\n Sua pontuação foi de {pontos} pontos!")
            else:
                print("Que pena!!! Seu chute foi menor que o número secreto. Tente novamente!")
                if(rodada == total_de_tentativas):
                    mensagem_derrota()
                    print(f"\n Sua pontuação foi de {pontos} pontos!")

            pontos_perdidos = abs(numero - chute)
            pontos = pontos - pontos_perdidos

def mensagem_vitoria():
    print("\nParabéns, você ganhou!\n")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_derrota(numero_secreto):
    print("\nPuxa, você foi enforcado!\n")
    print(f"O numero era {numero_secreto}\n")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mensagem_fim_de_jogo():
    print("\tFim do jogo!!!\n")

    print("*********************************")
    print("*      Obrigado por jogar!      *")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()