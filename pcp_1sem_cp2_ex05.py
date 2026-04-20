# --- Definição das Funções ---

def pode_aprovar(idade, renda, valor):
    # regra: maior de 18 anos e valor <= 20x a renda
    return idade > 18 and valor <= (renda * 20)

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    # formula price: PMT = PV * (i * (1+i)^n) / ((1+i)^n - 1)
    numerador = taxa * (1 + taxa)**parcelas
    denominador = (1 + taxa)**parcelas - 1
    return valor * (numerador / denominador)

def calcular_total(parcela, parcelas):
    # calculo adicional: total = PMT * n
    return parcela * parcelas

def calcular_juros(total, valor_original):
    # calculo adicional: juros = total - PV
    return total - valor_original

# --- codigo principal ---

nome = input("Nome do cliente: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: R$ "))
valor_financiado = float(input("Valor do empréstimo: R$ "))
n_parcelas = int(input("Número de parcelas (3 a 24): "))

# validação do número de parcelas
if n_parcelas < 3 or n_parcelas > 24:
    print("Erro: O número de parcelas deve ser entre 3 e 24.")
else:
    # verificação de aprovação
    if pode_aprovar(idade, renda, valor_financiado):
        taxa = definir_taxa(n_parcelas)
        pmt = calcular_parcela(valor_financiado, taxa, n_parcelas)
        total_pago = calcular_total(pmt, n_parcelas)
        juros_pagos = calcular_juros(total_pago, valor_financiado)

        # exibição dos resultados
        print("\n" + "="*30)
        print("STATUS: EMPRÉSTIMO APROVADO")
        print(f"Nome do cliente: {nome}")
        print(f"Valor financiado: R$ {valor_financiado:.2f}")
        print(f"Taxa de juros aplicada: {taxa * 100:.0f}% ao mês")
        print(f"Valor da parcela: R$ {pmt:.2f}")
        print(f"Valor total pago: R$ {total_pago:.2f}")
        print(f"Total de juros pagos: R$ {juros_pagos:.2f}")
        print("="*30)
    else:
        # Item 5 - Se negado
        print("\n" + "="*30)
        print("STATUS: EMPRÉSTIMO NEGADO")
        print("Motivo: O cliente não atende aos requisitos de idade ou renda.")
        print("="*30)