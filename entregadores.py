def cadastro():

    nome = input("Insira o nome do entregador: ")
    while nome == "" or None:
        print ("Erro: o nome nao pode ser nulo: ")
        nome = input("Insira o nome do entregador: ")
    cpf = input("Insira o cpf do entregador: ")
    while cpf == "" or None:
        print ("Erro: o cpf nao pode ser nulo: ")
        cpf = input("Insira o cpf do entregador: ")
    veiculo = int(input("Insira o veiculo do entregador:\n1.0 Moto\n2.0 Caroo\n3.0 Caminhao\n\nEscolha sua opcao: "))

    #perguntar como faz para colocar isso aqui na lista de menus
def listar():
    pass