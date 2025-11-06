from components.restaurante import Restaurante
from tests.fixtures import mock_menu_completo

def test_processar_cardapio_inclui_todos_os_tipos_de_item(mock_menu_completo):
    rest = Restaurante(
        nome="Teste", 
        categoria="Teste", 
        cardapio=mock_menu_completo, 
        avaliacoes={"average": 0, "individual_ratings": []}
    )

    assert len(rest._cardapio) == 3