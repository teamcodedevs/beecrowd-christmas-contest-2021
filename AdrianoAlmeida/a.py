'''input
10
Boneca 1
TheSims 9
Carrinho 1
Blusa 3
Sapatilha 4
Relogio 7
Teclado 7
Televisao 5
Bola 1
FoneOuvido 7
'''
items = (
	'Brinquedos',
	'Alimentos',
	'Roupas',
	'Calcados',
	'Eletronicos',
	'Livros',
	'Gadgets',
	'Smartphones',
	'Jogos',
	'Papelaria',
)

d = {i: 0 for i in range(10)}

n = int(input())

while n > 0:
	id = int(input().split()[-1])-1
	d[id] += 1
	n-=1

for item, total in zip(items, d.values()):
	print(f"Total de {item}: {total}")
