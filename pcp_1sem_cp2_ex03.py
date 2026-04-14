# Entrada das notas

cp1 = float(input("Digite sua nota da CP1: "))
cp2 = float(input("Digite sua nota da CP2: "))
cp3 = float(input("Digite sua nota da CP3: "))

sp1 = float(input("Digite sua nota da Sprint1: "))
sp2 = float(input("Digite sua nota da Sprint2: "))

gs = float(input("Digite sua nota da Global Solution: "))

# Identificar a menor nota

menor_nota = cp1
if cp2 < menor_nota:
    menor_nota = cp2
if cp3 < menor_nota:
    menor_nota = cp3
 # print(f"menor nota: {menor_nota}") <--Utilizei para conferir meu codigo, se quiser pode apagar
