# =========================
# Sistema Bancário Simples
# Funções: Depositar, Sacar, Extrato e Sair
# Controle de limite por saque e número máximo de saques
# =========================

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis principais
saldo = 0  # Saldo inicial do cliente
limite = 500  # Valor máximo permitido por saque
extrato = []  # Lista para registrar todas as movimentações
numero_saques = 0  # Contador de saques realizados
LIMITE_SAQUES = 3  # Máximo de saques permitidos por sessão

# Loop principal do programa (executa até o usuário escolher sair)
while True:

    opcao = input(menu)  # Lê a opção escolhida pelo usuário

    # ======================
    # Depósito
    # ======================
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:  # só permite valores positivos
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")  # adiciona no histórico
        else:
            print("Operação falhou! O valor informado é inválido.")

    # ======================
    # Saque
    # ======================
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        # Regras de validação
        excedeu_saldo = valor > saldo  # saque maior que o saldo
        excedeu_limite = valor > limite  # saque maior que o limite permitido
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # já atingiu limite de saques

        # Validações com mensagens de erro específicas
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:  # saque válido
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")  # registra saque no histórico
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    # ======================
    # Extrato
    # ======================
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in extrato:  # percorre lista de operações
                print(movimento)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # ======================
    # Sair do sistema
    # ======================
    elif opcao == "q":
        break  # encerra o loop principal e finaliza o programa

    # ======================
    # Opção inválida
    # ======================
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
