import pytest
from tests.fixtures import sabor_express_object_fixture, sobremesa_fixture
from components.cardapio.sobremesa import Sobremesa

def teste_escolher_restaurante(sabor_express_object_fixture):
    sabor_express = sabor_express_object_fixture
    restaurante_escolhido = sabor_express.escolher_restaurante(1)

    assert restaurante_escolhido._nome == "Restaurante 1"

def teste_escolher_pedido(sabor_express_object_fixture):
    sabor_express = sabor_express_object_fixture
    restaurante_escolhido = sabor_express.escolher_restaurante(1)

    pedido_escolhido = sabor_express.escolher_pedido(restaurante_escolhido, 1)

    assert pedido_escolhido._nome == "Item 1"

@pytest.fixture
def item_teste_para_desconto():
    return Sobremesa("Item Teste", 100.0, "Tipo", "Tam")

def test_calcular_preco_com_desconto(sabor_express_object_fixture, item_teste_para_desconto):
    sabor_express = sabor_express_object_fixture
    item = item_teste_para_desconto

    sabor_express.calcular_preco(item, "S") 

    assert item._preco == 85.0

def test_calcular_preco_sem_desconto(sabor_express_object_fixture, item_teste_para_desconto):
    sabor_express = sabor_express_object_fixture
    item = item_teste_para_desconto

    sabor_express.calcular_preco(item, "N") 
    assert item._preco == 100.0