# Sistema eleitoral para verificar a idade e a obrigatoriedade de votação

# Solicitando informações
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

# Verificando as condições para informar se o voto é ou não obrigatório
print("")
if idade >= 18 and idade < 70:
    print ("Olá, " + nome + ". Seu voto é obrigatório.")

elif idade >= 16 and idade < 18 or idade >= 70:
    print ("Olá, " + nome + ". Você pode votar, mas não é obrigatório.")

elif idade < 0:
    print ("Por favor, informe uma idade real.")

else:
    print ("Olá, " + nome + ". Você ainda não participa do sistema eleitoral.")