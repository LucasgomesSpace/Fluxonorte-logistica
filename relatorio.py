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
        if p["status"] in contagem:
            contagem[p["status"]] += 1
    print(f"\n  Pendente:    {contagem['pendente']}\n  Em Transito: {contagem['em_transito']}\n  Entregue:    {contagem['entregue']}\n  Cancelado:   {contagem['cancelado']}")
    input("\n  Pressione ENTER para continuar...")
    menus.menu_relatorios()

def alta_prioridade():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"=======================================================\n  FLUXONORTE  |  PEDIDOS COM ALTA PRIORIDADE\n=======================================================")
    urgentes = []
    for p in dados.pedidos.values():
        if p["prioridade"] == "urgente":
            urgentes.append(p)
    if not urgentes:
        print("\n  Nenhum pedido urgente.")
    else:
        for p in urgentes:
            if p["entregador"]:
                entregador = p["entregador"]
            else:
                entregador = "Nenhum"
            print(f"\n  ID: {p['id']}  |  Item: {p['item']}  |  Status: {p['status']}")
            print(f"  Entregador: {entregador}")
            print("  -------------------------------------------------------")

    input("\n  Pressione ENTER para continuar...")
    menus.menu_relatorios()