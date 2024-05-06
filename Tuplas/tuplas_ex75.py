# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla e no final mostre
# a) Quantas vezes apareceu o valor 9
# b) Em que posicao foi digitado o primeiro valor 3
# c) Quais foram os numeros pares

num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite o ultimo numero: ')),
)

print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na posicao {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end= ' ')