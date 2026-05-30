import pedidos as p
import limpar as l
import gerarID as g
import informacoes as i

def entregadores(bancoPedidos,bancoEntregas,id_pedido):
    opcao=0
    while opcao != 3:
        l.limpar()
        print("\n\t-- ENTREGADORES --")
        print("\n1 - Cadastrar entregador")
        print("2 - Remover entregador")
        print("3 - Voltar para o menu principal")

        opcao=int(input("\nEscolha uma opção: "))

        match opcao:
            
            case 1:
                entrega=cadastrar(bancoEntregas,id_pedido)
                id_entregador=g.gerar_id(2)
                bancoEntregas[id_entregador]=entrega
                if bancoEntregas == {} or bancoPedidos == {}:
                    return None
                else:
                    return bancoPedidos,bancoEntregas,id_entregador
            case 2:
                remover_entregador(bancoEntregas)
            case 3:
                return
            case _:
                l.limpar()

def cadastrar(bancoEntregas,id_pedido):
    l.limpar()
    entrega=[]
    print("\n\t-- CADASTRO DE ENTREGADOR --")
    nome=input("\nDigite o nome do entregador: ")
    for id_entregador in bancoEntregas.keys():
        while nome == bancoEntregas[id_entregador][0]:
            l.limpar()
            print("\n\t-- CADASTRO DE ENTREGADOR --")
            print("\nEntregador já cadastrado, tente novamente.")
            nome=input("\nDigite o nome do entregador: ")
    entrega.append(nome)
    veiculo=input("Digite o veículo do entregador: ")
    entrega.append(veiculo)
    disponibilidade="Disponível"
    entrega.append(id_pedido)
    entrega.append(disponibilidade)
    num_entregas=0
    entrega.append(num_entregas)
    return entrega

def remover_entregador(bancoEntregas):
    l.limpar()
    print("\n\t-- REMOÇÃO DE ENTREGADOR --")
    if bancoEntregas != {}:
        id=input("\nDigite o ID do entregador que você quer remover: ")
        if id not in bancoEntregas.keys():
            print("\nEntregador não encontrado.")
            input("\nPressione ENTER para prosseguir...")
        else:
            del bancoEntregas[id]
            print("\nEntregador removido com sucesso!")
            input("\nPressione ENTER para prosseguir...")
    else:
        print("\nNenhum entregador cadastrado no momento.")
        input("\nPressione ENTER para prosseguir...")