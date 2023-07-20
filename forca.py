import random

def jogar():    
    mensagem_boas_vindas()

    palavra_secreta = carrega_palavras()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_faltando = str(letras_acertadas.count('_'))
    print(f"Ainda faltam acertar {letras_faltando} letras!")
    print(letras_acertadas)
    
    enforcou= False
    acertou=False
    tentativas = 0

    #Enquanto NÂO se enforcou (False fica True) E NÃO acertou (False fica True)
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            
            letras_faltando = str(letras_acertadas.count('_'))
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas

        print("\n", letras_acertadas)
        print(f"\nAinda faltam acertar {letras_faltando} letras!")
    
    if (acertou):
        mensagem_vitoria()        
    else:
        mensagem_derrota(palavra_secreta)
        
    mensagem_fim_de_jogo()

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

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

def mensagem_derrota(palavra_secreta):
    print("\nPuxa, você foi enforcado!\n")
    print(f"A palavra era {palavra_secreta}\n")
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

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (letra == chute):
            letras_acertadas[index] = letra
        index += 1

def pede_chute():
    chute =input("\nDigite uma letra: ")
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def carrega_palavras(nome_arquivo="palavras.txt"):
    arquivo = open(nome_arquivo)
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())
        
    arquivo.close

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def mensagem_boas_vindas():
    print("\n*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************\n")

def mensagem_fim_de_jogo():
    print("\nFim do jogo!!!")

    print("*********************************")
    print("Obrigado por jogar!")
    print("*********************************")

if (__name__ == "__main__"):
    jogar()