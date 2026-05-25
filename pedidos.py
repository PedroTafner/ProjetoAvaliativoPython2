import limpar as l
import gerarID as g
def pedidos(bancoPedidos):
    opcao=0
    while opcao != 4:
        l.limpar()
        print("\n\t-- PEDIDOS --")
        print("\n1 - Cadastrar pedido")
        print("2 - Listar pedidos")
        print("3 - Atualizar pedido")
        print("4 - Voltar para o Menu Principal")

        opcao=int(input("\nEscolha uma opção: "))
        match opcao:
            case 1:
                pedido=cadastrar()
                id_pedido=g.gerar_id(1)
                bancoPedidos[id_pedido]=pedido
                return  bancoPedidos,id_pedido
            case 2:
                listar(bancoPedidos)
            case 3:
                atualizar(bancoPedidos)
            case 4:
                return
            case _:
                l.limpar()

   
def cadastrar():
    l.limpar()
    pedido=[]
    print("\n\t-- CADASTRO DE PEDIDOS --")
    nome=input("\nDigite o nome do cliente:  ")
    pedido.append(nome)
    endereco=input("Digite o endereço do cliente: ")
    pedido.append(endereco)
    prioridade=input("Digite a prioridade do pedido (Alta ou Normal): ")
    pedido.append(prioridade)
    descricao=input("Digite a descrição do pedido: ")
    pedido.append(descricao)
    status="Pendente"
    pedido.append(status)
    return pedido

def atualizar(bancoPedidos):
    opcao=0
    while opcao != 5:
        l.limpar()
        print("\n\t-- ATUALIZAR PEDIDO --")
        print("\n1 - Alterar o status do pedido")
        print("2 - Cancelar o pedido")
        print("3 - Associar entregadores a pedidos")
        print("4 - Remover associação de entregador")
        print("5 - Voltar para pedidos")

        opcao=int(input("\nEscolha uma opção: "))
        match opcao:

            case 1:
                atualizar_status(bancoPedidos)
            case 2:
                cancelar(bancoPedidos)
            case 3:
                pass
            case 4:
                pass
            case 5:
                return
            case _:
                l.limpar()

def listar(bancoPedidos):
    l.limpar()
    print("\n\t-- LISTAGEM DE PEDIDOS --\n")
    if bancoPedidos == {}:
        print("Nenhum pedido cadastrado no momento.")
    else:
        print(bancoPedidos)
    input("\nDigite ENTER para prosseguir...")

def atualizar_status(bancoPedidos):
    l.limpar()
    print("\n\t-- ATUALIZAR STATUS DO PEDIDO --")
    if bancoPedidos != {}:
        id=input("\nDigite o ID do pedido que você quer atualizar: ")
        if id in bancoPedidos.keys():
            x=input("\nQual o novo status do pedido: ")
            bancoPedidos[id][4]=x
            print("\nStatus atualizado com sucesso!")
            input("\nDigite ENTER para prosseguir...")
        else:
            print("\nPedido não encontrado.")
            input("\nDigite ENTER para prosseguir...")
    else:
        print("\nNenhum pedido cadastrado no momento.")
        input("\nDigite ENTER para prosseguir...")

def cancelar(bancoPedidos):
    l.limpar()
    print("\n\t-- CANCELAR PEDIDO  --")
    if bancoPedidos != {}:
        id=input("\nDigite o ID do pedido que você quer cancelar: ")
        if id in bancoPedidos.keys():
            del bancoPedidos[id]
            print("\nPedido cancelado com sucesso!")
            input("\nDigite ENTER para prosseguir...")
        else:
            print("\nPedido não encontrado.")
            input("\nDigite ENTER para prosseguir...")
    else:
        print("\nNenhum pedido cadastrado no momento.")
        input("\nDigite ENTER para prosseguir...")