import sys
import math

def solvePuzzle(size, sat):
	satExpressions = sat
	
	truths = [None]*(size**3+1)
	
	
	for x in range(len(satExpressions)):
		satExpressions[x] = satExpressions[x].split(' ')
	
	#while there are still expressions left
	#while len(satExpressions) > 0:
	
	
	while len(satExpressions) > 53:
	
		secondArray = []
	
		for x in satExpressions:
			if len(x) == 1:
				if x[0][0] == '-':
					truths[int(x[0][1:])] = False
				else:
					truths[int(x[0])] = True
			elif len(x) > 1:
				subArray = []
				copy = True
				for y in x:
					if y[0] == '-':
						if(truths[int(y[1:])] != True):
							subArray.append(y)
						if(truths[int(y[1:])] == False):
							copy = False
					else:
						if(truths[int(y)] != False):
							subArray.append(y)
						if(truths[int(y)] == True):
							copy == False
				if(copy == True):
					secondArray.append(subArray)
		satExpressions = secondArray
		print len(satExpressions)
		#print truths
	
	print truths
	print len(truths)
	
	board = []
	
	for a in range(9):
		board.append([])
		for b in range(9):
			board[a].append(0)
			
	for a in range(1, len(truths)):
		if truths[a] == True:
			x = int((a-1)/81)
			y= int((a-1 - x*81)/9)
			z = a-x*81-9*y
			board[x][y] = z
			
	for a in range(9):
		print board[a]

def main():
	if len(sys.argv) == 1:
		print ("No arguments")
	else:
		inputSat = ""
		try:
			file = open(sys.argv[1])
			inputSat = file.read()
			file.close()
		except:
			print ("Not a valid file")
			inputGrid = sys.argv[1]
			
		sat = []
		boardSize = 0
			
		for x in inputSat.splitlines():
			if x.startswith('new puzzle'):
				boardSize = int(x[12])
				if(sat!= []):
					print ('next puzzle')
					solvePuzzle(boardSize,sat)
					sat = []
			else:
				sat.append(x)
		if sat != []:
			print ('next puzzle')
			solvePuzzle(boardSize,sat)
		
if __name__ == "__main__":
	main() 