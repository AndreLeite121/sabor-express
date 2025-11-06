import pytest
from components.cardapio.bebida import Bebida

@pytest.fixture
def bebida_fixture():
    return Bebida("Bebida Mock", 100.0, "500ml")

def test_aplicar_desconto_bebida(bebida_fixture):
    bebida_fixture.aplicar_desconto()
    assert bebida_fixture._preco == 92.0