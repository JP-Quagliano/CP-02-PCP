# Entrada das notas - Thiago Nakano

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

#Calculo da media - Leticia Aiko
media = (((cp1 + cp2 + cp3 - menor_nota) + (sp1 + sp2)) / 4)*0.4 + gs * 0.6
media_peso = media * 0.4

#Mostrando a nota no sistema
print(f"Sua media semestral e:{media:.1f}")
print(f"Sua media com peso e:{media_peso:.1f}")