p, q, f = map(float, input().split())
total = 0.00
for i in range(int(q)):
    total += float(input())
ptotal = p+total
print(f"{ptotal:.2f}\n{'ho ho ho' if ptotal <= f else 'papai noel precisa fazer exercicios'}")
