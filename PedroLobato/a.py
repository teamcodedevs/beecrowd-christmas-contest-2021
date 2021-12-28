lines = int(input())
categories = ['Total de Brinquedos',
              'Total de Alimentos',
              'Total de Roupas',
              'Total de Calcados',
              'Total de Eletronicos',
              'Total de Livros',
              'Total de Gadgets',
              'Total de Smartphones',
              'Total de Jogos',
              'Total de Papelaria']
items = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for _ in range(0, lines):
    categoryIndex = int(input().split()[1]) - 1
    items[categoryIndex] += 1

for index, value in enumerate(items):
    print(f'{categories[index]}: {value}')
