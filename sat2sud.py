import sys
import math


def solvePuzzle(size, satExtressions):
	truths = [None]*size**3
	solved = False
	for x in satExtressions:
		x = x.split(' ')
		print x
	#print satExtressions
	
	
	#while solved == False:
		#for x in satExtressions.splitlines():
			
	

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
					print 'next puzzle'
					print solvePuzzle(boardSize,sat)
					sat = []
			else:
				sat.append(x)
		if sat != []:
			print 'next puzzle'
			print solvePuzzle(boardSize,sat)
		
if __name__ == "__main__":
	main() 