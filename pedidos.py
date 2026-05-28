import limpar as l
import gerarID as g
import informacoes as i
def pedidos(bancoPedidos,bancoEntregas):
    opcao=0
    while opcao != 3:
        l.limpar()
        print("\n\t-- PEDIDOS --")
        print("\n1 - Cadastrar pedido")
        print("2 - Atualizar pedido")
        print("3 - Voltar para o Menu Principal")

        opcao=int(input("\nEscolha uma opção: "))
        match opcao:
            case 1:
                pedido=cadastrar()
                id_pedido=g.gerar_id(1)
                bancoPedidos[id_pedido]=pedido
                if bancoPedidos == {} or bancoEntregas == {}:
                    return None
                else:
                    return  bancoPedidos,bancoEntregas,id_pedido
            case 2:
                atualizar(bancoPedidos,bancoEntregas)
            case 3:
                return
            case _:
                l.limpar()

   
def cadastrar():
    l.limpar()
    pedido=[]
    print("\n\t-- CADASTRO DE PEDIDOS --")
    nome=input("\nDigite o nome do cliente: ")
    pedido.append(nome)
    endereco=input("Digite o endereço do cliente: ")
    pedido.append(endereco)
    prioridade=input("Digite a prioridade do pedido (Alta ou Normal): ")
    pedido.append(prioridade)
    descricao=input("Digite a descrição do pedido: ")
    pedido.append(descricao)
    status="Pendente"
    pedido.append(status)
    id_entregador=0
    pedido.append(id_entregador)
    return pedido

def atualizar(bancoPedidos,bancoEntregas):
    opcao=0
    while opcao != 5:
        l.limpar()
        print("\n\t-- ATUALIZAR PEDIDO --")
        print("\n1 - Alterar o status do pedido")
        print("2 - Finalizar Pedido")
        print("3 - Associar pedidos à entregadores")
        print("4 - Remover associação de entregador")
        print("5 - Voltar para pedidos")

        opcao=int(input("\nEscolha uma opção: "))
        match opcao:

            case 1:
                atualizar_status(bancoPedidos,bancoEntregas)
            case 2:
                finalizar_pedido(bancoPedidos,bancoEntregas)
            case 3:
                associar_pedido(bancoPedidos,bancoEntregas)
            case 4:
                remover_associacao(bancoPedidos,bancoEntregas)
            case 5:
                return
            case _:
                l.limpar()


def atualizar_status(bancoPedidos,bancoEntregas):
    l.limpar()
    print("\n\t-- ATUALIZAR STATUS DO PEDIDO --")
    if bancoPedidos != {}:
        id=input("\nDigite o ID do pedido que você quer atualizar: ")
        if id not in bancoPedidos.keys():
            print("\nPedido não encontrado.")
            input("\nPrecione ENTER para prosseguir...")
            return
        if bancoPedidos[id][5] == 0:
            if id in bancoPedidos.keys():
                l.limpar()
                novo_status=0
                print("\n\t-- ATUALIZAR STATUS DO PEDIDO --")
                print("\n1 - Entregue")
                print("2 - Cancelado")
                if novo_status != 2:
                    novo_status=int(input("\nPara qual status você quer atualizar o pedido: "))
                    match novo_status:
                        case 1:
                            bancoPedidos[id][4]="Entregue"
                        case 2:
                            bancoPedidos[id][4]="Cancelado"
                    print("\nStatus atualizado com sucesso!")
                    input("\nDigite ENTER para prosseguir...")
            else:
                print("\nPedido não encontrado.")
                input("\nDigite ENTER para prosseguir...")
        else:
            if id in bancoPedidos.keys():
                l.limpar()
                novo_status=0
                print("\n\t-- ATUALIZAR STATUS DO PEDIDO --")
                print("\n1 - Entregue")
                print("2 - Cancelado")
                if novo_status != 2:
                    novo_status=int(input("\nQual o novo status do pedido: "))
                    match novo_status:
                        case 1:
                            id_entregador=bancoPedidos[id][5]
                            bancoPedidos[id][4]="Entregue"
                            bancoPedidos[id][5]=0
                            bancoEntregas[id_entregador][3]="Disponível"
                            bancoEntregas[id_entregador][2]=0
                        case 2:
                            id_entregador=bancoPedidos[id][5]
                            bancoPedidos[id][4]="Cancelado"
                            bancoPedidos[id][5]=0
                            bancoEntregas[id_entregador][3]="Disponível"
                            bancoEntregas[id_entregador][2]=0
                    print("\nStatus atualizado com sucesso!")
                    input("\nDigite ENTER para prosseguir...")
            else:
                print("\nPedido não encontrado.")
                input("\nDigite ENTER para prosseguir...")
    else:
        print("\nNenhum pedido cadastrado no momento.")
        input("\nDigite ENTER para prosseguir...")

