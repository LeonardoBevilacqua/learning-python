n = int(input("Entre com a quantidade de numeros que deseja somar: "))
soma = 0

for i in range(n):
    num = float(input(f"Digite o {i+1}º. numero: "))
    soma += num

print(f"O resultado da soma é {soma}")