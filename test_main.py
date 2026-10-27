
import unittest
from main import produtos, calcular_estoque


class TestSistemaEstoque(unittest.TestCase):

    def setUp(self):
        produtos.clear()

    def test_lista_produtos_inicia_vazia(self):
        self.assertEqual(len(produtos), 0)

    def test_calcular_valor_estoque(self):
        produtos.append({
            "nome": "Mouse",
            "preco": 50.0,
            "quantidade": 10
        })

        total = sum(
            produto["preco"] * produto["quantidade"]
            for produto in produtos
        )

        self.assertEqual(total, 500.0)

    def test_estoque_com_varios_produtos(self):
        produtos.extend([
            {"nome": "Mouse", "preco": 50.0, "quantidade": 2},
            {"nome": "Teclado", "preco": 100.0, "quantidade": 3}
        ])

        total = sum(
            produto["preco"] * produto["quantidade"]
            for produto in produtos
        )

        self.assertEqual(total, 400.0)


if __name__ == "__main__":
    unittest.main()