def remover_associacao(bancoPedidos,bancoEntregas):
    l.limpar()
    print("\n\t-- REMOVER ASSOCIAÇÃO DE ENTREGADOR --")
    if bancoPedidos != {}:
        id_pedido=input("\nDigite o ID do pedido que você quer desassociar de um entregador: ")
        if id_pedido in bancoPedidos.keys():
            if bancoPedidos[id_pedido][5] != 0:
                id_entregador=bancoPedidos[id_pedido][5]
                bancoPedidos[id_pedido][5]=0
                bancoPedidos[id_pedido][4]="Pendente"
                bancoEntregas[id_entregador][2]=0
                bancoEntregas[id_entregador][3]="Disponível"
                print("\nPedido desassociado com sucesso!")
                input("\nDigite ENTER para prosseguir...")
            else:
                print("\nNenhum entregador associado à esse pedido.")
                input("\nPrecione ENTER para prosseguir...")
        else:
            print("\nEntregador não encontrado.")
            input("\nPrecione ENTER para prosseguir...")
    else:
        print("\nNenhum entregador cadastrado no momento.")
        input("\nPrecione ENTER para prosseguir...")

def associar_pedido(bancoPedidos,bancoEntregas):
    l.limpar()
    print("\n\t-- ASSOCIAR PEDIDOS À ENTREGADORES --")
    if bancoPedidos != {}:
        for id_pedido,dadosP in bancoPedidos.items():
            for id_entregador,dadosE in bancoEntregas.items():
                if dadosP[4] == "Pendente" and dadosE[3] == "Disponível":
                    dadosP[4]="Em rota"
                    dadosP[5]=id_entregador
                    dadosE[3]="Em trabalho"
                    dadosE[2]=id_pedido
                    print("\nPedido associado com sucesso!")
                    input("\nPrecisone ENTER para prosseguir...")
                else:
                    print("\nNenhum entregador ou pedido disponível no momento.")
    else:
        print("\nNenhum pedido cadastrado no momento.")
        input("\nPrecione ENTER para prosseguir...")

def finalizar_pedido(bancoPedidos,bancoEntregas):
    l.limpar()
    print("\n\r-- FINALIZAR PEDIDO --")
    if bancoPedidos != {}:
        id=input("\nDigite o ID do pedido que será finalizado: ")
        if id not in bancoPedidos.keys():
            print("\nPedido não encontrado.")
            input("\nPrecione ENTER para prosseguir...")
            return
        else:
            for id_pedido in bancoPedidos.keys():
                for id_entregador in bancoEntregas.keys():
                    if bancoPedidos[id_pedido][4] == "Em rota":
                        bancoPedidos[id_pedido][4]="Entregue"
                        bancoPedidos[id_pedido][5]=0
                        bancoEntregas[id_entregador][3]="Disponível"
                        bancoEntregas[id_entregador][2]=0
                        bancoEntregas[id_entregador][4]=bancoEntregas[id_entregador][4]+1
        print("\nPedido finalizado com sucesso!")
        input("\nPrecione ENTER para prosseguir...")
    else:
        print("\nNenhum pedido cadastrado no momento.")
        input("\nPrecione ENTER para prosseguir...")