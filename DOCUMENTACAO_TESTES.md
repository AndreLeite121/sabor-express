# Documentação de Testes - Sabor Express

Este documento detalha os testes unitários criados para a aplicação Sabor Express, conforme solicitado. O objetivo foi validar a lógica de negócio, garantir a correta implementação das regras de desconto e corrigir bugs existentes na lógica de processamento de dados.

Os testes foram implementados utilizando `pytest`, com dados de mock fornecidos através de `fixtures`.

## 1. Descrição das Mudanças e Correção de Bug

A mudança mais significativa implementada durante este trabalho foi a correção de um bug crítico na classe `Restaurante` e a subsequente validação.

### O Bug: Falha no Processamento do Cardápio

Durante a análise do código, foi identificado que o método `processar_cardapio` na classe `Restaurante` (`components/restaurante.py`) não estava funcionando como esperado.

* **Problema:** O método iterava sobre os dados do menu. Ele corretamente adicionava itens do tipo `Prato` à lista `_cardapio`. No entanto, ao encontrar itens do tipo `Bebida` ou `Sobremesa`, o código **instanciava os objetos, mas esquecia de adicioná-los (`.append()`)** à lista final.
* **Resultado:** Qualquer restaurante criado teria um cardápio contendo *apenas* pratos, ignorando todas as bebidas e sobremesas.

### A Solução (Guiada por Testes)

Para validar e corrigir este bug, foi aplicada uma abordagem de TDD:

1.  **Criação do Teste:** Foi criado o teste `test_processar_cardapio_inclui_todos_os_tipos_de_item` (`tests/test_restaurante.py`).
2.  **Criação da Fixture:** Uma fixture (`mock_menu_completo` em `tests/fixtures.py`) foi criada contendo um Prato, uma Bebida e uma Sobremesa (3 itens).
3.  **Falha (Red):** Ao executar o `pytest` pela primeira vez, o teste falhou (como visto na sua primeira saída, `AssertionError: assert 1 == 3`), provando que apenas 1 dos 3 itens estava sendo processado.
4.  **Correção (Green):** O código em `components/restaurante.py` foi corrigido, adicionando as chamadas `cardapio.append()` que faltavam nos blocos `if item["tipo"] == "Bebida"` e `elif item["tipo"] == "Sobremesa"`.
5.  **Sucesso (Refactor):** Ao rodar o `pytest` novamente, o teste passou, confirmando que o bug foi corrigido e o cardápio agora é processado corretamente.

## 2. Cobertura de Testes Adicional

Além da correção do bug, foram implementados testes unitários para validar outras lógicas de negócio críticas da aplicação:

* **Lógica de Desconto (Itens):** Foram criados testes dedicados para `Prato`, `Bebida` e `Sobremesa`, validando que o método `aplicar_desconto()` de cada classe aplica a porcentagem correta (5%, 8% e 15%, respectivamente).
* **Lógica de Aplicação (Pedido):** Na classe `SaborExpress`, foram adicionados testes para o método `calcular_preco`. Esses testes verificam os dois cenários: quando o usuário informa "S" para o desconto (e o desconto é aplicado) e quando informa "N" (e o preço original é mantido).
* **Lógica de Seleção:** Os testes `teste_escolher_restaurante` e `teste_escolher_pedido` validam que a lógica de seleção de itens a partir dos índices está funcionando como esperado.

## 3. Tabela Resumo dos Testes Implementados

Abaixo está o detalhamento de todos os 8 testes que compõem a suíte de testes final.

| Componente Testado (Classe) | Teste Criado (Nome da Função) | Mocks Necessários (Fixtures) | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| `Restaurante` | `test_processar_cardapio_inclui_todos_os_tipos_de_item` | `mock_menu_completo` | O cardápio processado deve conter 3 itens (Prato, Bebida e Sobremesa). |
| `Prato` | `test_aplicar_desconto_prato` | `prato_fixture` | O preço de 100.0 deve ser 95.0 (desconto de 5%). |
| `Bebida` | `test_aplicar_desconto_bebida` | `bebida_fixture` | O preço de 100.0 deve ser 92.0 (desconto de 8%). |
| `Sobremesa` | `teste_aplicar_desconto_sobremesa` | `sobremesa_fixture` | O preço de 100.0 deve ser 85.0 (desconto de 15%). |
| `SaborExpress` | `teste_escolher_restaurante` | `sabor_express_object_fixture` | O restaurante retornado no índice 1 deve ser "restaurante 1". |
| `SaborExpress` | `teste_escolher_pedido` | `sabor_express_object_fixture` | O item retornado no índice 1 deve ser "Item 1". |
| `SaborExpress` | `test_calcular_preco_com_desconto` | `sabor_express_object_fixture`, `item_teste_para_desconto` | O preço de 100.0 deve ser 85.0 (desconto de 15% da sobremesa aplicado). |
| `SaborExpress` | `test_calcular_preco_sem_desconto` | `sabor_express_object_fixture`, `item_teste_para_desconto` | O preço de 100.0 deve permanecer 100.0 (desconto não aplicado). |