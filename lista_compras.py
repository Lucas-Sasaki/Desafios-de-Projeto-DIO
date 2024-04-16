import textwrap

def menu():
    opcoes = """
    \n
    ================= OPÇÕES =================
    [ad]\tAdicionar Item na Lista
    [rm]\tRemover item da lista
    [lp]\tListar produtos
    [q]\tEncerrar processo
    =>
    """
    return textwrap.dedent(opcoes)


def inserir_item(lista_compra):
    item = input("Informe o produto a ser adicionado na lista: ")
    produto = filtrar_produtos(item, lista_compra)
    if produto:
        print(f"{item} já está na lista de compras!")

    else:
        print(f"{item} adicionado a lista de compras com sucesso!")
        lista_compra.append(item)

    return item


def remover_item(lista_compra):
    item = input("Qual item deseja remover da compra? ")
    produto = filtrar_produtos(item, lista_compra)
    if produto:
        print(f"{item} removido da lista de compras!")
        lista_compra.remove(item)

    else:
        print(f"!!!!!{item} não está presente em sua lista de compras.!!!!!")



def listar_produtos(lista_compra):
    print("================= LISTA DE COMPRAS =================")
    for i, produto in enumerate(lista_compra, start=1):
        linha = f"""
                {i} - {produto}
                """
        print(textwrap.dedent(linha))


def filtrar_produtos(item, lista_compra):
    item_filtrado = [item for produto in lista_compra if produto == item]
    return item_filtrado[0] if item_filtrado else None


def main():
    lista_compra = []

    while True:
        opcao = input(menu())

        if opcao == "ad":
            inserir_item(lista_compra)

        elif opcao == "rm":
            remover_item(lista_compra)

        elif opcao == "lp":
            listar_produtos(lista_compra)

        elif opcao == "q":
            break

        else:
            print("Informe um valor valido")


main()