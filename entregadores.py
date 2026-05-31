import os
import dados
import menus




def cadastrar_entregador():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  CADASTRAR ENTREGADOR\n=======================================================")

    nome = input("\n  Nome: ").strip()
    if nome == "":
        print("  Nome nao pode ser vazio.")
        input("\n  Pressione ENTER para continuar...")
        cadastrar_entregador()
        return

    if nome in dados.entregadores:
        print("  Entregador ja cadastrado.")
        input("\n  Pressione ENTER para continuar...")
        menus.menu_entregadores()
        return

    op = input("\n  Veiculo:\n  1. Moto\n  2. Carro\n  3. Caminhao\n\n  Opcao: ").strip()
    if op == "1":
        veiculo = "moto"
        limite = 1
    elif op == "2":
        veiculo = "carro"
        limite = 2
    elif op == "3":
        veiculo = "caminhao"
        limite = 3
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        cadastrar_entregador()
        return

    disp = input("\n  Disponivel?\n  1. Sim\n  2. Nao\n\n  Opcao: ").strip()
    if disp == "1":
        disponivel = True
    elif disp == "2":
        disponivel = False
    else:
        print("  Opcao invalida.")
        input("\n  Pressione ENTER para continuar...")
        cadastrar_entregador()
        return

    dados.entregadores[nome] = {
        "nome":       nome,
        "veiculo":    veiculo,
        "limite":     limite,
        "disponivel": disponivel,
        "pedidos":    []
    }

    print("\n  Entregador cadastrado com sucesso!")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_entregadores()


def listar_entregadores():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  LISTAR ENTREGADORES\n=======================================================")

    if not dados.entregadores:
        print("\n  Nenhum entregador cadastrado.")
    else:
        for nome, e in dados.entregadores.items():
            if e["disponivel"]:
                status = "Disponivel"
            else:
                status = "Indisponivel"

            if e["pedidos"]:
                lista_pedidos = e["pedidos"]
            else:
                lista_pedidos = "Nenhum"

            ocupacao = f"{len(e['pedidos'])}/{e['limite']}"
            print(f"\n  Nome: {nome}  |  Veiculo: {e['veiculo']}  |  Capacidade: {ocupacao}  |  Status: {status}")
            print(f"  Pedidos: {lista_pedidos}")
            print(f"  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_entregadores()
