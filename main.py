import pedidos as p
import entregas as e
bancoPedidos={}
bancoEntregas={}
opcao=0
while opcao != 4:
    p.limpar()
    print("\n\t-- MENU PRINCIPAL --")
    print("\n1 - Pedidos")
    print("2 - Entregadores")
    print("3 - Informações")
    print("4 - Sair")

    opcao=int(input("\nEscolha uma opção: "))
    match opcao:

        case 1:
            novoBancoPedidos,id_pedido=p.pedidos(bancoPedidos)
            bancoPedidos.update(novoBancoPedidos)
        case 2:  
            entregadoresDisp=[]   
            if bancoPedidos == {}:
               id_pedido=0
            novoBancoEntregas,id_entregador=e.entregadores(bancoEntregas,id_pedido)
            bancoEntregas.update(novoBancoEntregas)
            if bancoEntregas[id_entregador][3] == "Disponível":
                entregadoresDisp.append(bancoEntregas[id_entregador])
        case 3:
            pass
        case 4:
            print("\nPrograma finalizado\n")
            print(novoBancoEntregas)
            print(entregadoresDisp)
        case _:
            p.limpar()

