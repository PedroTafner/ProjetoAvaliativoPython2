import limpar as l

def informacoes(bancoPedidos, bancoEntregas):
    opcao = 0
    while opcao != 6:
        l.limpar()
        print("\n\t-- INFORMAÇÕES --")
        print("\n1 - Listar Pedidos")
        print("2 - Buscar Pedido por nome do cliente")
        print("3 - Entregador Disponível")
        print("4 - Todas as Entregas de um Entregador")
        print("5 - Relatórios Operacionais")
        print("6 - Voltar")
        
        opcao = int(input("\nEscolha uma opção: "))
        match opcao:
            case 1:
                listar_pedido(bancoPedidos)
            case 2:
                buscar_pedido(bancoPedidos)
            case 3:
                entregador_disponivel(bancoEntregas)
            case 4:
                entregas_entregador(bancoPedidos,bancoEntregas)
            case 5:
                relatorios(bancoPedidos,bancoEntregas)
            case 6:
                return
            case _:
                l.limpar()


def buscar_pedido(bancoPedidos):
    l.limpar()
    print("\n\t-- BUSCAR PEDIDO POR NOME DO CLIENTE --\n")
    if bancoPedidos == {}:
        print("Nenhum pedido cadastrado no momento.")
    else:
        nome = input("Digite o nome do cliente do pedido: ")
        for id_pedido,dados in bancoPedidos.items():
            if dados[0] == nome:
                print(f"\nID: {id_pedido} | Cliente: {dados[0]} | Endereço: {dados[1]} | Status: {dados[4]}")
            else:
                print("\nPedido não encontrado.")
    input("\nPressione ENTER para prosseguir...")

def listar_pedido(bancoPedidos):
    l.limpar()
    print("\n\t-- LISTAGEM DE PEDIDOS --")
    if bancoPedidos == {}:
        print("\nNenhum pedido cadastrado no momento.")
    else:
        print("\n-- PEDIDOS PENDENTES --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] == "Pendente":
                print(f"\nID: {id_pedido} | Cliente: {dados[0]} | Status: {dados[4]}")
        print("\n-- PEDIDOS ENTREGUES --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] == "Entregue":
                print(f"\nID: {id_pedido} | Cliente: {bancoPedidos[id_pedido][0]} | Status: {dados[4]}")
        print("\n-- PEDIDOS EM ROTA --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] == "Em rota":
                print(f"\nID: {id_pedido} | Cliente: {bancoPedidos[id_pedido][0]} | Status: {dados[4]}")

    input("\nPrecione ENTER para prosseguir...")


def entregador_disponivel(bancoEntregas):
    l.limpar()
    print("\n\t-- ENTREGADORES DISPONÍVEIS --\n")
    if bancoEntregas != {}:
        for id_entregador in bancoEntregas:
            if bancoEntregas[id_entregador][3] == "Disponível":
                print(f"ID: {id_entregador} | Nome: {bancoEntregas[id_entregador][0]}")
    else:
        print("Nenhum entregador cadastrado no momento.")
    input("\nPressione ENTER para prosseguir...")


def entregas_entregador(bancoPedidos, bancoEntregas):
    l.limpar()
    print("\n\t-- ENTREGAS DE UM ENTREGADOR --")
    if bancoEntregas != {}:
        id_entregador = input("\nDigite o ID do entregador: ")
        if id_entregador in bancoEntregas:
            pedido_id = bancoEntregas[id_entregador][2]
            if pedido_id in bancoPedidos:
                print(f"\nEntregador: {bancoEntregas[id_entregador][0]} | Pedido: {pedido_id} | Cliente: {pedido_id[0]}")
        else:
            print("\nEntregador não encontrado.")
    else:
        print("\nNenhum entregador cadastrado no momento.")
    input("\nPressione ENTER para prosseguir...")

def relatorios(bancoPedidos, bancoEntregas):
    opcao = 0
    while opcao != 5:
        l.limpar()
        print("\n\t-- RELATÓRIOS OPERACIONAIS --")
        print("\n1 - Total de Pedidos")
        print("2 - Quantidade por Status")
        print("3 - Alta Prioridade")
        print("4 - Entregador com Maior Número de Entregas")
        print("5 - Voltar")
        
        opcao = int(input("\nEscolha uma opção: "))
        match opcao:
            case 1:
                total_pedidos(bancoPedidos)
            case 2:
                quantidade_status(bancoPedidos)
            case 3:
                alta_prioridade(bancoPedidos)
            case 4:
                maior_entregas(bancoEntregas)
            case 5:
                return