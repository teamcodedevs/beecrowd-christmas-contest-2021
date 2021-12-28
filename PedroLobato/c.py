input_coin = [50, 25, 10, 5, 1]
n = float(input())
m = float(input())
coins = int(format(n - m, '.2f').split('.')[1])

for coin in input_coin:
    print(f'{coins//coin} moeda(s) de {coin}')
    coins %= coin
