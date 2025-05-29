numero = int(input("Digite um número da sua escolha: "))
confirm = print(f"O número escolhido foi {numero}.")
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
elif numero == 0:
    print("O número é zero.")