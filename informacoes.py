import limpar as l

def informacoes(bancoPedidos, bancoEntregas):
    opcao = 0
    while opcao != 6:
        l.limpar()
        print("\n\t-- INFORMAÇÕES --")
        print("\n1 - Listar Pedidos")
        print("2 - Listar Entregadores")
        print("3 - Buscar Pedido por cliente")
        print("4 - Números de entregas dos entregadores")
        print("5 - Relatórios Operacionais")
        print("6 - Voltar")
        
        opcao = int(input("\nEscolha uma opção: "))
        match opcao:
            case 1:
                listar_pedido(bancoPedidos,bancoEntregas)
            case 2:
                listar_entregador(bancoEntregas)
            case 3:
                buscar_pedido(bancoPedidos)
            case 4:
               num_entregas(bancoEntregas)
            case 5:
                relatorios(bancoPedidos,bancoEntregas)
            case 6:
                return
            case _:
                l.limpar()

def integrar_pedidoEntregador(bancoPedidos,bancoEntregas,prioridade):
    if prioridade == {}:
        for id_pedido,dadosP in bancoPedidos.items():
            for id_entregador,dadosE in bancoEntregas.items():
                if dadosE[3] == "Disponível" and dadosP[5] == 0 and dadosE[2] == 0 and dadosP[4] == "Pendente":
                    if dadosP[5] == 0 and dadosE[2] == 0:
                        dadosE[2]=id_pedido
                        dadosP[5]=id_entregador
                        bancoPedidos[id_pedido][4]="Em rota"
                        bancoEntregas[id_entregador][3]="Em trabalho"
                        break
    else:
        for id_pedido,dadosP in prioridade.items():
            for id_entregador,dadosE in bancoEntregas.items():
                if dadosE[3] == "Disponível" and dadosP[5] == 0 and dadosE[2] == 0 and dadosP[4] == "Pendente":
                    if dadosP[5] == 0 and dadosE[2] == 0:
                        dadosE[2]=id_pedido
                        dadosP[5]=id_entregador
                        bancoPedidos[id_pedido][4]="Em rota"
                        bancoEntregas[id_entregador][3]="Em trabalho"
                        break
    return bancoPedidos,bancoEntregas
                
def num_entregas(bancoEntregas):
    l.limpar()
    print("\n\t-- NÚMERO DE ENTREGAS DOS ENTREGADORES --")
    if bancoEntregas != {}:
        for id,dados in bancoEntregas.items():
            print(f"\nID: {id} | Nome: {dados[0]} | Número de entregas: {dados[4]}")
        input("\nPrecione ENTER para prosseguir...")
    else:
        print("\nNenhum entregador cadastrado no momento.")
        input("\nPrecione ENTER para prosseguir...")
    

def buscar_pedido(bancoPedidos):
    l.limpar()
    print("\n\t-- BUSCAR PEDIDO POR NOME DO CLIENTE --\n")
    if bancoPedidos == {}:
        print("Nenhum pedido cadastrado no momento.")
    else:
        nome = input("Digite o nome do cliente do pedido: ")
        for id_pedido,dados in bancoPedidos.items():
            if dados[0] == nome:
                print(f"\nID: {id_pedido} | Cliente: {dados[0]} | Endereço: {dados[1]} | Prioridade: {dados[2]} | Descrição: {dados[3]} | Status: {dados[4]} | ID do entregador: {dados[5]}")
            else:
                print("\nPedido não encontrado.")
    input("\nPressione ENTER para prosseguir...")

def listar_entregador(bancoEntregas):
    l.limpar()
    print("\n\t-- LISTAGEM DE ENTREGADORES --")
    if bancoEntregas == {}:
        print("\nNenhum entregador cadastrado no momento.")
    else:
        print("\n-- ENTREGADORES DISPONÍVEIS --")
        for id_entregador in bancoEntregas:
            if bancoEntregas[id_entregador][3] == "Disponível":
                print(f"\nID: {id_entregador} | Nome: {bancoEntregas[id_entregador][0]} | Veículo: {bancoEntregas[id_entregador][1]} | Status: {bancoEntregas[id_entregador][3]} | Número de entregas: {bancoEntregas[id_entregador][4]}")
        print("\n-- ENTREGADORES EM TRABALHO --")
        for id_entregador in bancoEntregas:
            if bancoEntregas[id_entregador][3] == "Em trabalho":
                print(f"\nID: {id_entregador} | Nome: {bancoEntregas[id_entregador][0]} | Veículo: {bancoEntregas[id_entregador][1]} | Status: {bancoEntregas[id_entregador][3]} | Número de entregas: {bancoEntregas[id_entregador][4]}")
    input("\nPrecione ENTER para prosseguir...")

