import os

pedidos = {"id_1": ["remedios", "40g", "urgencia", "entregue"]} #EXEMPLOS
entregadores = {"Gabriel": ["id_1", "id_2"]}
cont_pedidos = 0
limit_entrega = 3

def menu_entregadores():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"======================================================= \n  FLUXONORTE  |  ENTREGADORES\n=======================================================")
    print("\n  1. Cadastrar Entregador\n  2. Listar Entregadores\n  0. Voltar\n=======================================================")
    op = input("  Opção: ")

    if op == "1":
        input("\n  Pressione ENTER para continuar...")
        menu_entregadores()
    elif op == "2":
        input("\n  Pressione ENTER para continuar...")
        menu_entregadores()
    elif op == "0":
        menu_principal()
    else:
        print("  Opção inválida.")
        input("\n  Pressione ENTER para continuar...")
        menu_entregadores()


def menu_pedidos():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS\n=======================================================")
    print("\n  1. Cadastrar Pedido\n  0. Voltar\n")
    op = input("  Opção: ")

    if op == "1":
        input("\n  Pressione ENTER para continuar...")
        menu_pedidos()
    elif op == "0":
        menu_principal()
    else:
        print("  Opção inválida.")
        input("\n  Pressione ENTER para continuar...")
        menu_pedidos()


def menu_atualizacao():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  ATUALIZACAO DE PEDIDOS\n=======================================================")
    print(f"\n  1. Alterar Status do Pedido\n  2. Cancelar Pedido\n  3. Associar Entregador a Pedido\n  4. Remover Associacao de Entregador\n  0. Voltar\n")
    op = input("  Opção: ")

    if op == "1":
        input("\n  Pressione ENTER para continuar...")
        menu_atualizacao()
    elif op == "2":
        input("\n  Pressione ENTER para continuar...")
        menu_atualizacao()
    elif op == "3":
        input("\n  Pressione ENTER para continuar...")
        menu_atualizacao()
    elif op == "4":
        input("\n  Pressione ENTER para continuar...")
        menu_atualizacao()
    elif op == "0":
        menu_principal()
    else:
        print("  Opção inválida.")
        input("\n  Pressione ENTER para continuar...")
        menu_atualizacao()


def menu_consultas():
    os.system("cls" if os.name == "nt" else "clear")
    print("=======================================================\n  FLUXONORTE  |  CONSULTAS\n=======================================================")
    print(f"\n  1. Pedidos Pendentes\n  2. Pedidos Entregues\n  3. Buscar Pedido por ID\n  4. Entregadores Disponiveis\n  5. Todas as Entregas de um Entregador\n  0. Voltar\n")
    op = input("  Opção: ")

    if op == "1":
        input("\n  Pressione ENTER para continuar...")
        menu_consultas()
    elif op == "2":
        input("\n  Pressione ENTER para continuar...")
        menu_consultas()
    elif op == "3":
        input("\n  Pressione ENTER para continuar...")
        menu_consultas()
    elif op == "4":
        input("\n  Pressione ENTER para continuar...")
        menu_consultas()
    elif op == "5":
        input("\n  Pressione ENTER para continuar...")
        menu_consultas()
    elif op == "0":
        menu_principal()
    else:
        print("  Opção inválida.")
        input("\n  Pressione ENTER para continuar...")
        menu_consultas()


def menu_relatorios():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  RELATORIOS\n=======================================================")
    print(f"\n  1. Total de Pedidos\n  2. Pedidos por Status\n  3. Pedidos com Alta Prioridade\n  4. Entregador com Mais Entregas\n  0. Voltar\n")
    op = input("  Opção: ")

    if op == "1":
        input("\n  Pressione ENTER para continuar...")
        menu_relatorios()
    elif op == "2":
        input("\n  Pressione ENTER para continuar...")
        menu_relatorios()
    elif op == "3":
        input("\n  Pressione ENTER para continuar...")
        menu_relatorios()
    elif op == "4":
        input("\n  Pressione ENTER para continuar...")
        menu_relatorios()
    elif op == "0":
        menu_principal()
    else:
        print("  Opção inválida.")
        input("\n  Pressione ENTER para continuar...")
        menu_relatorios()


def menu_principal():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  MENU PRINCIPAL\n=======================================================")
    print(f"\n  1. Entregadores\n  2. Pedidos\n  3. Atualizacao de Pedidos\n  4. Consultas\n  5. Relatorios\n  0. Finalizar Sistema\n")
    op = input("  Opção: ")

    if op == "1":
        menu_entregadores()
    elif op == "2":
        menu_pedidos()
    elif op == "3":
        menu_atualizacao()
    elif op == "4":
        menu_consultas()
    elif op == "5":
        menu_relatorios()
    elif op == "0":
        os.system("cls" if os.name == "nt" else "clear")
        print("=======================================================\n  Sistema FluxoNorte encerrado. Ate logo!\n=======================================================")
    else:
        print("  Opção inválida.")
        input("\n  Pressione ENTER para continuar...")
        menu_principal()


menu_principal()

