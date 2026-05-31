import os
import dados
import menus


def total_pedidos():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  TOTAL DE PEDIDOS\n=======================================================")
    print(f"\n  Total de pedidos cadastrados: {len(dados.pedidos)}")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_relatorios()


def pedidos_por_status():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS POR STATUS\n=======================================================")
    contagem = {"pendente": 0, "em_transito": 0, "entregue": 0, "cancelado": 0}
    for p in dados.pedidos.values():
        if p[3] in contagem:
            contagem[p[3]] += 1
    print(f"\n  Pendente:    {contagem['pendente']}")
    print(f"  Em Transito: {contagem['em_transito']}")
    print(f"  Entregue:    {contagem['entregue']}")
    print(f"  Cancelado:   {contagem['cancelado']}")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_relatorios()


def alta_prioridade():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS COM ALTA PRIORIDADE\n=======================================================")

    urgentes = []
    for id_p, p in dados.pedidos.items():
        if p[2] == "urgente":
            urgentes.append(id_p)

    if not urgentes:
        print("\n  Nenhum pedido urgente.")
    else:
        for id_p in urgentes:
            p = dados.pedidos[id_p]
            print(f"\n  ID: {id_p}  |  Item: {p[0]}  |  Status: {p[3]}")
            print("  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_relatorios()
