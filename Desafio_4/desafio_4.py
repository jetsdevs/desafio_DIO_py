valor_inicial = float(input("Informe o valor Inicial: "))
taxa_juros = float(input("Informe o juros: "))
periodo = int(input("Informe o periodo: "))


# TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.


def calcular_juros_compostos(valor_inicial, taxa_juros, periodo):
    montante = valor_inicial * (1 + taxa_juros) ** periodo
    return montante


juros_compostos = calcular_juros_compostos(valor_inicial, taxa_juros, periodo)

print(f"Valor final do investimento: R$ {juros_compostos:.2f}")
