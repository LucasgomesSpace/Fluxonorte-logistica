import os
import dados
import menus


def pedidos_pendentes():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS PENDENTES\n=======================================================")

    encontrados = []
    for id_p, p in dados.pedidos.items():
        if p[3] == "pendente":
            encontrados.append(id_p)

    if not encontrados:
        print("\n  Nenhum pedido pendente.")
    else:
        for id_p in encontrados:
            p = dados.pedidos[id_p]
            print(f"\n  ID: {id_p}  |  Item: {p[0]}  |  Prioridade: {p[2]}")
            print("  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_consultas()


def pedidos_entregues():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS ENTREGUES\n=======================================================")

    encontrados = []
    for id_p, p in dados.pedidos.items():
        if p[3] == "entregue":
            encontrados.append(id_p)

    if not encontrados:
        print("\n  Nenhum pedido entregue.")
    else:
        for id_p in encontrados:
            p = dados.pedidos[id_p]
            print(f"\n  ID: {id_p}  |  Item: {p[0]}")
            print("  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_consultas()


def entregadores_disponiveis():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  ENTREGADORES DISPONIVEIS\n=======================================================")

    encontrados = []
    for nome, e in dados.entregadores.items():
        if e[1] == "moto":
            limite = 1
        elif e[1] == "carro":
            limite = 2
        else:
            limite = 3
        if e[2] == "disponivel" and len(e[0]) < limite:
            encontrados.append(nome)

    if not encontrados:
        print("\n  Nenhum entregador disponivel.")
    else:
        for nome in encontrados:
            e = dados.entregadores[nome]
            if e[1] == "moto":
                limite = 1
            elif e[1] == "carro":
                limite = 2
            else:
                limite = 3
            vagas = limite - len(e[0])
            print(f"\n  Nome: {nome}  |  Veiculo: {e[1]}  |  Vagas: {vagas}/{limite}")
            print("  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_consultas()
