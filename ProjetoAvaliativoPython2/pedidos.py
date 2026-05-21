import random as r
import os
def pedidos(banco):
    limpar()

    opcao=0
    while opcao != 3:
        print("\n\t-- PEDIDOS --")
        print("\n1 - Cadastrar pedido")
        print("2 - Atualizar pedido")
        print("3 - Voltar para o Menu Principal")

        opcao=int(input("\nEscolha uma opção: "))
        match opcao:
            case 1:
                pedido=cadastrar_pedido()
                id_pedido=gerar_id(1)
                banco[id_pedido]=pedido
                return  banco
            case 2:
                pass
            case 3:
                return
            case _:
                limpar()

   
def cadastrar_pedido():
    limpar()
    pedido=[]
    print("\n\t-- CADASTRO DE PEDIDOS --")
    nome=input("\nDigite o nome do cliente:  ")
    pedido.append(nome)
    endereco=input("Digite o endereço do cliente: ")
    pedido.append(endereco)
    prioridade=input("Digite a prioridade do pedido (Alta ou Normal): ")
    pedido.append(prioridade)
    descricao=input("Digite a descrição do pedido: ")
    pedido.append(descricao)
    status="Pendente"
    pedido.append(status)
    id_entregador=gerar_id(2)
    pedido.append(id_entregador)
    return pedido
def gerar_id(opcao):
    id = ""
    if opcao == 1:
        alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        letra = r.randint(0,25)
        letra = alfabeto.pop(letra)
        id += str(letra)
        for _ in range(4):
            id += str(r.randint(0, 9))
        return id
    else:
        for _ in range(4):
            id += str(r.randint(0, 9))
        return id

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')