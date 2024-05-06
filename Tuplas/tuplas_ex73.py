# Crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocacao e depois mostre:
# a) Os 5 primeiros colocados
# b) os ultimos 4 colocados da tabela
# c) Uma lista com os times em ordem alfabetica
# c) Em que posicao na tabela esta o time fortaleza

times = ('Botafogo', 'Atletico-MG', 'Bragantico', 'Athletico-PR', 'Bahia', 'Internacional', 'Cruzeiro', 'Flamengo', 'Gremio', 'Criciuma', 'Fortaleza', 'Palmeiras', 'Juventude', 'Sao Paulo', 'Corinthians', 'Fluminese', 'Vasco da gama', 'EC Vitoria', 'Atletico-GO', 'Cuiaba')

print(f'Lista de times do Brasileirao {times}')
print()
print(f'Os 5 primeiros sao {times[:6]}')
print()
print(f'Os 4 ultimos sao {times[-4:]}')
print()
print(f'Times em ordem alfabetica {sorted(times)}')
print()
print(f'O Fortaleza esta na posicao {times.index('Fortaleza')+1}')