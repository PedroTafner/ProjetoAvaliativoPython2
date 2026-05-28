import pedidos as p
import limpar as l
import gerarID as g
import informacoes as i
def entregadores(bancoPedidos,bancoEntregas,id_pedido):
    opcao=0
    while opcao != 4:
        l.limpar()
        print("\n\t-- ENTREGADORES --")
        print("\n1 - Cadastrar entregador")
        print("2 - Listar entregadores")
        print("3 - Remover entregador")
        print("4 - Voltar para o menu principal")

        opcao=int(input("\nEscolha uma opção: "))

        match opcao:
            
            case 1:
                entrega=cadastrar(id_pedido)
                id_entregador=g.gerar_id(2)
                bancoEntregas[id_entregador]=entrega
                if bancoEntregas == {} or bancoPedidos == {}:
                    return None
                else:
                    return bancoPedidos,bancoEntregas,id_entregador
            case 2:
                listar(bancoEntregas)
            case 3:
                pass
            case 4:
                pass
            case _:
                pass

def cadastrar(id_pedido):
    l.limpar()
    entrega=[]
    print("\n\t-- CADASTRO DE ENTREGADOR --")
    nome=input("\nDigite o nome do entregador: ")
    entrega.append(nome)
    veiculo=input("Digite o veículo do entregador: ")
    entrega.append(veiculo)
    disponibilidade="Disponível"
    entrega.append(id_pedido)
    entrega.append(disponibilidade)
    return entrega

def listar(bancoEntregas):
    l.limpar()
    print("\n\t-- LISTAGEM DE PEDIDOS --\n")
    if bancoEntregas == {}:
        print("Nenhum pedido cadastrado no momento.")
    else:
        print(bancoEntregas)
    input("\nDigite ENTER para prosseguir...")