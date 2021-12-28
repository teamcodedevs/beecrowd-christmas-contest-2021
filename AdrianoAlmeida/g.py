'''input
4
dwight jello 51430
creed beans 263
stanley pretzels 45121
pam brushtool 941
'''
n = int(input())

gifts = {}

while n > 0:
	s = input().split()
	k = ' '.join(s[:-1]).strip()
	v = int(s[-1])
	gifts[k] = v
	n-=1

gifts = {k: v for k, v in sorted(gifts.items(), key=lambda item: item[1])}

for k, v in gifts.items():
	print(f"{k} {v}")
