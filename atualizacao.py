import os
import dados
import menus


def alterar_status():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  ALTERAR STATUS DO PEDIDO\n=======================================================")

    id_pedido = input("\n  ID do pedido: ").strip()
    if id_pedido not in dados.pedidos:
        print("  Pedido nao encontrado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    pedido = dados.pedidos[id_pedido]
    if pedido[3] == "cancelado":
        print("  Pedido cancelado nao pode ser alterado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    print(f"\n  Status atual: {pedido[3]}")
    op = input("\n  Novo status:\n  1. Pendente\n  2. Em Transito\n  3. Entregue\n\n  Opcao: ").strip()
    if op == "1":
        pedido[3] = "pendente"
    elif op == "2":
        pedido[3] = "em_transito"
    elif op == "3":
        pedido[3] = "entregue"
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        alterar_status()
        return

    print("\n  Status atualizado com sucesso!")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_pedidos()


def cancelar_pedido():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  CANCELAR PEDIDO\n=======================================================")

    id_pedido = input("\n  ID do pedido: ").strip()
    if id_pedido not in dados.pedidos:
        print("  Pedido nao encontrado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    pedido = dados.pedidos[id_pedido]
    if pedido[3] == "cancelado":
        print("  Pedido ja esta cancelado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    for nome_ent in dados.entregadores:
        if id_pedido in dados.entregadores[nome_ent][0]:
            dados.entregadores[nome_ent][0].remove(id_pedido)

    pedido[3] = "cancelado"

    print("\n  Pedido cancelado com sucesso!")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_pedidos()


def associar_entregador():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  ASSOCIAR ENTREGADOR A PEDIDO\n=======================================================")

    id_pedido = input("\n  ID do pedido: ").strip()
    if id_pedido not in dados.pedidos:
        print("  Pedido nao encontrado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    pedido = dados.pedidos[id_pedido]
    if pedido[3] == "cancelado":
        print("  Pedido cancelado nao pode receber entregador.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    ja_associado = False
    for nome_ent in dados.entregadores:
        if id_pedido in dados.entregadores[nome_ent][0]:
            ja_associado = True
    if ja_associado:
        print("  Pedido ja possui entregador associado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    nome_ent = input("  Nome do entregador: ").strip()
    if nome_ent not in dados.entregadores:
        print("  Entregador nao encontrado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    entregador = dados.entregadores[nome_ent]
    if entregador[2] != "disponivel":
        print("  Entregador esta indisponivel.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    if entregador[1] == "moto":
        limite = 1
    elif entregador[1] == "carro":
        limite = 2
    else:
        limite = 3

    if len(entregador[0]) >= limite:
        print(f"  Entregador atingiu o limite de pedidos ({limite}).")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    entregador[0].append(id_pedido)

    print("\n  Entregador associado com sucesso!")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_pedidos()
