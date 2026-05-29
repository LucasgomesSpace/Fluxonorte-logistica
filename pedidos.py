def cadastropedidos():
    item = input("Insira o item para o cadastro: ")
    while item == "" or None:
        print ("Erro: o nome do item nao pode ser nulo: ")
        item = input("Insira o item para o cadastro: ")

    peso = float(input("Insira o peso do item: "))
    while peso == "" or None:
        print ("Erro: o peso do item nao pode ser nulo: ")
        peso = float(input("Insira o peso do item: "))

    prioridade = int(input("Prioridade:\n1.0 Normal\n2.0 Medio\n3.0 Urgente\n\nEscolha sua opcao: "))
    while prioridade == "" or None:
        print ("Erro: A prioridade do item nao pode ser nulo: ")
        prioridade = int(input("Prioridade:\n1.0 Normal\n2.0 Medio\n3.0 Urgente\n\nEscolha sua opcao: "))

    status = int(input("Status\n1.0 Pendente\n2.0 Entregue\n\nEscolha sua opcao: "))
    while status == "" or None:
        print ("Erro: O status do item nao pode ser nulo: ")
        status = int(input("Status\n1.0 Pendente\n2.0 Entregue\n\nEscolha sua opcao: "))