def listar_pedido(bancoPedidos,bancoEntregas):
    l.limpar()
    print("\n\t-- LISTAGEM DE PEDIDOS --")
    if bancoPedidos == {}:
        print("\nNenhum pedido cadastrado no momento.")
    else:
        print("\n-- PEDIDOS PENDENTES --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] == "Pendente":
                print(f"\nID: {id_pedido} | Cliente: {dados[0]} | Descrição: {dados[3]} | Endereço: {dados[1]} | Prioridade: {dados[2]} | Status: {dados[4]}")
        print("\n-- PEDIDOS EM ROTA --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] == "Em rota":
                print(f"\nID: {id_pedido} | Cliente: {bancoPedidos[id_pedido][0]} | Descrição: {dados[3]} | Endereço: {dados[1]} | Prioridade: {dados[2]}  | Status: {dados[4]} | ID_Entregador: {dados[5]}")
        print("\n-- PEDIDOS ENTREGUES --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] == "Entregue":
                print(f"\nID: {id_pedido} | Cliente: {bancoPedidos[id_pedido][0]} | Descrição: {dados[3]} | Endereço: {dados[1]} | Prioridade: {dados[2]} | Status: {dados[4]}")
        print("\n-- PEDIDOS CANCELADOS --")
        for id_pedido,dados in bancoPedidos.items():
            if dados[4] == "Cancelado":
                print(f"\nID: {id_pedido} | Cliente: {bancoPedidos[id_pedido][0]} | Status: {dados[4]} | Descrição: {dados[3]} | Endereço: {dados[1]} | Prioridade: {dados[2]} | ID_Entregador: {dados[5]}")
    input("\nPrecione ENTER para prosseguir...")


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
                maior_num_entregas(bancoEntregas)
            case 5:
                return
            
def total_pedidos(bancoPedidos):
    l.limpar()
    print("\n\t-- TOTAL DE PEDIDOS --\n")
    total = len(bancoPedidos)
    print(f"Total: {total} pedidos")
    input("\nPressione ENTER para prosseguir...")


def quantidade_status(bancoPedidos):
    l.limpar()
    print("\n\t-- PEDIDOS POR STATUS --\n")
    pendente = 0
    em_rota = 0
    entregue = 0
    cancelado = 0
    
    for id_pedido in bancoPedidos.keys():
        status = str(bancoPedidos[id_pedido][4])
        if status == "Pendente":
            pendente = pendente + 1
        else:
            if status == "Em Rota":
                em_rota = em_rota + 1
            else:
                if status == "Entregue":
                    entregue = entregue + 1
                else:
                    if status == "Cancelado":
                        cancelado = cancelado + 1
    
    print(f"Pendente: {pendente}")
    print(f"Em Rota: {em_rota}")
    print(f"Entregue: {entregue}")
    print(f"Cancelado: {cancelado}")
    input("\nPressione ENTER para prosseguir...")


def alta_prioridade(bancoPedidos):
    l.limpar()
    print("\n\t-- PEDIDOS ALTA PRIORIDADE --\n")
    for id_pedido in bancoPedidos:
        if bancoPedidos[id_pedido][2] == "Alta":
            print(f"ID: {id_pedido} | Cliente: {bancoPedidos[id_pedido][0]}")
    input("\nPressione ENTER para prosseguir...")


def maior_num_entregas(bancoEntregas):
    l.limpar()
    print("\n\t-- ENTREGADOR COM MAIOR NÚMERO DE ENTREGAS --\n")
    if bancoEntregas != {}:
        primeira_chave = list(bancoEntregas.keys())[0]
        print(f"Entregador: {bancoEntregas[primeira_chave][0]}")
    else:
        print("Nenhum entregador cadastrado.")
    input("\nPressione ENTER para prosseguir...")