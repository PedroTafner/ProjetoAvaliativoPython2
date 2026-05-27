import limpar as l

def informacoes(bancoPedidos, bancoEntregas):
    opcao = 0
    while opcao != 7:
        
        l.limpar()
        print("\n\t-- INFORMAÇÕES --")
        print("\n1 - Pedidos Pendentes")
        print("2 - Pedidos Entregues")
        print("3 - Buscar Pedido por ID")
        print("4 - Entregador Disponível")
        print("5 - Todas as Entregas de um Entregador")
        print("6 - Relatórios Operacionais")
        print("7 - Voltar")
        
        opcao = int(input("\nEscolha uma opção: "))
        match opcao:
            case 1:
                pedidos_pendentes(bancoPedidos)
            case 2:
                pedidos_entregues(bancoPedidos)
            case 3:
                buscar_pedido(bancoPedidos)
            case 4:
                entregador_disponivel(bancoEntregas)
            case 5:
                entregas_entregador(bancoPedidos, bancoEntregas)
            case 6:
                relatorios(bancoPedidos, bancoEntregas)
            case 7:
                return


def pedidos_pendentes(bancoPedidos):
    
    l.limpar()
    print("\n\t-- PEDIDOS PENDENTES --\n")
    if bancoPedidos == {}:
        print("Nenhum pedido cadastrado no momento.")
    else:
        id_pedido=input("\nDigite o ID do pedido: ")
        for id_pedido in bancoPedidos:
            if bancoPedidos[id_pedido][4] == "Pendente":
                print(f"ID: {id_pedido} | Cliente: {bancoPedidos[id_pedido][0]} | Status: Pendente")
    input("\nPrecione ENTER para prosseguir...")


def pedidos_entregues(bancoPedidos):
    l.limpar()
    print("\n\t-- PEDIDOS ENTREGUES --\n")
    if bancoPedidos == {}:
        print("Nenhum pedido cadastrado no momento.")
    else:
        for id_pedido in bancoPedidos:
            if bancoPedidos[id_pedido][4] == "Entregue":
                print(f"ID: {id_pedido} | Cliente: {bancoPedidos[id_pedido][0]} | Status: Entregue")
    input("\nPressione ENTER para prosseguir...")


def buscar_pedido(bancoPedidos):
    l.limpar()
    print("\n\t-- BUSCAR PEDIDO POR ID --\n")
    id_busca = input("Digite o ID do pedido: ")
    if id_busca in bancoPedidos:
        dados = bancoPedidos[id_busca]
        print(f"\nID: {id_busca} | Cliente: {dados[0]} | Endereço: {dados[1]} | Status: {dados[4]}")
    else:
        print("Pedido não encontrado.")
    input("\nPressione ENTER para prosseguir...")

def listar_pedido(bancoPedidos):
    l.limpar()
    print("\n\t-- LISTAGEM DE PEDIDOS --\n")
    if bancoPedidos == {}:
        print("Nenhum pedido cadastrado no momento.")
    else:
        print(bancoPedidos)
    input("\nPrecione ENTER para prosseguir...")


def entregador_disponivel(bancoEntregas):
    l.limpar()
    print("\n\t-- ENTREGADORES DISPONÍVEIS --\n")
    if bancoEntregas == {}:
        print("Nenhum entregador cadastrado no momento.")
    else:
        for id_entregador in bancoEntregas:
            if bancoEntregas[id_entregador][3] == "Disponível":
                print(f"ID: {id_entregador} | Nome: {bancoEntregas[id_entregador][0]}")
    input("\nPressione ENTER para prosseguir...")


def entregas_entregador(bancoPedidos, bancoEntregas):
    l.limpar()
    print("\n\t-- ENTREGAS DE UM ENTREGADOR --")
    id_entregador = input("\nDigite o ID do entregador: ")
    if bancoEntregas != {}:
        if id_entregador in bancoEntregas:
            pedido_id = bancoEntregas[id_entregador][2]
            if pedido_id in bancoPedidos:
                print(f"\nEntregador: {bancoEntregas[id_entregador][0]} | Pedido: {pedido_id} | Cliente: {pedido_id[0]}")
        else:
            print("Entregador não encontrado.")
    else:
        print("Nenhum entregador cadastrado no momento.")
    input("\nPressione ENTER para prosseguir...")

def relatorios(bancoPedidos, bancoEntregas):
    opcao = 0