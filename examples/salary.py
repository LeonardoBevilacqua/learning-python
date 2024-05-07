salarioAntigo = 3000.0
valeAntigo = 20.0
valeNovo = 28.0
ajuste = 0.05
diasUteis = 20
horasDeTrabalho = 6

valorDoAjuste = salarioAntigo * ajuste
novoSalario = (salarioAntigo + valorDoAjuste) + (valeNovo * diasUteis)
valorPorHora = novoSalario / (diasUteis * horasDeTrabalho)

print("Salário", novoSalario)
print(f"Salário por hora {valorPorHora:.2f}")
