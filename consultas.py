import os
import dados
import menus



def pedidos_pendentes():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS PENDENTES\n=======================================================")

    encontrados = []
    for p in dados.pedidos.values():
        if p["status"] == "pendente":
            encontrados.append(p)
    if not encontrados:
        print("\n  Nenhum pedido pendente.")
    else:
        for p in encontrados:
            if p["entregador"]:
                entregador = p["entregador"]
            else:
                entregador = "Nenhum"
            print(f"\n  ID: {p['id']}  |  Item: {p['item']}  |  Prioridade: {p['prioridade']}")
            print(f"  Entregador: {entregador}")
            print("  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_consultas()


def pedidos_entregues():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS ENTREGUES\n=======================================================")

    encontrados = []
    for p in dados.pedidos.values():
        if p["status"] == "entregue":
            encontrados.append(p)
    if not encontrados:
        print("\n  Nenhum pedido entregue.")
    else:
        for p in encontrados:
            print(f"\n  ID: {p['id']}  |  Item: {p['item']}  |  Entregador: {p['entregador']}")
            print("  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_consultas()


def entregadores_disponiveis():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  ENTREGADORES DISPONIVEIS\n=======================================================")

    encontrados = []
    for e in dados.entregadores.values():
        if e["disponivel"] and len(e["pedidos"]) < e["limite"]:
            encontrados.append(e)
    if not encontrados:
        print("\n  Nenhum entregador disponivel.")
    else:
        for e in encontrados:
            vagas = e["limite"] - len(e["pedidos"])
            print(f"\n  Nome: {e['nome']}  |  Veiculo: {e['veiculo']}  |  Vagas: {vagas}/{e['limite']}")
            print("  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_consultas()
