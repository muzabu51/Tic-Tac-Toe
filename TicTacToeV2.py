import CheckWin as chk
import DrawBoard as draw

conv = {1:'X', 2:'O'}
play = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
ref = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def Index(pos):
	i = int(pos / 3) - 1 if not pos % 3  else int(pos / 3)
	j = (pos % 3) - 1
	return i, j


def gameplay():
	count = 0
	straight, diag = (0, 0)
	print('Reference grid'.center(18))
	draw.drawboard(3, ref)
	while (not (straight and diag)) or count < 9:
		print()
		print('Player 1 is X and Player 2 is O')
		inp1 = int(input('Player 1 enter your position on the grid (1 - 9): '))
		i1, j1 = Index(inp1)
		print()
		play[i1][j1] = conv[1]
		draw.drawboard(3, play)
		straight = chk.check_straight(play, 1)
		diag = chk.check_diagonal(play, 1)
		if straight or diag:
			print('Player 1 has won')
			break
		print()
		inp2 = int(input('Player 2 enter your position on the grid (1 - 9): '))
		i2, j2 = Index(inp2)
		print()
		play[i2][j2] = conv[2]
		draw.drawboard(3, play)
		straight = chk.check_straight(play, 2)
		diag = chk.check_diagonal(play, 2)
		if straight or diag:
			print('Player 2 has won')
			break
		count += 1

gameplay()
