import pytest
from components.cardapio.prato import Prato

@pytest.fixture
def prato_fixture():
    return Prato("Prato Mock", 100.0, "Desc Mock")

def test_aplicar_desconto_prato(prato_fixture):
    prato_fixture.aplicar_desconto()
    assert prato_fixture._preco == 95.0