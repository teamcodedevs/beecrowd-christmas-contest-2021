'''input
7.35
10.00
'''
a = float(input())
b = float(input())
c = b-a
c = (c*100)%100
t = [] 

for i in [50, 25, 10, 5, 1]:
	print(f"{int(c//i)} moeda(s) de {i}")
	c %= i