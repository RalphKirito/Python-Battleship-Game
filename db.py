import time, os, platform

# LINES: 24

# Animation
def animateIn(size):
	osclr()
	if size == 'full':
		size = 24

	if int(size) % 2 == 0:
		for frame in range((size // 2) - 1):
			osclr()
			if frame != 10:
				print('\n' * (9 - frame))
			bar('top')
			spc(frame * 2)
			bar('bottom')
			if frame != 10:
				print('\n' * (9 - frame))
			time.sleep(0.01)
	else:
		osclr()
		print('\n' * 9)
		bar('top')
		bar('bottom')
		print('\n' * 9)
		time.sleep(0.01)
		for frame in range(size // 2):
			osclr()
			print('\n' * (9 - frame))
			bar('top')
			spc(1 + (frame * 2))
			bar('bottom')
			print('\n' * (8 - frame))
			time.sleep(0.01)

def animateOut(size):
	osclr()
	if size == 'full':
		size = 24

	if int(size) % 2 == 0:
		for frame in range((size // 2) - 1, -1, -1):
			osclr()
			if frame != 10:
				print('\n' * (9 - frame))
			bar('top')
			spc(frame * 2)
			bar('bottom')
			if frame != 10:
				print('\n' * (9 - frame))
			time.sleep(0.01)
	else:
		for frame in range(size // 2, -1, -1):
			osclr()
			print('\n' * (9 - frame))
			bar('top')
			spc(1 + (frame * 2))
			bar('bottom')
			print('\n' * (8 - frame))
			time.sleep(0.01)
		osclr()
		print('\n' * 9)
		bar('top')
		bar('bottom')
		print('\n' * 9)
		time.sleep(0.01)

# Formatting
def osclr():
	if platform.system() == 'Windows':
		os.system('cls');
	else:
		os.system('clear');

def center(text):
	print('{:^79}'.format(text))

def bar(pos):
	if pos == 'mid':
		print('|' + '-' * 77 + '|')
	elif pos == 'top':
		print("." + ('-' * 77) + '.')
	elif pos  == 'bottom':
		print("\'" + ('-' * 77) + '\'')
	elif pos == 'bar':
		print("-" * 78)

def halfBar(pos):
	if pos == 'top':
		print("." + ('-' * 39) + '.', end='')
		print(('-' * 37) + '.')

	elif pos == 'bottom':
		print("\'" + ('-' * 39) + '\'', end='')
		print(('-' * 37) + '\'')

def cont(text):
	print('| ' + '{:^75}'.format(text) + ' |')

def halfCont(text1,text2):
	print('|' + '{:^39}'.format(text1) + '|', end='')
	print('{:^37}'.format(text2) + '|', end='\n')

def spc(lines):
	for i in range(lines):
		cont('')

def alert(body):
	osclr()
	print('\n' * 8)
	bar('top')
	cont("ERROR!")
	cont(body)
	bar('bottom')
	print('\n' * 8)
	time.sleep(0.8)

def win(body):
	osclr()
	print('\n' * 8)
	bar('top')
	cont("NOTICE")
	cont(body)
	bar('bottom')
	print('\n' * 8)
	time.sleep(1)
def wait(body):
	osclr()
	print('\n' * 8)
	bar('top')
	cont("PLEASE WAIT")
	cont(body)
	bar('bottom')
	print('\n' * 8)
	time.sleep(2)

# Process
def splash():
	osclr()
	bar('top')
	spc(6)

	cont('{:<20}'.format("         _~_"))
	cont('{:<20}'.format("      __(__(__"))
	cont('{:<20}'.format("     (_((_((_("))
	cont('{:<20}'.format("   \=-:--:--:--."))
	cont('{:<20}'.format("____\_o__o__o_/____"))
	cont('{:<20}'.format("  BATTLESHIP GAME"))

	spc(6)
	cont('Developed by: Ralph Silaya')
	cont('')
	bar('bottom')
	#time.sleep(10)
	time.sleep(2)

def mainMenu():
	osclr()
	bar('top')
	cont('{:<20}'.format("         _~_"))
	cont('{:<20}'.format("      __(__(__"))
	cont('{:<20}'.format("     (_((_((_("))
	cont('{:<20}'.format("   \=-:--:--:--."))
	cont('{:<20}'.format("____\_o__o__o_/____"))
	cont('{:<20}'.format("  BATTLESHIP GAME"))
	spc(2)

	cont('{:<40}'.format("[1] NEW GAME"))
	cont('{:<40}'.format("    Starts a new game."))
	cont('{:<40}'.format("[2] LOAD GAME"))
	cont('{:<40}'.format("    Load an existing game."))
	cont('{:<40}'.format("[3] HIGH SCORES"))
	cont('{:<40}'.format("    View previous game high scores."))
	cont('{:<40}'.format("[4] HOW TO PLAY"))
	cont('{:<40}'.format("    View instructions to play the game."))
	cont('{:<40}'.format("[5] CREDITS"))
	cont('')
	cont('{:<40}'.format("[6] EXIT"))
	spc(1)
	bar('bottom')

def pauseMenu(saveOn):
	pause = ['1','2','3','4']

	animateIn(13)
	osclr()

	print('\n' * 4)
	bar('top')
	cont('{:<20}'.format("          _~_"))
	cont('{:<20}'.format("       __(__(__"))
	cont('{:<20}'.format("      (_((_((_("))
	cont('{:<20}'.format("    \=-:--:--:--."))
	cont('{:<20}'.format(" ____\_o__o__o_/____"))
	cont('{:<20}'.format("BATTLESHIP GAME PAUSE"))
	spc(1)
	cont('{:<40}'.format("[1] BACK TO GAME"))
	cont('{:<40}'.format("[2] SAVE GAME"))
	cont('{:<40}'.format("[3] HOW TO PLAY"))
	cont('{:<40}'.format("[4] BACK TO MAIN MENU"))
	bar('bottom')
	print('\n' * 3)
	pauseChoice = input("  Enter your choice: ")

	if pauseChoice == '2' and saveOn == False:
		alert("Please position all your battleships first before saving!")
		pauseMenu(saveOn)
	elif pauseChoice in pause:
		return pauseChoice
	else:
		alert("You have entered an invalid menu item!")
		pauseMenu(saveOn)

# Game Proper
def includeZero(colname,grid,gridAI):
	for column in range(6):
		for row in range(6):
			grid[colname[column] + str(row + 1)] = '0'
			gridAI[colname[column] + str(row + 1)] = '0'

def chkStat(grid, cell):
	if grid[cell] == '0': # idle
		return ' '
	elif grid[cell] == '1': # missed
		return 'X'
	elif grid[cell] == 'A' or grid[cell] == 'B' or grid[cell] == 'C':
		return 'O'
	elif grid[cell] == 'X' or grid[cell] == 'Y':
		return ' '
	elif grid[cell] == 'Z':
		return ' '
	elif grid[cell] == 'O':
		return '*'

def printGrid(colname, grid, gridAI):
	#animateIn('full')
	osclr()
	halfBar('top')
	halfCont("PLAYER'S BATTLE SEA", "OPPONENT'S BATTLE SEA")

	# Player
	print('| ', end=' ')
	for col in range(len(colname)):
		print('', '{:^5}'.format(colname[col]),end='')
	print(' |', end='')
	# AI
	for col in range(len(colname)):
		print('', '{:^5}'.format(colname[col]), end='')
	print(' |')

	
	for rows in range(6):
		# Player
		print('|', end='  ')
		for top in range(len(colname)):
			print(' .---.', end='')
		print(' |', end='')
		# AI
		for top in range(len(colname)):
			print(' .---.', end='')
		print(' |')

		# Player
		print('|' ,rows + 1, end='')
		for mid in range(len(colname)):
			print(' |', chkStat(grid, colname[mid] + str(rows + 1)), '|', end='')
		print(' |', end='')
		# AI
		for mid in range(len(colname)):
			print(' |', chkStat(gridAI, colname[mid] + str(rows + 1)), '|', end='')
		print(' |')

		# Player
		print('|', end='  ')
		for bot in range(len(colname)):
			print(" \'---\'", end='')
		print(' |', end='')
		# AI
		for bot in range(len(colname)):
			print(" \'---\'", end='')
		print(' |')
	halfBar('bottom')

def chkShipExist(cell,colname,grid, dimension):
	restriction = []

	# Check if out of sea
	if (colname.index(cell[0]) + dimension) > 5:
		restriction.append('E')
	if (colname.index(cell[0]) - dimension) < 0:
		restriction.append('W')
	if int(cell[1]) + dimension > 6:
		restriction.append('S')
	if int(cell[1]) - dimension < 1:
		restriction.append('N')

	# Check if adjacent ship exist
	if 'E' not in restriction and (grid[colname[colname.index(cell[0]) + dimension] + cell[1]] == 'A' or \
								   grid[colname[colname.index(cell[0]) + dimension] + cell[1]] == 'B' or \
								   grid[colname[colname.index(cell[0]) + dimension] + cell[1]] == 'C' or \
								   grid[colname[colname.index(cell[0]) + dimension] + cell[1]] == 'X' or \
								   grid[colname[colname.index(cell[0]) + dimension] + cell[1]] == 'Y' or \
								   grid[colname[colname.index(cell[0]) + dimension] + cell[1]] == 'Z' or \
								   (dimension == 2 and (grid[colname[colname.index(cell[0]) + (dimension - 1)] + cell[1]] == 'C')) or \
								   (dimension == 2 and (grid[colname[colname.index(cell[0]) + (dimension - 1)] + cell[1]] == 'X')) or \
								   (dimension == 2 and (grid[colname[colname.index(cell[0]) + (dimension - 1)] + cell[1]] == 'Y')) or \
								   (dimension == 2 and (grid[colname[colname.index(cell[0]) + (dimension - 1)] + cell[1]] == 'Z'))):
		restriction.append('E')

	if 'W' not in restriction and (grid[colname[colname.index(cell[0]) - dimension] + cell[1]] == 'A' or \
								   grid[colname[colname.index(cell[0]) - dimension] + cell[1]] == 'B' or \
								   grid[colname[colname.index(cell[0]) - dimension] + cell[1]] == 'C' or \
								   grid[colname[colname.index(cell[0]) - dimension] + cell[1]] == 'X' or \
								   grid[colname[colname.index(cell[0]) - dimension] + cell[1]] == 'Y' or \
								   grid[colname[colname.index(cell[0]) - dimension] + cell[1]] == 'Z' or \
								   (dimension == 2 and (grid[colname[colname.index(cell[0]) - (dimension - 1)] + cell[1]] == 'C')) or \
								   (dimension == 2 and (grid[colname[colname.index(cell[0]) - (dimension - 1)] + cell[1]] == 'X')) or \
								   (dimension == 2 and (grid[colname[colname.index(cell[0]) - (dimension - 1)] + cell[1]] == 'Y')) or \
								   (dimension == 2 and (grid[colname[colname.index(cell[0]) - (dimension - 1)] + cell[1]] == 'Z'))):
		restriction.append('W')

	if 'S' not in restriction and (grid[cell[0] + str(int(cell[1]) + dimension)] == 'A' or \
								   grid[cell[0] + str(int(cell[1]) + dimension)] == 'B' or \
								   grid[cell[0] + str(int(cell[1]) + dimension)] == 'C' or \
								   grid[cell[0] + str(int(cell[1]) + dimension)] == 'X' or \
								   grid[cell[0] + str(int(cell[1]) + dimension)] == 'Y' or \
								   grid[cell[0] + str(int(cell[1]) + dimension)] == 'Z' or \
								   (dimension == 2 and (grid[cell[0] + str(int(cell[1]) + (dimension - 1))] == 'X')) or \
								   (dimension == 2 and (grid[cell[0] + str(int(cell[1]) + (dimension - 1))] == 'Y')) or \
								   (dimension == 2 and (grid[cell[0] + str(int(cell[1]) + (dimension - 1))] == 'Z')) or \
								   (dimension == 2 and (grid[cell[0] + str(int(cell[1]) + (dimension - 1))] == 'C'))):
		restriction.append('S')

	if 'N' not in restriction and (grid[cell[0] + str(int(cell[1]) - dimension)] == 'A' or \
								   grid[cell[0] + str(int(cell[1]) - dimension)] == 'B' or \
								   grid[cell[0] + str(int(cell[1]) - dimension)] == 'C' or \
								   grid[cell[0] + str(int(cell[1]) - dimension)] == 'X' or \
								   grid[cell[0] + str(int(cell[1]) - dimension)] == 'Y' or \
								   grid[cell[0] + str(int(cell[1]) - dimension)] == 'Z' or \
								   (dimension == 2 and (grid[cell[0] + str(int(cell[1]) - (dimension - 1))] == 'X')) or \
								   (dimension == 2 and (grid[cell[0] + str(int(cell[1]) - (dimension - 1))] == 'Y')) or \
								   (dimension == 2 and (grid[cell[0] + str(int(cell[1]) - (dimension - 1))] == 'Z')) or \
								   (dimension == 2 and (grid[cell[0] + str(int(cell[1]) - (dimension - 1))] == 'C'))):
		restriction.append('N')

	return restriction

def isLose(stat):
	if stat[0] == 0 and stat[1] == 0 and stat[2] == 0:
		return True
	else:
		return False

def makeStr(grid):
	colname = ['A','B','C','D','E','F']
	thisgrid = ''

	for column in range(6):
		for row in range(6):
			thisgrid += str(grid[colname[column] + str(row + 1)])
	return thisgrid

def makeStrStat(aiShipStat,playerShipStat):
	thisstat = ''

	for e in aiShipStat:
		thisstat += str(e)
	for e2 in playerShipStat:
		thisstat += str(e2)

	return thisstat

def saveGame(grid,gridAI,aiShipStat,playerShipStat,playerScore):
	if os.path.exists("save.dat"):
		saveCount = 0
		overwrite = []

		chkSaved = open("save.dat", "r")
		for lines in chkSaved:
			saveCount += 1
		chkSaved.close()

		if saveCount < 3:
			animateIn(11)
			osclr()
			print('\n' * 4)
			bar('top')
			cont('{:<20}'.format("         _~_"))
			cont('{:<20}'.format("      __(__(__"))
			cont('{:<20}'.format("     (_((_((_("))
			cont('{:<20}'.format("   \=-:--:--:--."))
			cont('{:<20}'.format("____\_o__o__o_/____"))
			cont('{:<20}'.format("     SAVE GAME"))
			spc(1)
			cont("Please enter your name to save file.")
			spc(1)
			bar('bottom')
			print('\n' * 5)
			name = input("  Enter your name: ")

			saveGame = open("save.dat", "a")
			saveGame.write(name + '%' + makeStr(grid) + '%' + makeStr(gridAI) + '%' + makeStrStat(aiShipStat,playerShipStat) + '%' + str(playerScore) + '\n')
			saveGame.close

			win("Successfully saved game progress!")
			return True
		else:
			win("Save files are on its maximum! Overwrite another to save.")
			readFiles = open("save.dat", "r")
			for lines in readFiles:
				overwrite.append(lines[:-1].split('%'))
			readFiles.close()

			while True:
				animateIn(12)
				osclr()
				print('\n' * 4)
				bar('top')
				cont('{:<20}'.format("         _~_"))
				cont('{:<20}'.format("      __(__(__"))
				cont('{:<20}'.format("     (_((_((_("))
				cont('{:<20}'.format("   \=-:--:--:--."))
				cont('{:<20}'.format("____\_o__o__o_/____"))
				cont('{:<20}'.format("     SAVE GAME"))
				spc(1)
				cont('{:<40}'.format("[1] " + overwrite[0][0].capitalize()))
				cont('{:<40}'.format("[2] " + overwrite[1][0].capitalize()))
				cont('{:<40}'.format("[3] " + overwrite[2][0].capitalize()))
				bar('bottom')
				print('\n' * 4)
				replace = input("  Enter choice to overwrite: ")

				if replace == '1' or replace == '2' or replace == '3':
					animateIn(11)
					osclr()
					print('\n' * 5)
					bar('top')
					cont('{:<20}'.format("         _~_"))
					cont('{:<20}'.format("      __(__(__"))
					cont('{:<20}'.format("     (_((_((_("))
					cont('{:<20}'.format("   \=-:--:--:--."))
					cont('{:<20}'.format("____\_o__o__o_/____"))
					cont('{:<20}'.format("     SAVE GAME"))
					spc(1)
					cont("Please enter your name to save file.")
					spc(1)
					bar('bottom')
					print('\n' * 4)
					name = input("  Enter your name: ")

					overwrite[int(replace) - 1] = [name,makeStr(grid),makeStr(gridAI),makeStrStat(aiShipStat,playerShipStat),str(playerScore)]

					overWriteFile = open("save.dat", 'w')
					for saves in overwrite:
						print(saves)
						overWriteFile.write(saves[0] + '%' + saves[1] + '%' + saves[2] + '%' + saves[3] + '%' + saves[4] + '\n')
					overWriteFile.close()
					win("Successfully saved game progress!")
					return True
				else:
					alert("Entered number is not an option.")
	else:
		animateIn(12)
		osclr()
		print('\n' * 5)
		bar('top')
		cont('{:<20}'.format("         _~_"))
		cont('{:<20}'.format("      __(__(__"))
		cont('{:<20}'.format("     (_((_((_("))
		cont('{:<20}'.format("   \=-:--:--:--."))
		cont('{:<20}'.format("____\_o__o__o_/____"))
		cont('{:<20}'.format("     SAVE GAME"))
		spc(1)
		cont("Please enter your name to save file.")
		spc(1)
		bar('bottom')
		print('\n' * 5)
		name = input("  Enter your name: ")

		makeFile = open("save.dat", "w")
		makeFile.write(name + '%' + makeStr(grid) + '%' + makeStr(gridAI) + '%' + makeStrStat(aiShipStat,playerShipStat) + '%' + str(playerScore) + '\n')
		makeFile.close()
		win("Successfully saved game progress!")
		return True

def smartAI(cell):
	colname = ['A','B','C','D','E','F']
	possible = []

	# Adding
	if (cell[0] != 'A' and cell[0] != 'F') and (cell[1] != '1' and cell[1] != '6'):
		possible.append(colname[colname.index(cell[0]) + 1] + cell[1])
		possible.append(colname[colname.index(cell[0]) - 1] + cell[1])
		possible.append(cell[0] + str(int(cell[1]) + 1))
		possible.append(cell[0] + str(int(cell[1]) - 1))
	else:
		if cell == 'A1':
			possible.append('B1')
			possible.append('A2')
		elif cell == 'A6':
			possible.append('B6')
			possible.append('A5')
		elif cell == 'F1':
			possible.append('E1')
			possible.append('F2')
		elif cell == 'F6':
			possible.append('F5')
			possible.append('E6')
		elif cell[0] == 'A':
			possible.append(cell[0] + str(int(cell[1]) - 1))
			possible.append(cell[0] + str(int(cell[1]) + 1))
			possible.append('B' + cell[1])
		elif cell[0] == 'F':
			possible.append(cell[0] + str(int(cell[1]) - 1))
			possible.append(cell[0] + str(int(cell[1]) + 1))
			possible.append('E' + cell[1])
		elif cell[1] == '1':
			possible.append(colname[colname.index(cell[0]) - 1] + cell[1])
			possible.append(colname[colname.index(cell[0]) + 1] + cell[1])
			possible.append(cell[0] + '2')
		elif cell[1] == '6':
			possible.append(colname[colname.index(cell[0]) - 1] + cell[1])
			possible.append(colname[colname.index(cell[0]) - 1] + cell[1])
			possible.append(cell[0] + '5')

	return possible
