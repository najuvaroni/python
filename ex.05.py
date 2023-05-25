valor = float(input("Informe o valor:"))
tempo = float(input("Informe quantos dias de atraso: "))
taxa = float(input("Informe a taxa: "))
prestacao = valor + ((valor * (taxa / 100)) * tempo)

print("O valor da prestação é: ", prestacao)