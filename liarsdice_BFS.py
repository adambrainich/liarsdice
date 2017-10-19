# Adam K Brainich
# Josh Manulat
# Daniel Salazar
# CPSC 481
# 15 October 2017

# WORK IN PROGRESS BUILD

import random
import time

aiInfo = [[0,0,0,0,0],5] # dice values, number of dice
playerInfo = [[0,0,0,0,0],5]
NUMBERWORDS = 'zero one two three four five six seven eight nine ten'.split()
NUMBERPLURALS = 'z ones twos threes fours fives sixes'.split()

def pause(sec):
    time.sleep(sec)

def rollDice(agentInfo):
	agentInfo[0] = [0,0,0,0,0]
	for x in range(agentInfo[1]):
		agentInfo[0][x] = random.randint(1,6)
	agentInfo[0].sort()
	return agentInfo

def playerChoice():
    print('Would you like to [b]et, [c]hallenge, or declare the last bet [s]pot on?')
    invalid = True
    while invalid:
        d = input()
        if d == 'b':
            return 0
        if d == 'c':
            return 1
        if d == 's':
            return 2
        print('Invalid input. Please enter the letter b, c, or s.')

def validBet (oldBet, newBet, totalDice):
    if oldBet[0] > newBet[0] or (oldBet[0] == newBet[0] and oldBet[1] >= newBet[1]) or newBet[0] > totalDice or newBet[1] > 6:
        return False
    else:
        return True

def playerBet(oldBet, totalDice):
	newBet = [0,0]
	wrong = True
	while wrong:
		print('What would you like to bet? [Number of dice] [Value of dice]')
		newBet = input()
		newBet = newBet.split()
		if len(newBet) > 1 and newBet[0].isdigit() and newBet[1].isdigit():
			newBet = [int(newBet[0]),int(newBet[1])]
			if validBet(oldBet,newBet,totalDice):
				wrong = False
	print('You bet that there are ' + NUMBERWORDS[newBet[0]] + ' ' + NUMBERPLURALS[newBet[1]] + ' on the table.')
	pause(2)
	return newBet

print('Welcome to Liar\'s Dice!')
print('       .-------.    ______')
print('      /   o   /|   /\     \\')
print('     /_______/o|  /o \  o  \\')
print('     | o     | | /   o\_____\\')
print('     |   o   |o/ \o   /o    /')
print('     |     o |/   \ o/  o  /')
print('     \'-------\'     \/____o/')
playerTurn = True
gameContinues = True

while gameContinues:
	aiInfo = rollDice(aiInfo)
	playerInfo = rollDice(playerInfo)
	roundContinues = True
	totalDice = aiInfo[1] + playerInfo[1]
	currentBet = [0,0]

	print('Your hand: ')
	print(playerInfo[0])

	while roundContinues:
		if playerTurn:
			choice = playerChoice()

			if choice == 0:			# bet
				currentBet = playerBet(currentBet, totalDice)
				playerTurn = False
			elif choice == 1:		# challenge
				if currentBet == [0,0]:
					print('There is no bet to challenge.')
				else:
					pass
			elif choice == 2:		# spot on
				if currentBet == [0,0]:
					print('There is no bet to call spot on.')
				else:
					pass

		elif playerTurn == False:
			pass

		roundContinues = False

	gameContinues = False

# testing
print(aiInfo[0])
print(playerInfo[0])