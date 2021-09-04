print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 22

chute = input("Digite seu chute: ")

print("Você digitiou ", chute)

chute = int(chute)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou!!")

else:

    if(maior):
        print("Voce errou!! seu chute foi maior que o número secreto")
    if (menor):
        print("Voce errou!! seu chute foi menor que o número secreto")

print("Fim de jogo!!!")
