menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: "))
        if (deposito > 0):
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor do depósito deve ser positivo.")

    elif opcao == "s":
        if (numero_saques <= LIMITE_SAQUES):
            saque = float(input("Informe o valor do saque: "))
            if (saque > limite):
                print("Saque não deve ultrapassar valor de R$500.00.")
            elif (saque < 0):
                print("Valor do saque deve ser positivo.")
            elif (saque < saldo):
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite diário de três saques alcançado.")

    elif opcao == "e":
        print("==========EXTRATO==========")
        if (extrato == ""):
            print("Nenhuma transaçao foi realizada.")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("===========================")
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")