import os
import entregadores 
import pedidos 
import atualizacao 
import consultas
import relatorio 



def menu_principal():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  MENU PRINCIPAL\n=======================================================")
    op = input("\n  1. Entregadores\n  2. Pedidos\n  3. Consultas\n  4. Relatorios\n  0. Finalizar Sistema\n  Opcao: ")

    if op == "1":
        menu_entregadores()
    elif op == "2":
        menu_pedidos()
    elif op == "3":
        menu_consultas()
    elif op == "4":
        menu_relatorios()
    elif op == "0":
        os.system("cls" if os.name == "nt" else "clear")
        print(f"=======================================================\n  Sistema FluxoNorte encerrado. Ate logo!\n=======================================================")
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        menu_principal()


def menu_entregadores():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  ENTREGADORES\n=======================================================")
    print("\n  1. Cadastrar Entregador\n  2. Listar Entregadores\n  0. Voltar\n")
    op = input("  Opcao: ")

    if op == "1":
        entregadores.cadastrar_entregador()
    elif op == "2":
        entregadores.listar_entregadores()
    elif op == "0":
        menu_principal()
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        menu_entregadores()


def menu_pedidos():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS\n=======================================================")
    print("\n  1. Cadastrar Pedido\n  2. Alterar Status do Pedido\n  3. Cancelar Pedido\n  4. Associar Entregador a Pedido\n  0. Voltar\n")
    op = input("  Opcao: ")

    if op == "1":
        pedidos.cadastrar_pedido()
    elif op == "2":
        atualizacao.alterar_status()
    elif op == "3":
        atualizacao.cancelar_pedido()
    elif op == "4":
        atualizacao.associar_entregador()
    elif op == "0":
        menu_principal()
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        menu_pedidos()



def menu_consultas():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  CONSULTAS\n=======================================================")
    print(f"\n  1. Pedidos Pendentes\n  2. Pedidos Entregues\n  3. Entregadores Disponiveis\n  0. Voltar\n")
    op = input("  Opcao: ")

    if op == "1":
        consultas.pedidos_pendentes()
    elif op == "2":
        consultas.pedidos_entregues()
    elif op == "3":
        consultas.entregadores_disponiveis()
    elif op == "0":
        menu_principal()
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        menu_consultas()


def menu_relatorios():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  RELATORIOS\n=======================================================")
    print(f"\n  1. Total de Pedidos\n  2. Pedidos por Status\n  3. Pedidos com Alta Prioridade\n  0. Voltar\n")
    op = input("  Opcao: ")

    if op == "1":
        relatorio.total_pedidos()
    elif op == "2":
        relatorio.pedidos_por_status()
    elif op == "3":
        relatorio.alta_prioridade()
    elif op == "0":
        menu_principal()
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        menu_relatorios()
