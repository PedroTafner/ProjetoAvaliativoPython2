import limpar as l
import gerarID as g
import informacoes as i
def pedidos(bancoPedidos,bancoEntregas):
    opcao=0
    while opcao != 3:
        l.limpar()
        print("\n\t-- PEDIDOS --")
        print("\n1 - Cadastrar Pedido")
        print("2 - Atualizar Pedido")
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
    while prioridade != "Alta" and prioridade != "Normal":
        l.limpar()
        print("\n\t-- CADASTRO DE PEDIDOS --")
        print("\nErro, opção de prioridade inválida!\n")
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
    while opcao != 6:
        l.limpar()
        print("\n\t-- ATUALIZAR PEDIDO --")
        print("\n1 - Cancelar Pedido")
        print("2 - Finalizar Pedido")
        print("3 - Reativar Pedido")
        print("4 - Associar Pedidos à Entregadores")
        print("5 - Remover associação de Entregador")
        print("6 - Voltar para Pedidos")

        opcao=int(input("\nEscolha uma opção: "))
        match opcao:

            case 1:
                cancelar_pedido(bancoPedidos,bancoEntregas)
            case 2:
                finalizar_pedido(bancoPedidos,bancoEntregas)
            case 3:
                reativar_pedido(bancoPedidos)
            case 4:
                associar_pedido(bancoPedidos,bancoEntregas)
            case 5:
                remover_associacao(bancoPedidos,bancoEntregas)
            case 6:
                return
            case _:
                l.limpar()


def cancelar_pedido(bancoPedidos,bancoEntregas):
    l.limpar()
    cont=0
    print("\n\t-- CANCELELAMENTO DE PEDIDOS --")
    if bancoPedidos != {}:
        print("\n-- PEDIDOS DISPONÍVEIS --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] != "Entregue" or dados[4] != "Em rota":
                cont+=1
                print(f"\nID: {id_pedido} | Nome: {dados[0]} | ID do entregador: {dados[5]} | Status: {dados[4]}")
        if cont == 0:
            print("\nNenhum pedido cadastrado no momento.")
            input("\nPrecione ENTER para prosseguir...")
        id=input("\nDigite o ID do pedido que você quer cancelar: ")
        if id not in bancoPedidos.keys():
            print("\nPedido não encontrado.")
            input("\nPrecione ENTER para prosseguir...")
            return
        elif bancoPedidos[id][5] == 0:
            bancoPedidos[id][4]="Cancelado"
            print("\nPedido cancelado com sucesso!")
            input("\nPrecione ENTER para prosseguir...")
        else:
            id_entregador=bancoPedidos[id][5]
            bancoPedidos[id][5]="Cancelado"
            bancoEntregas[id_entregador][2]=0
            bancoEntregas[id_entregador][3]="Disponível"
            print("\nPedido cancelado com sucesso!")
            input("\nPrecione ENTER para prosseguir...")
    else:
        print("\nNenhum pedido cadastrado no momento.")
        input("\nDigite ENTER para prosseguir...")
            


def remover_associacao(bancoPedidos,bancoEntregas):
    l.limpar()
    print("\n\t-- REMOVER ASSOCIAÇÃO DE ENTREGADOR --")
    if bancoPedidos != {}:
        print("\n-- PEDIDOS DISPONÍVEIS --")
        for id_pedido,dados in bancoPedidos.items():
            print(f"\nID: {id_pedido} | Nome: {dados[0]} | ID do entregador: {dados[5]}")
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
    print("\n\t-- FINALIZAR PEDIDO --")
    if bancoPedidos != {}:
        if bancoEntregas != {}:
            print("\n-- PEDIDOS DISPONÍVEIS --")
            for id_pedido,dados in bancoPedidos.items():
                print(f"\nID: {id_pedido} | Nome: {dados[0]} | ID do entregador: {dados[5]}")
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
            print("\nNenhum entregador cadastrado no momento.")
            input("\nPrecione ENTER para prosseguir...")
    else:
        print("\nNenhum pedido cadastrado no momento.")
        input("\nPrecione ENTER para prosseguir...")

def reativar_pedido(bancoPedidos):
    l.limpar()
    print("\n\t-- REATIVAR PEDIDO --")
    if bancoPedidos != {}:
        print("\n-- PEDIDOS CANCELADOS --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] == "Cancelado":
                print(f"\nID: {id_pedido} | Nome: {dados[0]} | ID do entregador: {dados[5]}")
        id=input("\nDigite o ID do pedido que será reativado: ")
        if id not in bancoPedidos.keys():
            print("\nPedido não encontrado.")
            input("\nPrecione ENTER para prosseguir...")
            return
        elif bancoPedidos[id][4] == "Cancelado":
            bancoPedidos[id][4]="Pendente"
            print("\nPedido reativado com sucesso!")
            input("\nPrecione ENTER para prosseguir...")
    else:
        print("\nNenhum pedido cadastrado no momento.")
        input("\nPrecione ENTER para prosseguir...")

