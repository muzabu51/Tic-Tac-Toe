def check_straight(game, player):
	
	for i in range(3):
		j = 0 
		if game[i][j]:
			# row check
			if game[i][j] == game[i][j+1] == game[i][j+2]:
				return player
			# column check
			elif game[j][i] == game[j+1][i] == game[j+2][i]:
				return player
			else:
				return 0


def check_diagonal(game, player):
	if game[1][1]:
		if game[0][0] == game[1][1] == game[2][2]:
			return 1
		elif game[0][2] == game[1][1] == game[2][0]:
			return player
		else:
			return 0
