import time, os, platform, db, random

def refresh():
	global grid, gridAI, aiShipStat, playerShipStat, playerScore, possible
	grid = {}
	gridAI = {}
	db.includeZero(colname,grid,gridAI)
	playerScore = 40
	isHitAdj = False
	possible = []

	#Ship Status
	aiShipStat = [1,2,3]
	playerShipStat = [1,2,3]

# Global Data
colname = ['A','B','C','D','E','F']
dire = ['N', 'E', 'S', 'W']
isHitAdj = False

refresh()
aiList = list(gridAI)

# Program Start
def playerMove():
	global grid,gridAI,playerScore, playerShipStat, aiShipStat, isHitAdj

	while True:
		db.printGrid(colname,grid, gridAI)
		while True:
			playerHit = input("  Enter cell to attack: ").upper()

			if playerHit == '':
				pauseChoice = db.pauseMenu(True)
				if pauseChoice == '1':
					db.animateOut(13)
					db.animateIn('full')
					db.printGrid(colname,grid,gridAI)
					continue
				elif pauseChoice == '2':
					if db.saveGame(grid,gridAI,aiShipStat,playerShipStat,playerScore):
						refresh()
						return True
				elif pauseChoice == '3':
					howTo()
				elif pauseChoice == '4':
					db.win("Game was aborted by the user!")
					refresh()					
					return True
			elif playerHit not in gridAI:
				db.win("Entered cell is outside the battle sea!")
				db.printGrid(colname,grid,gridAI)
			elif gridAI[playerHit] == 'O' or gridAI[playerHit] == '1':
				db.win("You already attacked that cell!")
				db.printGrid(colname,grid,gridAI)
			elif gridAI[playerHit] == 'X':
				db.win("An opponent ship has sunked!")
				aiShipStat[0] -= 1
				playerScore += 10
				gridAI[playerHit] = 'O'
				break
			elif gridAI[playerHit] == 'Y' and aiShipStat[1] != 1:
				db.win("An opponent ship was attacked!")
				aiShipStat[1] -= 1
				playerScore += 5
				gridAI[playerHit] = 'O'
				break
			elif gridAI[playerHit] == 'Z' and aiShipStat[2] != 1:
				db.win("An opponent ship was attacked!")
				aiShipStat[2] -= 1
				playerScore += 3
				gridAI[playerHit] = 'O'
				break
			elif gridAI[playerHit] == 'Y' and aiShipStat[1] == 1:
				db.win("An opponent ship has sunked!")
				playerScore += 5
				gridAI[playerHit] = 'O'
				aiShipStat[1] -= 1
				break
			elif gridAI[playerHit] == 'Z' and aiShipStat[2] == 1:
				aiShipStat[2] -= 1
				db.win("An opponent ship has sunked!")
				playerScore += 5
				gridAI[playerHit] = 'O'
				break
			else:
				db.win("You missed an attack!")
				gridAI[playerHit] = '1'
				break
		# Check Win
		if db.isLose(aiShipStat):
			#db.win("Congratulations. You defeated your opponent!")
			
			# Enter high score here.
			if os.path.exists("high-score.dat"):
				scores = 0
				listScore = []

				chkScoreLen = open("high-score.dat", 'r')
				for hs in chkScoreLen:
					scores += 1
				chkScoreLen.close()

				if scores < 3:
					db.osclr()
					print('\n' * 4)
					db.bar('top')
					db.cont('{:<20}'.format("         _~_"))
					db.cont('{:<20}'.format("      __(__(__"))
					db.cont('{:<20}'.format("     (_((_((_("))
					db.cont('{:<20}'.format("   \=-:--:--:--."))
					db.cont('{:<20}'.format("____\_o__o__o_/____"))
					db.cont('{:<20}'.format("  BATTLESHIP GAME"))
					db.spc(1)
					db.cont("Congratulations, mate! Your score is " + str(playerScore) + '!')
					db.cont("You won the battleship game!")
					db.spc(1)
					db.bar('bottom')
					print('\n' * 4)
					name = input("  Enter your name: ")

					saveHigh = open('high-score.dat', 'a')
					saveHigh.write(str(playerScore) + ',' + name + '\n')
					saveHigh.close()

					refresh()
					return True
				else:
					readScores = open("high-score.dat", 'r')
					for topScores in readScores:
						listScore.append(topScores[:-1].split(','))
					readScores.close()

					if playerScore > int(listScore[0][0]) or playerScore > int(listScore[1][0]) or playerScore > int(listScore[2][0]):
						db.osclr()
						print('\n' * 4)
						db.bar('top')
						db.cont('{:<20}'.format("         _~_"))
						db.cont('{:<20}'.format("      __(__(__"))
						db.cont('{:<20}'.format("     (_((_((_("))
						db.cont('{:<20}'.format("   \=-:--:--:--."))
						db.cont('{:<20}'.format("____\_o__o__o_/____"))
						db.cont('{:<20}'.format("  BATTLESHIP GAME"))
						db.spc(1)
						db.cont("Congratulations, mate! Your score is " + str(playerScore) + '!')
						db.cont("You won the battleship game and achieved a high score!")
						db.spc(1)
						db.bar('bottom')
						print('\n' * 4)
						name = input("  Enter your name: ")

						for i in range(len(listScore)):
							listScore[i][0] = int(listScore[i][0])
						listScore.sort()

						if playerScore > listScore[-1][0]:
							listScore[0] = listScore[1]
							listScore[1] = listScore[2]
							listScore[2] = [playerScore,name]
						elif playerScore > listScore[-2][0]:
							listScore[0] = listScore[1]
							listScore[1] = [playerScore,name]
						else:
							listScore[2] = [playerScore,name]

						# Save to file
						saveHighScores = open("high-score.dat", "w")
						for players in listScore:
							saveHighScores.write(str(players[0]) + ',' + players[1] + '\n')
						saveHighScores.close()

						refresh()
						return True
					else:
						db.osclr()
						print('\n' * 4)
						db.bar('top')
						db.cont('{:<20}'.format("         _~_"))
						db.cont('{:<20}'.format("      __(__(__"))
						db.cont('{:<20}'.format("     (_((_((_("))
						db.cont('{:<20}'.format("   \=-:--:--:--."))
						db.cont('{:<20}'.format("____\_o__o__o_/____"))
						db.cont('{:<20}'.format("  BATTLESHIP GAME"))
						db.spc(1)
						db.cont("Congratulations, mate! Your score is " + str(playerScore) + '!')
						db.spc(2)
						db.bar('bottom')
						print('\n' * 3)
						x = input("  Press enter to continue... ")
						del x

						refresh()
						return True
			else:
				db.osclr()
				print('\n' * 4)
				db.bar('top')
				db.cont('{:<20}'.format("         _~_"))
				db.cont('{:<20}'.format("      __(__(__"))
				db.cont('{:<20}'.format("     (_((_((_("))
				db.cont('{:<20}'.format("   \=-:--:--:--."))
				db.cont('{:<20}'.format("____\_o__o__o_/____"))
				db.cont('{:<20}'.format("  BATTLESHIP GAME"))
				db.spc(1)
				db.cont("Congratulations, mate! Your score is " + str(playerScore) + '!')
				db.cont("You won the battleship game!")
				db.spc(1)
				db.bar('bottom')
				print('\n' * 4)
				name = input("  Enter your name: ")

				makeHigh = open('high-score.dat', 'w')
				makeHigh.write(str(playerScore) + ',' + name + '\n')
				makeHigh.close()

				refresh()
				return True

		db.printGrid(colname,grid,gridAI)
		time.sleep(1)
		# AI Move

		while True:
			db.wait("Computer is thinking.")

			#print(isHitAdj)
			if isHitAdj:
				if len(possible) == 0:
					isHitAdj = False
				else:
					move = random.choice(possible)

					if grid[move] == '0':
						grid[move] = '1'

						toPop = possible.index(move)
						possible.pop(toPop)
						break
					elif grid[move] == '1' or grid[move] == 'O':
						toPop = possible.index(move)
						possible.pop(toPop)
						continue
					elif grid[move] == 'B' and playerShipStat[1] == 1:
						grid[move] = 'O'
						playerScore -= 5
						db.win("Opponent has sunked one of your ships!")
						playerShipStat[1] -= 1

						possible = []
						isHitAdj = False
						break
					elif grid[move] == 'C' and playerShipStat[2] != 1:
						grid[move] = 'O'
						playerShipStat[2] -= 1
						playerScore -= 3
						db.win("One of your ships was attacked by your opponent!")

						# Set SmartAI
						possible = db.smartAI(move)
						isHitAdj = True
						break
					elif grid[move] == 'C' and playerShipStat[2] == 1:
						grid[move] = 'O'
						playerScore -= 5
						db.win("Opponent has sunked one of your ships!")
						playerShipStat[2] -= 1

						possible = []
						isHitAdj = False
						break

			else:
				possible = []
				move = random.choice(list(grid))

				if grid[move] == 'A':
					grid[move] = 'O'
					playerShipStat[0] -= 1
					db.win("Opponent has sunked one of your ships!")
					playerScore -= 10
					break
				elif grid[move] == 'B' and playerShipStat[1] != 1:
					grid[move] = 'O'
					playerShipStat[1] -= 1
					playerScore -= 5
					db.win("One of your ships was attacked by your opponent!")

					# Set SmartAI
					possible = db.smartAI(move)
					isHitAdj = True
					break
				elif grid[move] == 'C' and playerShipStat[2] != 1:
					grid[move] = 'O'
					playerShipStat[2] -= 1
					playerScore -= 3
					db.win("One of your ships was attacked by your opponent!")

					# Set SmartAI
					possible = db.smartAI(move)
					isHitAdj = True
					break
				elif grid[move] == 'B' and playerShipStat[1] == 1:
					grid[move] = 'O'
					playerScore -= 5
					db.win("Opponent has sunked one of your ships!")
					playerShipStat[1] -= 1
					break
				elif grid[move] == 'C' and playerShipStat[2] == 1:
					grid[move] = 'O'
					playerScore -= 5
					db.win("Opponent has sunked one of your ships!")
					playerShipStat[2] -= 1
					break
				elif grid[move] == 'O' or grid[move] == '1':
					continue
				else:
					grid[move] = '1'
					break

		# If win/lose
		if db.isLose(playerShipStat):
			db.bar('top')
			db.cont('{:<20}'.format("         _~_"))
			db.cont('{:<20}'.format("      __(__(__"))
			db.cont('{:<20}'.format("     (_((_((_("))
			db.cont('{:<20}'.format("   \=-:--:--:--."))
			db.cont('{:<20}'.format("____\_o__o__o_/____"))
			db.cont('{:<20}'.format("  BATTLESHIP GAME"))
			db.spc(1)
			db.cont("Booo! The opponent has sunked all your battleships!")
			db.spc(2)
			db.bar('bottom')
			print('\n' * 3)
			x = input("  Press enter to continue... ")
			del x
			refresh()
			return True
		#break

