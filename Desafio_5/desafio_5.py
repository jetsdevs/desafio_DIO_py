valor = float(input("Informe um valor: "))

if valor > 0:
    # TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
    print(
        f"""Deposito realizado com sucesso! 
            Saldo atual: R$ {valor:.2f}"""
    )
elif valor < 0:
    # TODO: Imprimir a mensagem de valor inválido.
    print("Valor invalido! Digite um valor maior que zero.")
else:
    # TODO: Imprimir a mensagem de encerrar o programa.
    print("Encerrando o programa...")
