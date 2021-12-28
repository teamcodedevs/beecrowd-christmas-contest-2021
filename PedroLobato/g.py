d = {}
n = int(input())
for _ in range(n):
    name, gift, t  = input().split()
    d[f'{name} {gift}'] = int(t)

d = dict(sorted(d.items(), key=lambda item: item[1]))

for key, value in d.items():
    print(f'{key} {value}')
