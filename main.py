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
            try:
                novoBancoPedidos,id_pedido=p.pedidos(bancoPedidos)
                bancoPedidos.update(novoBancoPedidos)
            except:
                pass
        case 2:  
            if bancoPedidos == {}:
               id_pedido=0
            try:
                novoBancoEntregas,id_entregador=e.entregadores(bancoEntregas,id_pedido)
                bancoEntregas.update(novoBancoEntregas)
            except:
                pass
        case 3:
            try:
                i.informacoes(bancoPedidos, bancoEntregas)
            except:
                pass
        case 4:
            print("\nPrograma finalizado\n")
        case _:
            l.limpar()

