cd = int(input("Digite o código do estado de origem (1-5): "))
pesoT = float(input("Digite o peso da carga em toneladas: "))
cdg = int(input("Digite o código da carga (10-40): "))

pesoKg = pesoT * 1000


if 10 <= cdg <= 20:
   precoporkg = 100.00
elif 21 <= cdg <= 30:
   precoporkg = 250.00
elif 31 <= cdg <= 40:
   precoporkg = 340.00
else:
   precoporkg = 0.0 # Caso o código fosse inválido


vcarga = pesoKg * precoporkg


if cd == 1:
   imposto = 0.35
elif cd == 2:
   imposto = 0.25
elif cd == 3:
   imposto = 0.15
elif cd == 4:
   imposto = 0.05
elif cd == 5:
   imposto = 0.0 # Isento
else:
   imposto = 0.0


vimposto = vcarga * imposto

valor_total = vcarga + vimposto


print("-" * 30)
print(f"Peso em quilos: {pesoKg:.2f} kg")
print(f"Preço da carga: R$ {vcarga:.2f}")
print(f"Valor do imposto: R$ {vimposto:.2f}")
print(f"Valor total transportado: R$ {valor_total:.2f}")
print("-" * 30)

