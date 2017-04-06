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
			#truth array keeps track of the negated variables
			if x[0] == '-':
				truths[int(x[1:])] = False
			else:
				truths[int(x)] = True
			
	board = [] #array that will printed out containing solved puzzle
	
	for a in range(size):
		board.append([])
		for b in range(size):
			board[a].append(0)
			
	for a in range(1, len(truths)):
		#algorithm to convert CNF back to an integer
		#uses the formula given in SudokuasSat.pdf
		if truths[a] == True:
			x = int((a-1)/size**2)
			y = int((a-1 - x*size**2)/size)
			z = a-x*size**2-size*y
			board[y][x] = z
	
	#print the solved puzzle		
	for a in range(size):
		print (board[a])

def main():
	#sat2sud.py takes in the output of the SAT solver as a command line argument
	if len(sys.argv) == 1:
		print ("No arguments") #no file given so we exit
	else:
		inputSat = ""
		try:
			file = open(sys.argv[1])
			inputSat = file.read()
			file.close()
		except:
			print ("Not a valid file")
			inputGrid = sys.argv[1]
		#once a valid file is given solvePuzzle is called to turn the cnf from the SAT to a sudoku	
		inputSat = inputSat.splitlines()
		solvePuzzle(inputSat)
		
if __name__ == "__main__":
	main() 
