# Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina.
# O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. 
# Utilize um loop 'for' para iterar sobre os alunos e suas notas.

# Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. 
# Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

# Ao final, exiba a média geral da turma.




quantidade_alunos = int(input("Quantos alunos estão na disciplina? "))
numero_do_aluno = 1
soma_das_medias = 0
for aluno in range(1, quantidade_alunos+1):
    nome_do_aluno = input(f"Digite o nome do {numero_do_aluno}º aluno: ")
    nota_1 = float(input("Digite a 1ª nota: "))
    nota_2 = float(input("Digite a 2ª nota: "))
    nota_3 = float(input("Digite a 3ª nota: "))
    media_individual = float(nota_1 + nota_2 + nota_3) / 3
    soma_das_medias += media_individual
    if media_individual >= 7 and media_individual <= 10:
        resultado = "Aprovado!"
    else:
        resultado = "Reprovado!"
    print(f"Aluno: {nome_do_aluno}\n1ª Nota: {nota_1}\n2ª Nota: {nota_2}\n3ª Nota: {nota_3}\nMédia: {media_individual:.2f}\nResultado: {resultado}")
    numero_do_aluno+=1
(print(f"A média geral da turma é: {soma_das_medias / quantidade_alunos}"))
