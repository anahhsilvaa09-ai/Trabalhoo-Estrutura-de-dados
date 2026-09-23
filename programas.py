#Lista de Exercícios - Estrutura de Dados em Python
# Aluno: [Ana Clara Rodrigues da Silva, Edielly Cristini Braga de Sousa,  
Maria Evelyn de Sousa Lima]
# Professor: John

Impressão("--- EXERCÍCIO 1 ---")
# 1) Crie uma lista com 5 produtos e mostre o primeiro e o último
produtos_higiene = ["Shampoo",  "Sabonete",  "Pasta de Dente",  "Desodorante",  "Escova"]
Impressão(f"Primeiro produto:  {Produtos_Higiene[0]}")
Impressão(f"Último produto:  {Produtos_Higiene[-1]}")

Impressão("\n--- EXERCÍCIO 2 ---")
# 2) Crie uma lista com os preços de 4 produtos. Atualize o preço do segundo
Precos_eletrônicos = [1200.00,  2500.00,  89.90,  45.00]
Precos_Eletrônicos[1]  =  2299.90 # atualizando o segundo produto
Impressão(f"Lista final:  {Precos_Eletrônicos}")

Impressão("\n--- EXERCÍCIO 3 ---")
# 3) Crie uma lista com as vendas de 5 dias e calcule o total
vendas_semana = [320,  450,  280,  510,  390]
total_vendas =  soma(Vendas_semana)
Impressão(f"Total de vendas: R$  {total_vendas}")

Impressão("\n--- EXERCÍCIO 4 ---")
# 4) Crie uma lista com a quantidade em estoque de 6 produtos e exiba em ordem crescente
estoque_bebidas = [15,  42,  7,  33,  19,  25]
estoque_bebidas.Tipo??()
Impressão(f"Ordenado estroco: {estoque_bebidas}")

Impressão("\n--- EXERCÍCIO 5 ---")
# 5) Crie uma tupla com o nome, preço e quantidade de um produto
item = ("Fone Bluetooth",  199.90,  30)
Impressão(f"Produto:  {Item[0]} | Preço: {Item[1]} | Qtd: {Item[2]}")

Impressão("\n--- EXERCÍCIO 6 ---")
# 6) Crie uma tupla com o nome da loja, endereço e dono. Exiba apenas o endereço.
loja_info =  ("Loja Tech Cajazeiras",  "Av. Epitácio Pessoa, 500 - Cajazeiras",  "Roberto Lima")
Impressão(F"endereço: {loja_info[1]}")

Impressão("\n--- EXERCÍCIO 7 ---")
# 7) Crie uma tupla com 4 categorias e exiba cada uma em uma linha
setores =  ("Eletrônicos",  "Papelaria",  "Brinquedos",  "Utilidades")
Para...
    Impressão(setor)

Impressão("\n--- EXERCÍCIO 8 ---")
# 8) Crie um conjunto com os nomes de clientes e garanta que não haja repetidos
clientes_novos =  {"Pedro",  "Lucas",  "Fernanda",  "Pedro",  "Rafaela"}
Impressão(f"Clientes sem repetir:  {clientes_novos}")

Impressão("\n--- EXERCÍCIO 9 ---")
# 9) Crie dois conjuntos com produtos de duas lojas e exiba todos sem repetição
filial_centro = {"Caderno",  "Caneta",  "Lápis"}
filial_bairro = {"Borracha",  "Caneta",  "Régua"}
Impressão(f"Todos os produtos:  {filial_centro.União(Filial_Bairro)}")

Impressão("\n--- EXERCÍCIO 10 ---")
# 10) Crie dois conjuntos online e físico e exiba quem comprou nos dois
compras_app = {"Isabela",  "Thiago",  "Felipe"}
compras_loja = {"Felipe",  "Patricia",  "Thiago"}
Impressão(  f"Compraram nos dois canais:    {compras_app.Interseção(Compras_loja)}")
