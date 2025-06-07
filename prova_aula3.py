numero_secreto = 7
tentativas_totais = 3
tentativa = 1

print("Adivinhe o número entre 1 e 10.")

while tentativa <= tentativas_totais:
    numero = int(input(f"Tentativa{tentativa}: Digite o número: "))

    if numero == numero_secreto:
        print("VOCÊ ACERTOU!")
        break
    else:
        print("VOCÊ ERROU!")

    tentativa += 1

if numero != numero_secreto:
    print(f"VOCÊ PERDEU TODAS AS TENTATIVAS! O NÚMERO ERA{numero_secreto}.")