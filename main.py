import pedidos as p
import entregas as e
import informacoes as i
import limpar as l
bancoPedidos={}
bancoEntregas={}
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
                if resultado != None:
                    novoBancoPedidos,bancoEntregas,id_pedido=resultado
                    bancoPedidos.update(novoBancoPedidos)
                    bancoEntregas.update(novoBancoEntregas)
                    bancoPedidos,bancoEntregas=i.integrar_pedidoEntregador(bancoPedidos,bancoEntregas)
        case 2:  
            id_pedido=0
            result=e.entregadores(bancoPedidos,bancoEntregas,id_pedido)
            if result != None:
                novoBancoPedidos,novoBancoEntregas,id_entregador=result
                bancoEntregas.update(novoBancoEntregas)
                bancoPedidos.update(novoBancoPedidos)
                bancoPedidos,bancoEntregas=i.integrar_pedidoEntregador(bancoPedidos,bancoEntregas)
        case 3:
            i.informacoes(bancoPedidos, bancoEntregas)
        case 4:
            print("\nPrograma finalizado\n")
        case _:
            l.limpar()

