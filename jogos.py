import adivinhacao
import forca

def escolher_jogo():
    print("****************")
    print("Escolha seu jogo")
    print("****************")

    print("(1) Forca (2) Adivinhação")
    jogo= int(input("Faça sua escolha: "))

    if (jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()
    else:
        print("Numero não correponde a nenhum jogo!")

if (__name__ == "__main__"):
    escolher_jogo()