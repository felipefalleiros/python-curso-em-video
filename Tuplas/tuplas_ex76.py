# Crie um programa que tenha uma tupla unica com nomes de produtos e eseus respectivos precos na sequencia
# No final mostre uma listagem de precos organizando os dados em forma tabular

produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Trasferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-'*40)
print(f'{"Listagem de precos":^40}')
print('-'*40)
for cont in range(len(produtos)):
    if cont % 2 == 0:
        print(f'{produtos[cont]:.<30}', end=' ')
    else:
        print(f'R${produtos[cont]:>7.2f}')