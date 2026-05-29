import pedidos as p
import entregas as e
import informacoes as i
import limpar as l
bancoPedidos={}
bancoEntregas={}
prioridade={}
opcao=0
while opcao != 4:
    l.limpar()
    print("\n\t-- MENU PRINCIPAL --")
    print("\n1 - Pedidos")
    print("2 - Entregadores")
    print("3 - Informações")
    print("4 - Sair")

    opcao=int(input("\nEscolha uma opção: "))
    match opcao:

        case 1:
            resultado=p.pedidos(bancoPedidos,bancoEntregas)
            for idPedido,dados in bancoPedidos.items():
                    if dados[2] == "Alta":
                        prioridade[idPedido]=dados
            if resultado != None:
                bancoPedidos,bancoEntregas,id_pedido=resultado
                bancoPedidos,bancoEntregas=i.integrar_pedidoEntregador(bancoPedidos,bancoEntregas,prioridade)
        case 2:  
            id_pedido=0
            result=e.entregadores(bancoPedidos,bancoEntregas,id_pedido)
            for idPedido,dados in bancoPedidos.items():
                    if dados[2] == "Alta":
                        prioridade[idPedido]=dados
            if result != None:
                bancoPedidos,bancoEntregas,id_entregador=result
                bancoPedidos,bancoEntregas=i.integrar_pedidoEntregador(bancoPedidos,bancoEntregas,prioridade)
        case 3:
            i.informacoes(bancoPedidos,bancoEntregas)
        case 4:
            input("\nPressione Enter para sair...")
            l.limpar()
        case _:
            l.limpar()

