from random import randint

# Crie uma lista de opções de jogo
t = ["Pedra", "Papel", "Tesoura"]

# Atribuir uma reprodução aleatória ao computador
computador = t[randint(0, 2)]

# Definir jogador para falso
jogador = False

while jogador == False:
# Definir o jogador como verdadeiro
    jogador = input("Pedra, Papel, Tesoura")
    if jogador == computador:
        print("Laço")
    elif jogador == "Pedra":
        if computador == "Papel":
            print("Você perdeu!", computador, "capas", jogador)
        else:
            print("Você ganhou!", jogador, "quebra", computador)
    elif jogador == "Papel":
        if computador == "Tesoura":
            print("Você perdeu", computador, "cortar", jogador)
        else:
            print("Você ganhou", jogador, "capas", computador)
    elif jogador == "Tesoura":
        if computador == "Pedra":
            print("Você perdeu", computador, "quebra", computador)
        else:
            print("Você ganhou", jogador, "cortar", computador)
    else:
        print("Essa não é uma jogada válida. Verifique a ortografia!")
    # Jogador foi definido como True, mas queremos que seja False para que o loop continue
    jogador = False
    computador = t[randint(0, 2)]





