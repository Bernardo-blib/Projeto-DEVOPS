
produtos = []


def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"Nome: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Quantidade: {produto['quantidade']}"
        )


def remover_produto():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()
    nome = input("Digite o nome do produto que deseja remover: ")

    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return

    print("Produto não encontrado.")


def calcular_estoque():
    total = sum(
        produto["preco"] * produto["quantidade"]
        for produto in produtos
    )
    print(f"Valor total do estoque: R$ {total:.2f}")


def menu():
    while True:
        print("\n=== SISTEMA DE ESTOQUE ===")
        print("0 - Sair")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Calcular valor do estoque")
        print("4 - Remover produto")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            calcular_estoque()
        elif opcao == "4":
            remover_produto()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
