import pedidos as p
banco={}
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
            novoBanco=p.pedidos(banco)
            banco.update(novoBanco)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            p.limpar()

print(novoBanco)