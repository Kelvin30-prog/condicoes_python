# Sistema de classificação de alunos de acordo com sua média das notas

# Solicitando informações
nome = input("Qual o nome do aluno? ")
nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))

# Tirando a média das notas
media = (nota1 + nota2) / 2
mediastr = str(media)
print("")
print ("A média do aluno é: " + mediastr)

# Atribuindo condições para a classificação do aluno
if media >= 9 and media <= 10:
    print("O aluno " + nome + " está classificado no grupo A - EXCELENTE")

elif media >= 7 and media < 9:
    print("O aluno " + nome + " está classificado no grupo B - BOM")

elif media >= 6 and media < 7:
    print("O aluno " + nome + " está classificado no grupo C - INTERMEDIÁRIO")

elif media >= 0 and media < 6:
    print("O aluno " + nome + " está classificado no grupo D - RUIM")

else:
    print ("Não é possivel classificar essa média")