p1 = p2 = p3 = p4 = media = 0

p1 = float(input("Nota 1: "))
p2 = float(input("Nota 2: "))
p3 = float(input("Nota 3: "))
p4 = float(input("Nota 4: "))

media = (p1 + p2 + p3 + p4) / 4

if media >= 7:
    print("Aprovado")
elif media >=5:
    print("Recuperação")
else:
    print("Reprovado")

print("Média", media)