def sacar(saldo, valor, extrato, numero_saques, limite=500, limite_saques=3):
    if numero_saques < limite_saques:   
        if valor > limite:
            print("Saque não deve ultrapassar valor de R$500.00.")
        elif valor <= 0:
            print("Valor do saque deve ser positivo.")
        elif valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Saldo insuficiente.")
    else:
        print("Limite diário de três saques alcançado.")
    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor do depósito deve ser positivo.")
    return saldo, extrato

def exibir_extrato(extrato, saldo):
    print("========== EXTRATO ==========")
    if extrato == "":
        print("Nenhuma transação foi realizada.")
    else:
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    print("=============================")

def cadastrarUsuario(cpf_lista, usuarios):
    cpf = input("Informe seu CPF: ")

    if cpf in cpf_lista:
        print("CPF já cadastrado.")
    else:
        cpf_lista.append(cpf)
        nome = input("Informe seu nome: ")
        data_nascimento = input("Informe sua data de nascimento: ")
        endereco = input("Informe seu endereço: ")

        usuarios[cpf] = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        }

def cadastrarConta(cpf_lista, contas, n_conta):
    cpf = input("Informe seu CPF: ")

    if cpf in cpf_lista:
        contas[cpf] = {
            "conta": n_conta,
            "agencia": "0001",
            "numero_saques": 0
        }
        n_conta += 1
    else:
        print("Usuário não cadastrado.")
    return n_conta
    
menu = """

[cn] Cadastrar Usuário
[cc] Cadastrar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
cpf_lista = []
usuarios = {}
n_conta = 1
contas = {}

while True:
    opcao = input(menu)
    if opcao == "cn":
        cadastrarUsuario(cpf_lista, usuarios)
    elif opcao == "cc":
        n_conta = cadastrarConta(cpf_lista, contas, n_conta)
    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "s":
        cpf = input("Informe o CPF da conta: ")
        if cpf in contas:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo, valor, extrato, contas[cpf]["numero_saques"]
            )
            contas[cpf]["numero_saques"] = numero_saques
        else:
            print("Conta não encontrada.")
    elif opcao == "e":
        exibir_extrato(extrato, saldo)
    elif opcao == "q":
        for conta in contas.values():
            conta["numero_saques"] = 0
        print("Saindo do sistema...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")