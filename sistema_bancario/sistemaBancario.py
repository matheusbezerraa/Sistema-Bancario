menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor 
            extrato == f"Depósito: R${valor:.2f}\n"
        else:
            print("Operação falhou, valor inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))      

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques  >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operaçao falhou! Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operaçao falhou: o valor do saque excede o limite")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

    elif opcao =="e":
        print("\nEXTRATO")
        print("Sem movimentações" if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("")

    elif opcao == "q":
        break

    else:
        print("Operaçao invalida, por favor tente novamente")                       
