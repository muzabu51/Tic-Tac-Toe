def drawboard(size, gameplay):
	ho = '----'.center(6)*size
	for i in gameplay:
		print(ho)
		print(f'|  {i[0]}  |  {i[1]}  |  {i[2]}  |')
	print(('----'.center(6))*size)
