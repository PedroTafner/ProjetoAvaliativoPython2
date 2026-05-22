import pedidos as p
def entregadores(bancoEntregadores,id_pedido):
    p.limpar()
    opcao=0
    while opcao != 2:
        print("\n\t-- ENTREGADORES --")
        print("\n1 - Cadastrar entregador")
        print("2 - Voltar para o menu principal")

        opcao=int(input("\nEscolha uma opção: "))

        match opcao:
            
            case 1:
                entrega=cadastrar_entregador(id_pedido)
                id_entregador=p.gerar_id(2)
                bancoEntregadores[id_entregador]=entrega
                return bancoEntregadores,id_entregador
            case 2:
                return

def cadastrar_entregador(id_pedido):
    p.limpar()
    entrega=[]
    print("\n\t-- CADASTRO DE ENTREGADOR --")
    nome=input("Digite o nome do entregador: ")
    entrega.append(nome)
    veiculo=input("Digite o veículo do entregador: ")
    entrega.append(veiculo)
    disponibilidade="Disponível"
    entrega.append(id_pedido)
    entrega.append(disponibilidade)
    return entrega