db.splash()
db.animateOut('full')

while True:
	db.animateIn('full')
	db.mainMenu()
	menuChoice = input("  Enter your choice: ")

	def menuOptions(menuChoice):
		global grid,gridAI, playerShipStat, aiShipStat, playerScore

		if menuChoice == '1':
			db.animateOut('full')
			db.animateIn('full')
			while True: # 1x1 Battleship
				db.printGrid(colname,grid,gridAI)
				pos = input("  Place your 1x1 battleship: ").upper()

				if pos == '':
					pauseChoice = db.pauseMenu(False)
					if pauseChoice == '1':
						db.animateOut(13)
						db.animateIn('full')
						db.printGrid(colname,grid,gridAI)
						continue
					elif pauseChoice == '2':
						if db.saveGame(grid,gridAI,aiShipStat,playerShipStat,playerScore):
							refresh()
							return
					elif pauseChoice == '3':
						howTo()
					elif pauseChoice == '4':
						db.win("Game was aborted by the user!")
						refresh()
						
						return
				elif pos not in grid:
					db.alert("Entered cell is outside the battle sea!")
					db.printGrid(colname,grid,gridAI)
				else:
					grid[pos] = 'A'
					db.printGrid(colname,grid,gridAI)
					break

			while True: # 2x1 Battlship
				pos = input("  Place your 2x1 battleship: ").upper()

				if pos == '':
					pauseChoice = db.pauseMenu(False)
					if pauseChoice == '1':
						db.animateOut(13)
						db.animateIn('full')
						db.printGrid(colname,grid,gridAI)
						continue
					elif pauseChoice == '2':
						if db.saveGame(grid,gridAI,aiShipStat,playerShipStat,playerScore):
							refresh()
							return
					elif pauseChoice == '3':
						howTo()
					elif pauseChoice == '4':
						db.win("Game was aborted by the user!")
						refresh()
						
						
						return
				elif pos not in grid:
					db.alert("Entered cell is outside the battle sea!")
					db.printGrid(colname,grid,gridAI)
				elif grid[pos] == 'A':
					db.alert("A battleship is already in that cell!")
					db.printGrid(colname,grid,gridAI)
				else:
					grid[pos] = 'B'
					db.printGrid(colname,grid,gridAI)
					break
			while True:
				posDir = input("  Enter 2x1 battleship direction (N/E/S/W): ").upper()

				if posDir == '':
					pauseChoice = db.pauseMenu(False)
					if pauseChoice == '1':
						db.animateOut(13)
						db.animateIn('full')
						db.printGrid(colname,grid,gridAI)
						continue
					elif pauseChoice == '2':
						if db.saveGame(grid,gridAI,aiShipStat,playerShipStat,playerScore):
							refresh()
							return
					elif pauseChoice == '3':
						howTo()
					elif pauseChoice == '4':
						db.win("Game was aborted by the user!")
						refresh()
						
						
						return
				elif posDir not in dire:
					db.alert("Battleship direction is not valid!")
					db.printGrid(colname,grid,gridAI)
				elif posDir in db.chkShipExist(pos,colname,grid, 1):
					db.alert("Cannot position battleship there!")
					db.printGrid(colname,grid,gridAI)
				elif posDir == 'N' and pos[1] != '1':
					grid[pos[0] + str(int(pos[1]) - 1)] = 'B'
					db.printGrid(colname,grid,gridAI)
					break
				elif posDir == 'E' and pos[0] != 'F':
					grid[colname[colname.index(pos[0]) + 1] + pos[1]] = 'B'
					db.printGrid(colname,grid,gridAI)
					break
				elif posDir == 'S' and pos[0] != '6':
					grid[pos[0] + str(int(pos[1]) + 1)] = 'B'
					db.printGrid(colname,grid,gridAI)
					break
				elif posDir == 'W' and pos[0] != 'X':
					grid[colname[colname.index(pos[0]) - 1] + pos[1]] = 'B'
					db.printGrid(colname,grid,gridAI)
					break
				else:
					db.alert("Cannot position battleship outside the battle sea!")
					db.printGrid(colname,grid,gridAI)

			while True: # Pos 3x1 ship
				pos = input("  Place your 3x1 battleship: ").upper()

				if pos == '':
					pauseChoice = db.pauseMenu(False)
					if pauseChoice == '1':
						db.animateOut(13)
						db.animateIn('full')
						db.printGrid(colname,grid,gridAI)
						continue
					elif pauseChoice == '2':
						if db.saveGame(grid,gridAI,aiShipStat,playerShipStat,playerScore):
							refresh()
							return
					elif pauseChoice == '3':
						howTo()
					elif pauseChoice == '4':
						db.win("Game was aborted by the user!")
						refresh()
						
						
						return
				elif pos not in grid:
					db.alert("Entered cell is outside the battle sea!")
					db.printGrid(colname,grid,gridAI)
				elif grid[pos] == 'A' or grid[pos] == 'B':
					db.alert("A battleship is already in that cell!")
					db.printGrid(colname,grid,gridAI)
				else:
					grid[pos] = 'C'
					db.printGrid(colname,grid,gridAI)
					break
			while True:
				posDir = input("  Enter 3x1 battleship direction (N/E/S/W): ").upper()

				if posDir == '':
					pauseChoice = db.pauseMenu(False)
					if pauseChoice == '1':
						db.animateOut(13)
						db.animateIn('full')
						db.printGrid(colname,grid,gridAI)
						continue
					elif pauseChoice == '2':
						if db.saveGame(grid,gridAI,aiShipStat,playerShipStat,playerScore):
							refresh()
							return
					elif pauseChoice == '3':
						howTo()
					elif pauseChoice == '4':
						db.win("Game was aborted by the user!")
						refresh()
						
						
						return
				elif posDir not in dire:
					db.alert("Battleship direction is not valid!")
					db.printGrid(colname,grid,gridAI)
				elif posDir in db.chkShipExist(pos,colname,grid, 2):
					db.alert("Cannot position battleship there!")
					db.printGrid(colname,grid,gridAI)
				elif posDir == 'N' and pos[1] != '2':
					grid[pos[0] + str(int(pos[1]) - 1)] = 'C'
					grid[pos[0] + str(int(pos[1]) - 2)] = 'C'
					db.printGrid(colname,grid,gridAI)
					break
				elif posDir == 'E' and pos[0] != 'E':
					grid[colname[colname.index(pos[0]) + 1] + pos[1]] = 'C'
					grid[colname[colname.index(pos[0]) + 2] + pos[1]] = 'C'
					db.printGrid(colname,grid,gridAI)
					break
				elif posDir == 'S' and pos[0] != '5':
					grid[pos[0] + str(int(pos[1]) + 1)] = 'C'
					grid[pos[0] + str(int(pos[1]) + 2)] = 'C'
					db.printGrid(colname,grid,gridAI)
					break
				elif posDir == 'W' and pos[0] != 'A':
					grid[colname[colname.index(pos[0]) - 1] + pos[1]] = 'C'
					grid[colname[colname.index(pos[0]) - 2] + pos[1]] = 'C'
					db.printGrid(colname,grid,gridAI)
					break
				else:
					db.alert("Cannot position battleship outside the battle sea!")
					db.printGrid(colname,grid,gridAI)
			
			db.wait("Opponent is positioning his battleships.")
			random.shuffle(aiList)
			AIfirst = True
			AIsecond = True

			for cell in aiList:
				if (gridAI[cell] != 'A' or gridAI[cell] != 'B' or gridAI[cell] != 'C' or gridAI[cell] != 'X'):
					random.shuffle(dire)

					if AIfirst: # 1x1 AI
						gridAI[cell] = 'X'
						AIfirst = False
					elif AIsecond: # 1x2 AI
						for randomDir in dire:
							if randomDir not in db.chkShipExist(cell,colname,gridAI,1):
								if randomDir == 'N' and cell[1] != '1':
									gridAI[cell] = 'Y'
									gridAI[cell[0] + str(int(cell[1]) - 1)] = 'Y'
									AIsecond = False
									break
								elif randomDir == 'E' and cell[0] != 'F':
									gridAI[cell] = 'Y'
									gridAI[colname[colname.index(cell[0]) + 1] + cell[1]] = 'Y'
									AIsecond = False
									break
								elif randomDir == 'S' and cell[1] != '6':
									gridAI[cell] = 'Y'
									gridAI[cell[0] + str(int(cell[1]) + 1)] = 'Y'
									AIsecond = False
									break
								elif randomDir == 'W' and cell[0] != 'X':
									gridAI[cell] = 'Y'
									gridAI[colname[colname.index(cell[0]) - 1] + cell[1]] = 'Y'
									AIsecond = False
									break

					else: # 1x3 AI
						for randomDir in dire:
							if randomDir not in db.chkShipExist(cell,colname,gridAI,2):
								if randomDir == 'N' and (cell[1] != '1' or cell[1] != '2'):
									gridAI[cell] = 'Z'
									gridAI[cell[0] + str(int(cell[1]) - 1)] = 'Z'
									gridAI[cell[0] + str(int(cell[1]) - 2)] = 'Z'
									break
								elif randomDir == 'E' and (cell[0] != 'L' or cell[0] != 'E'):
									gridAI[cell] = 'Z'
									gridAI[colname[colname.index(cell[0]) + 1] + cell[1]] = 'Z'
									gridAI[colname[colname.index(cell[0]) + 2] + cell[1]] = 'Z'
									break
								elif randomDir == 'S' and (cell[0] != '6' or cell[0] != '5'):
									gridAI[cell] = 'Z'
									gridAI[cell[0] + str(int(cell[1]) + 1)] = 'Z'
									gridAI[cell[0] + str(int(cell[1]) + 2)] = 'Z'
									break
								elif randomDir == 'W' and (cell[1] != 'X' or cell[1] != 'A'):
									gridAI[cell] = 'Z'
									gridAI[colname[colname.index(cell[0]) - 1] + cell[1]] = 'Z'
									gridAI[colname[colname.index(cell[0]) - 2] + cell[1]] = 'Z'
									break
						break

			while True: # Alternate, infinite turn
				db.printGrid(colname,grid,gridAI)

				# Player Move

				if playerMove():
					return
		elif menuChoice == '2':
			loadSaved = []
			#temp = []

			if os.path.exists('save.dat'):
				saveCount = 0

				chkSaveNum = open('save.dat', 'r')
				for saves in chkSaveNum:
					saveCount += 1

				chkSaveNum.close()

				if saveCount != 0:
					readSaves = open('save.dat', 'r')
					for saves in readSaves:
						loadSaved.append(saves[:-1].split('%'))
					readSaves.close()

					while True:
						db.animateIn(12)
						db.osclr()
						print('\n' * 4)
						db.bar('top')
						db.cont('{:<20}'.format("         _~_"))
						db.cont('{:<20}'.format("      __(__(__"))
						db.cont('{:<20}'.format("     (_((_((_("))
						db.cont('{:<20}'.format("   \=-:--:--:--."))
						db.cont('{:<20}'.format("____\_o__o__o_/____"))
						db.cont('{:<20}'.format("     LOAD GAME"))
						db.spc(1)

						if len(loadSaved) == 3:
							db.cont('{:<40}'.format("[1] " + loadSaved[0][0].capitalize()))
							db.cont('{:<40}'.format("[2] " + loadSaved[1][0].capitalize()))
							db.cont('{:<40}'.format("[3] " + loadSaved[2][0].capitalize()))
						elif len(loadSaved) == 2:
							db.cont('{:<40}'.format("[1] " + loadSaved[0][0].capitalize()))
							db.cont('{:<40}'.format("[2] " + loadSaved[1][0].capitalize()))
							db.spc(1)
						elif len(loadSaved) == 1:
							db.cont('{:<40}'.format("[1] " + loadSaved[0][0].capitalize()))
							db.spc(2)

						db.bar('bottom')
						print('\n' * 4)
						load = input("  Enter game file to load: ")

						if load == '1' or load == '2' or load == '3':
							for column in range(6):
								for row in range(6):
									grid[colname[column] + str(row + 1)] = loadSaved[int(load) - 1][1][(6 * column) + row]
							
							for column in range(6):
								for row in range(6):
									gridAI[colname[column] + str(row + 1)] = loadSaved[int(load) - 1][2][(6 * column) + row]

							playerShipStat = [int(loadSaved[int(load) - 1][3][3]),int(loadSaved[int(load) - 1][3][4]),int(loadSaved[int(load) - 1][3][5])]
							aiShipStat = [int(loadSaved[int(load) - 1][3][0]),int(loadSaved[int(load) - 1][3][1]),int(loadSaved[int(load) - 1][3][2])]

							playerScore = int(loadSaved[int(load) - 1][4])

							playerMove()
							return
						else:
							db.alert("Entered number is not an option.")
				else:
					db.alert("No saved games yet.")
					return
			else:
				db.alert("No saved games yet.")
				return

			#break
		elif menuChoice == '3':
			if os.path.exists("high-score.dat"):
				# Read Scores
				highScores = []

				readScore = open("high-score.dat", 'r')
				for hs in readScore:
					highScores.append(hs[:-1].split(','))
				readScore.close()

				if len(highScores) == 3:
					db.animateIn(14)
					db.osclr()
					print('\n' * 3)
					db.bar('top')
					db.cont('{:<20}'.format("         _~_"))
					db.cont('{:<20}'.format("      __(__(__"))
					db.cont('{:<20}'.format("     (_((_((_("))
					db.cont('{:<20}'.format("   \=-:--:--:--."))
					db.cont('{:<20}'.format("____\_o__o__o_/____"))
					db.cont('{:<20}'.format("    HIGH SCORES"))
					db.spc(1)
					db.cont('{:<19}'.format("NAME") + '{:<5}'.format("SCORE"))
					db.cont('{:<19}'.format("1. " + highScores[2][1]) + '{:<5}'.format(highScores[2][0]))
					db.cont('{:<19}'.format("2. " + highScores[1][1]) + '{:<5}'.format(highScores[1][0]))
					db.cont('{:<19}'.format("3. " + highScores[0][1]) + '{:<5}'.format(highScores[0][0]))
					db.spc(1)
					db.bar('bottom')
					print('\n' * 3)
					x = input("  Press enter to continue... ")
					del x
					db.animateOut(14)
					return
				elif len(highScores) == 2:
					db.animateIn(14)
					db.osclr()
					print('\n' * 3)
					db.bar('top')
					db.cont('{:<20}'.format("         _~_"))
					db.cont('{:<20}'.format("      __(__(__"))
					db.cont('{:<20}'.format("     (_((_((_("))
					db.cont('{:<20}'.format("   \=-:--:--:--."))
					db.cont('{:<20}'.format("____\_o__o__o_/____"))
					db.cont('{:<20}'.format("    HIGH SCORES"))
					db.spc(1)
					db.cont('{:<19}'.format("NAME") + '{:<5}'.format("SCORE"))
					db.cont('{:<19}'.format("1. " + highScores[1][1]) + '{:<5}'.format(highScores[1][0]))
					db.cont('{:<19}'.format("2. " + highScores[0][1]) + '{:<5}'.format(highScores[0][0]))
					db.spc(2)
					db.bar('bottom')
					print('\n' * 3)
					x = input("  Press enter to continue... ")
					del x
					db.animateOut(14)
					return
				elif len(highScores) == 1:
					db.animateIn(14)
					db.osclr()
					print('\n' * 3)
					db.bar('top')
					db.cont('{:<20}'.format("         _~_"))
					db.cont('{:<20}'.format("      __(__(__"))
					db.cont('{:<20}'.format("     (_((_((_("))
					db.cont('{:<20}'.format("   \=-:--:--:--."))
					db.cont('{:<20}'.format("____\_o__o__o_/____"))
					db.cont('{:<20}'.format("    HIGH SCORES"))
					db.spc(1)
					db.cont('{:<19}'.format("NAME") + '{:<5}'.format("SCORE"))
					db.cont('{:<19}'.format("2. " + highScores[0][1]) + '{:<5}'.format(highScores[0][0]))
					db.spc(3)
					db.bar('bottom')
					print('\n' * 3)
					x = input("  Press enter to continue... ")
					del x
					db.animateIn(14)
					return
			else:
				db.alert("There are no high scores yet!")
		elif menuChoice == '4':
			db.animateOut('full')
			db.animateIn(17)
			db.osclr()

			print('\n' * 1)
			db.bar('top')
			db.spc(1)
			db.cont('{:<20}'.format("         _~_"))
			db.cont('{:<20}'.format("      __(__(__"))
			db.cont('{:<20}'.format("     (_((_((_("))
			db.cont('{:<20}'.format("   \=-:--:--:--."))
			db.cont('{:<20}'.format("____\_o__o__o_/____"))
			db.cont('{:<20}'.format("     BATTLESHIP   "))
			db.spc(1)
			db.cont('Battleship (or Battleships) is a game for two players where')
			db.cont('you try to guess the location of five ships your opponent has')
			db.cont('hidden on a grid. Players take turns calling out a row and')
			db.cont('column, attempting to name a square containing enemy ships.')
			db.cont('Source: http://boardgames.about.com')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 1)
			x = input("  Press enter to continue... ")
			db.osclr()

			print('\n' * 1)
			db.bar('top')
			db.spc(1)
			db.cont('{:<20}'.format("         _~_"))
			db.cont('{:<20}'.format("      __(__(__"))
			db.cont('{:<20}'.format("     (_((_((_("))
			db.cont('{:<20}'.format("   \=-:--:--:--."))
			db.cont('{:<20}'.format("____\_o__o__o_/____"))
			db.cont('{:<20}'.format("     BATTLESHIP   "))
			db.spc(1)
			db.cont('The player position his battleships anywhere in the battle sea.')
			db.cont("To enter a cell name, enter first the column then row")
			db.cont('(e.g. A1, B5). After this is done, the computer will position')
			db.cont('his own ships in his battle sea.')
			db.spc(3)
			db.bar('bottom')
			print('\n' * 1)
			x = input("  Press enter to continue... ")
			db.osclr()

			print('\n' * 1)
			db.bar('top')
			db.spc(1)
			db.cont('{:<20}'.format("         _~_"))
			db.cont('{:<20}'.format("      __(__(__"))
			db.cont('{:<20}'.format("     (_((_((_("))
			db.cont('{:<20}'.format("   \=-:--:--:--."))
			db.cont('{:<20}'.format("____\_o__o__o_/____"))
			db.cont('{:<20}'.format("     BATTLESHIP   "))
			db.spc(1)
			db.cont("Guess where in your opponent's battle sea his ships were")
			db.cont("position. Enter the cell in order to attack the cell.")
			db.cont('This will be done simultaneously until one is declared')
			db.cont('a winner (when all ships of opponent has been sunked.')
			db.cont('To enter the pause menu, just press enter in the game.')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 1)
			x = input("  Press enter to continue... ")
			db.animateOut(17)
			db.osclr()

		elif menuChoice == '5':
			db.animateOut('full')
			db.animateIn(10)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("mmmm   mmmmmm m    m mmmmmm m       mmmm  mmmmm  mmmmmm mmmm  ")
			db.cont('#   "m #      "m  m" #      #      m"  "m #   "# #      #   "m')
			db.cont('#    # #mmmmm  #  #  #mmmmm #      #    # #mmm#" #mmmmm #    #')
			db.cont('#    # #       "mm"  #      #      #    # #      #      #    #')
			db.cont('#mmm"  #mmmmm   ##   #mmmmm #mmmmm  #mm#  #      #mmmmm #mmm" ')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("  mmm           mmm   mmmm  mmmm   mmmmmm mmmm  ")
			db.cont(' #            m"   " m"  "m #   "m #      #   "m')
			db.cont(' ##           #      #    # #    # #mmmmm #    #')
			db.cont('#  #m#        #      #    # #    # #      #    #')
			db.cont('"#mm#m         "mmm"  #mm#  #mmm"  #mmmmm #mmm" ')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("mmmmm m     m        mmmmm    mm   m      mmmmm  m    m")
			db.cont('#    # "m m"         #   "#   ##   #      #   "# #    #')
			db.cont('#mmmm"  "#"          #mmmm"  #  #  #      #mmm#" #mmmm#')
			db.cont('#    #   #           #   "m  #mm#  #      #      #    #')
			db.cont('#mmmm"   #           #    " #    # #mmmmm #      #    #')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(2)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("")
			db.cont('')
			db.cont('')
			db.cont('')
			db.cont('')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("mmmmm    mm  mmmmmmmmmmmmmm m      mmmmmm  mmmm  m    m mmmmm  mmmmm ")
			db.cont('#    #   ##     #      #    #      #      #"   " #    #   #    #   "#')
			db.cont('#mmmm"  #  #    #      #    #      #mmmmm "#mmm  #mmmm#   #    #mmm#"')
			db.cont('#    #  #mm#    #      #    #      #          "# #    #   #    #     ')
			db.cont('#mmmm" #    #   #      #    #mmmmm #mmmmm "mmm#" #    # mm#mm  #     ')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("  mmm    mm   m    m mmmmmm")
			db.cont('m"   "   ##   ##  ## #     ')
			db.cont('#   mm  #  #  # ## # #mmmmm')
			db.cont('#    #  #mm#  # "" # #     ')
			db.cont(' "mmm" #    # #    # #mmmmm')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("")
			db.cont('')
			db.cont('')
			db.cont('')
			db.cont('')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("  mmm  m    m  mmmm    mmm         mmm    mmm  ")
			db.cont('m"   " ##  ## #"   " m"   "          #      #  ')
			db.cont('#      # ## # "#mmm  #               #      #  ')
			db.cont('#      # "" #     "# #               #      #  ')
			db.cont(' "mmm" #    # "mmm#"  "mmm"        mm#mm  mm#mm')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("mmmmm   mmmm    mmm  m    m  mmmm         m                  m")
			db.cont('#   "# m"  "m m"   " #  m"  #"   "         #     mmmmm      # ')
			db.cont('#mmmm" #    # #      #m#    "#mmm           #    # # #     #  ')
			db.cont('#   "m #    # #      #  #m      "#           #   # # #    #   ')
			db.cont('#    "  #mm#   "mmm" #   "m "mmm#"            #  # # #   #    ')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont("")
			db.cont('')
			db.cont('')
			db.cont('')
			db.cont('')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			print('\n' * 4)
			db.bar('top')
			db.spc(2)
			db.cont('#        m    #             #               "  ')
			db.cont('#   m  mm#mm  # mm   m   m  #mmm    mmm   mmm  ')
			db.cont('# m"     #    #"  #   #m#   #" "#  "   #    #  ')
			db.cont('#"#      #    #   #   m#m   #   #  m"""#    #  ')
			db.cont('#  "m    "mm  #   #  m" "m  ##m#"  "mm"#  mm#mm')
			db.spc(2)
			db.bar('bottom')
			print('\n' * 5)
			time.sleep(1)
			db.osclr()

			db.animateOut(10)
			return

		elif menuChoice == '6':
			db.animateOut('full')
			db.osclr()
			exit()
		#elif menuChoice == '0':
		#	hiddenMini()
		else:
			db.alert("You have entered an invalid menu item!")
	menuOptions(menuChoice)
