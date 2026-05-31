import os
import dados
import menus


def cadastrar_pedido():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  CADASTRAR PEDIDO\n=======================================================")

    item = input("\n  Item: ").strip()
    if item == "":
        print("  Item nao pode ser vazio.")
        input("\n  Pressione ENTER para continuar...")
        cadastrar_pedido()
        return

    peso = input("  Peso (kg): ").strip()
    if peso == "":
        print("  Peso nao pode ser vazio.")
        input("\n  Pressione ENTER para continuar...")
        cadastrar_pedido()
        return

    op_pri = input("\n  Prioridade:\n  1. Normal\n  2. Medio\n  3. Urgente\n\n  Opcao: ").strip()
    if op_pri == "1":
        prioridade = "normal"
    elif op_pri == "2":
        prioridade = "medio"
    elif op_pri == "3":
        prioridade = "urgente"
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        cadastrar_pedido()
        return

    dados.contador_pedidos += 1
    id_pedido = f"id_{dados.contador_pedidos}"
    dados.pedidos[id_pedido] = {"id":id_pedido,"item":item,"peso":peso,"prioridade":prioridade,"status":"pendente","entregador": None}
    print(f"\n  Pedido cadastrado com sucesso! ID: {id_pedido}")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_pedidos()
