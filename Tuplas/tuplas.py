# Tuplas sao variaveis compostas imutaveis
# Tuplas sao criadas entre parenteses ()
lanche = ('hamburger', 'suco', 'pizza', 'pudim')

# # Utilizando a funcao range, conseguimos acessar os valores apenas atraves dos indices
# for cont in range(0, len(lanche)):
#     print(f'Vou comer {lanche[cont]} na posicao {cont}')
# print()

# # Sem utilizar funcoes auxiliares na tupla, acessamos apenas os valores
# for comida in lanche:
#     print(comida)
# print()

# # Utilizando a funcao enumerate conseguimes acessar tanto o indice quanto o valor da tupla
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posicao {pos}')

# Metodo sorted (coloca a tupla em ordem e transforma em uma lista []) 
# print(sorted(lanche))

# concatenando tuplas com +, a ordem da concatenacao modifica o resultado final da lista
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b
d = b+a
print(b[-1:2])
# print(c)
# print(d)

# metodo count(x) conta quantas ocorrencias de x existem na tupla
# print(c.count(5))

# index(x) retorna em que indice (posicao) esta a primeiro ocorrencia de x dentro da tupla
# print(c.index(2))

# Tuplas aceitam dados de diferentes tipos
pessoa = ('Felipe', 24)
# print(pessoa)

# apesar das tuplas serem imutaveis elas podem ser apagados por completo utilizando del(nome_tupla)
# del (pessoa)