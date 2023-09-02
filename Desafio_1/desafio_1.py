saldo_atual = float(input("Digite seu saldo: "))
valor_deposito = float(input("Digite o valor do deposito: "))
valor_retirada = float(input("Digite o valor do saque: "))

# TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.

# TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).

saldo_atual = saldo_atual + valor_deposito

saldo_atual = saldo_atual - valor_retirada
print(f"Saldo atualizado na conta: {float(saldo_atual)}")
