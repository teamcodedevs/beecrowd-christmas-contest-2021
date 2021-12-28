'''input
.***....
*...*...
....*...
*..K*...
.*.*....
..*...**
*..*....
......*.
'''

board_in = []
board_ou = []

for i in range(8):
	row = input()
	board_in.append([])
	board_ou.append([])
	for cell in row:
		board_in[i].append(cell)
		board_ou[i].append(0)

def valid_pos(i, j):
	if i<0 or i > 7:
		return False
	if j<0 or j > 7:
		return False
	return True


for i in range(8):
	for j in range(8):
		if board_in[i][j] == '*' or board_in[i][j] == 'K':
			board_ou[i][j] = board_in[i][j]
			continue

		r, c = i-1, j-2
		if valid_pos(r, c):
			if board_in[r][c] == '*':
				board_ou[i][j] += 1

		r, c = i-2, j-1
		if valid_pos(r, c):
			if board_in[r][c] == '*':
				board_ou[i][j] += 1

		r, c = i-2, j+1
		if valid_pos(r, c):
			if board_in[r][c] == '*':
				board_ou[i][j] += 1

		r, c = i-1, j+2
		if valid_pos(r, c):
			if board_in[r][c] == '*':
				board_ou[i][j] += 1

		r, c = i+1, j+2
		if valid_pos(r, c):
			if board_in[r][c] == '*':
				board_ou[i][j] += 1

		r, c = i+2, j+1
		if valid_pos(r, c):
			if board_in[r][c] == '*':
				board_ou[i][j] += 1

		r, c = i+2, j-1
		if valid_pos(r, c):
			if board_in[r][c] == '*':
				board_ou[i][j] += 1

		r, c = i+1, j-2
		if valid_pos(r, c):
			if board_in[r][c] == '*':
				board_ou[i][j] += 1


for i in range(8):
	for j in range(8):
		print(board_ou[i][j], end='')
	print()