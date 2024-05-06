# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero a vinte. Seu programa devera ler um numero pelo teclado entre 0 e 20 e mostra-lo por extenso

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero_digitado = int(input('Digite um numero entre 0 e 20: '))

    if numero_digitado < 0 or numero_digitado > 20:
        print('Tente novamente. ')
    else:
        break

print(f'Voce digitou o numero {numeros[numero_digitado]}')