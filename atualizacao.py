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
    if pedido["status"] == "cancelado":
        print("  Pedido cancelado nao pode ser alterado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    print(f"\n  Status atual: {pedido['status']}")
    op = input("\n  Novo status:\n  1. Pendente\n  2. Em Transito\n  3. Entregue\n\n  Opcao: ").strip()
    if op == "1":
        pedido["status"] = "pendente"
    elif op == "2":
        pedido["status"] = "em_transito"
    elif op == "3":
        pedido["status"] = "entregue"
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
    if pedido["status"] == "cancelado":
        print("  Pedido ja esta cancelado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    if pedido["entregador"]:
        nome_ent = pedido["entregador"]
        if nome_ent in dados.entregadores and id_pedido in dados.entregadores[nome_ent]["pedidos"]:
            dados.entregadores[nome_ent]["pedidos"].remove(id_pedido)

    pedido["status"] = "cancelado"
    pedido["entregador"] = None

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
    if pedido["status"] == "cancelado":
        print("  Pedido cancelado nao pode receber entregador.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    if pedido["entregador"]:
        print(f"  Pedido ja possui entregador: {pedido['entregador']}")
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
    if not entregador["disponivel"]:
        print("  Entregador esta indisponivel.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    if len(entregador["pedidos"]) >= entregador["limite"]:
        print(f"  Entregador atingiu o limite de pedidos ({entregador['limite']}).")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_pedidos()
        return

    entregador["pedidos"].append(id_pedido)
    pedido["entregador"] = nome_ent

    print("\n  Entregador associado com sucesso!")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_pedidos()
