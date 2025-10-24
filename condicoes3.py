# Sistema de verificação se o numero é par ou impar e se é positivo ou negativo

# Solicitando informações
numero = float(input("Digite um numero do conjunto dos reais: "))

# Verificando se o numero é par ou ímpar
if numero % 2 == 0:
    print("Número par.")
else:
    print("Número ímpar.")

# Verificando se o número é positivo ou negativo
if numero > 0:
    print("Número positivo.")
elif numero < 0:
    print("Número negativo.")
else:
    print("Número zero")