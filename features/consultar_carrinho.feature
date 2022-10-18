#language: pt
Funcionalidade: Consultar carrinho Amazon

    '''Eu como usuario quero acessar a pagina do carrinho e consultar quais itens estao la'''

    Cenario: Consultar o carrinho da Amazon
    Dado acesso a pagina de um produto na Amazon
    Quando clico no adicionar o produto ao carrinho
    E carrinho e exibido
    Então devo saber quais itens estao no carrinho
