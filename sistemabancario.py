menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input(f"Digite o valor a ser depositado: ")) 
        if valor_deposito > 0:
            print("Valor depositado com sucesso!")
            saldo += valor_deposito
            extrato += f"Deposito realizado no valor de {valor_deposito:.2f}\n"
        else: 
            print("O valor a ser depositado deve ser maior que zero!")        
    elif opcao == "s":
        valor_saque = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")    
        elif excedeu_saldo:
            print("Retire seu dinheiro na boca do caixa")
            numero_saques += 1 
            saldo -= valor_saque
            extrato += f"Saque realizado no valor de {valor_saque:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("##########EXTRATO##########")
        print(extrato)
        print(f"{saldo:.2f}")
        print("###########################")
    elif opcao == "q":
        print("Obrigado pela preferência!")
        break
