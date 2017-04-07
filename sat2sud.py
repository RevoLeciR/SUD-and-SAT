import sys
import math
import os

def solvePuzzle(satExpressions, fil):
	satExpressions[1] = satExpressions[1].split(' ')
	size = len(satExpressions[1])-1

	truths = [None]*(size)
	size = int(size**(1/float(3)))+1
	
	#satExpressions[1] = satExpressions[1].split(' ')
	
	#print satExpressions[1]
	sat_arr = satExpressions[1]
	del sat_arr[-1] #remove last element (the 0) in the list
	#print satExpressions[1]
	secondArray = []
	
	#print len(satExpressions[1])
	#print len(truths)
	
	for x in satExpressions[1]:	
		#truth array keeps track of the negated variables
		if x[0] == '-':
			#print int(x[1:])
			truths[int(x[1:])-1] = False
		else:
			#print int(x)
			#print int(x)
			truths[int(x)-1] = True
	
	'''
	for i in range(len(truths)):
		if int(sat_arr[i]) < 0:
			truths[i] = False
		else:
			truths[i] = True
	'''
	
	
	board = [] #array that will printed out containing solved puzzle
	
	#fill size * size board with zeroes
	for a in range(size):
		board.append([])
		for b in range(size):
			board[a].append(0)
			
	for a in range(len(truths)):
		#algorithm to convert CNF back to an integer
		#uses the formula given in SudokuasSat.pdf
		if truths[a] == True:
			x = int((a)/size**2)
			y = int(((a) - x*size**2)/size)
			z = (a+1)-x*size**2-size*y
			board[y][x] = z
			
	#print the solved puzzle		
	for a in range(size):
		#print (board[a])
		fil.write(str(board[a])+"\n")

def main():
	'''
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
	'''
		
	fldr = raw_input("Enter folder name where SAT encodings: \n")
	par_dir = os.getcwd()
	
	#new_dir = par_dir + "\\" + fldr #windows directory style
	new_dir = par_dir + "/" + fldr #linux directory style
	
	if not os.path.exists(new_dir):
		print "Folder does not exist. Exiting."
		sys.exit()
	
	'''
	sol_fldr = raw_input("\nEnter a folder name where you like to store the Sudoku solutions. \n")
	new_sol_dir = par_dir + "\\" + sol_fldr #windows directory style
	#new_sol_dir = par_dir + "/" + sol_fldr #linux directory style
	'''
	
	os.chdir(new_dir) #change working directory
	
	grid_list = os.listdir(new_dir)
	
	#sol_fldr = raw_input("\nEnter a folder name where you like to store the Sudoku solutions. \n")
	
	pre = "Grid"
	suf = "_SATencoded.txt"
	sol = "Solution"
	for i in range(len(grid_list)):
		try:
			file = open(grid_list[i])
			inputSat = file.read()
			file.close()
		except:
			print "Error finding file " + full_fn
		
		inputSat = inputSat.splitlines()
		#print type(inputSat[0])
		if inputSat[0] == 'SAT':
			write_fn = sol + str(i+1).zfill(2) + ".txt"
			#print write_fn
			fil = open(write_fn, "w")
			solvePuzzle(inputSat, fil)
			fil.close()
		else:
			print grid_list[i] + " is not a miniSAT encoding."
	
if __name__ == "__main__":
	main() 
