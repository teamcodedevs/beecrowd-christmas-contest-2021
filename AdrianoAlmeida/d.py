'''input
95.45 12 100.00
0.85
0.24
0.65
0.47
0.98
0.67
0.54
0.78
0.35
0.97
1.00
0.12
'''
s = input().split()
cw, nc, aw = float(s[0]), int(s[1]), float(s[2])

while nc:
	c = float(input())
	cw += c
	nc-=1

print(f"{cw:.2f}\nho ho ho" if cw <= aw else f"{cw:.2f}\npapai noel precisa fazer exercicios")