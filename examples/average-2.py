nota1 = nota2 = nota3 = media = 0

nota1 = int(input("Informe a nota 1: "))
nota2 = int(input("Informe a nota 2: "))

media = (nota1 + nota2) / 2
print(f"Média {media}")

if media >= 7:
    print("Aprovado")
else:
    if media < 5:
        print("Reprovado")
    else:
        print("Recuperação")
        nota3 = int(input("Informe a nota de recuperação: "))

        if nota1 > nota2:
            media = (nota1 + nota3) / 2
        else:
            media = (nota2 + nota3) / 2

        if media >= 7:
            print("Aprovado")
        else:
            print("Repovado após recuperação")

        print(f"Média {media}")
