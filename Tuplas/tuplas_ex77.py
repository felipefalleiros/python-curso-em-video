# Crie um programa que tenha uma tupla com varias palvaras. Depois voce deve mostrar para cada palavra quais sao suas vogais

palavras = ('felipe', 'barbara', 'bruno','ane')
for nome in palavras:
    print(f'\nNa palavra {nome} temos', end=' ')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
        