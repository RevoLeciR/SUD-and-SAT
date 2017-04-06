import sys
import math

def solvePuzzle(satExpressions):

	size = len(satExpressions[1])-1

	truths = [None]*(size)
	size = size**(1/3)
	
	satExpressions[1] = satExpressions[1].split(' ')
	
	secondArray = []
	
	
	
	
	for x in satExpressions[1]:	
		if(x != 0):
			if x[0] == '-':
				truths[int(x[1:])] = False
			else:
				truths[int(x)] = True
			
	board = []
	
	for a in range(size):
		board.append([])
		for b in range(size):
			board[a].append(0)
			
	for a in range(1, len(truths)):
		if truths[a] == True:
			x = int((a-1)/size**2)
			y = int((a-1 - x*size**2)/size)
			z = a-x*size**2-size*y
			board[y][x] = z
			
	for a in range(size):
		print (board[a])

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
			
		inputSat = inputSat.splitlines()
		solvePuzzle(inputSat)
		
if __name__ == "__main__":
	main() 