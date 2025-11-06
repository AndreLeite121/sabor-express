from .avaliacao_restaurante import AvaliacaoRestaurante
from .cardapio.bebida import Bebida
from .cardapio.item_cardapio import ItemCardapio
from .cardapio.prato import Prato
from .cardapio.sobremesa import Sobremesa

class Restaurante:
    """ Representa um restaurante e suas características. """
    def __init__(self, nome, categoria, cardapio, avaliacoes):
        """
        Inicializa uma instância da classe Restaurante.

        Entrada:
        - nome (str): Nome do restaurante criado
        - categoria (str): Categoria do restaurante criado
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._cardapio = self.processar_cardapio(cardapio)
        self._ativo = False
        self._avaliacoes = AvaliacaoRestaurante(
            media=avaliacoes["average"],
            avaliacoes_individuais=avaliacoes["individual_ratings"]
        )
    
    def __str__(self):
        """ Retorna uma representação textual da instância """
        return f'{self._nome} | {self._categoria}'
    
    @property
    def ativo(self):
        """ Retorna um símbolo verda de verificação se restaurante ativo e um x vermelho se não """
        return '✅' if self._ativo else '❌'
    
    @property
    def exibir_cardapio(self):
        print(f'\nCardapio do restaurante {self._nome}\n')
        
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome: {item._nome.ljust(25)} | Preço: R${str(item._preco).ljust(20)} | Descrição: {item.descricao}'
                print(mensagem)
            else:
                mensagem = f'{i}. Nome: {item._nome.ljust(25)} | Preço: R${str(item._preco).ljust(20)} | Tamanho: {item.tamanho}'
                print(mensagem)
    
    def calcular_media_avaliacoes(self):
        soma = 0
        for avaliacao in self._avaliacoes.avaliacoes_individuais:
            soma += avaliacao["rating"]
        
        self._avaliacoes.media = soma / len(self._avaliacoes.avaliacoes_individuais)

    def processar_cardapio(self, cardapio_data):
        cardapio = []

        for item in cardapio_data:
            if "tipo" in item:
                if item["tipo"] == "Bebida":
                    cardapio.append(
                        Bebida(
                            nome=item["Item"],
                            preco=item["Price"],
                            tamanho=item["Size"]
                        )
                    )
                elif item["tipo"] == "Sobremesa":
                    cardapio.append(
                        Sobremesa(
                            nome=item["Item"],
                            preco=item["Price"],
                            tipo=item["Type"],
                            tamanho=item["Size"]
                        )
                    )
            else:
                cardapio.append(
                    Prato(
                        nome=item["Item"],
                        preco=item["Price"],
                        descricao=item["Description"]
                    )
                )
                
        return cardapio
    
    def alternar_estado(self):
        """ Altera estado de um restaurando de ativo para desativado ou vice-versa """
        self._ativo = not self._ativo
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)