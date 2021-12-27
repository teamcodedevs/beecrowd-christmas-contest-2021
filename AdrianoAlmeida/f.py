'''input
3
529982247-25
529982247-25
123456789-10
'''
n = int(input())


def cpf_validation(cpf):
	for j in range(2):
		s = 0
		for i in range(0, 9+j):
			s += cpf[i]*(10+j-i)
		cd = 11-(s%11)
		cd = 0 if cd == 10 or cd == 11 else cd
		if cd != cpf[9+j]:
			return False
	return True


while n > 0:
	cpf = list(map(int, input().replace('-', '')))
	print("HoHoHoHo!" if cpf_validation(cpf) else "Muahahaha!")
	n-=1