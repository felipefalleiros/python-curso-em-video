# Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estao na tupla

import random

numeros = (random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))

for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')


