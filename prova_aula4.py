inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
soma_pares = 0
par = False
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pares += numero
        par = True

else:
    if par:
        print(f"A soma dos números pares é: {soma_pares}.")
    else:
        print("Não á números pares.")