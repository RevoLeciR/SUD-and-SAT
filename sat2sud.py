import sys
import math


def solvePuzzle(size, sat):
	satExpressions = sat
	
	truths = [None]*(size**3+1)
	
	
	for x in range(len(satExpressions)):
		satExpressions[x] = satExpressions[x].split(' ')
	
	
	
	
	#while there are still expressions left
	#while len(satExpressions) > 0:
	for x in satExpressions:
		if len(x) == 1:
			if x[0] == '-':
				truths[int(x[0][1:])] = False
				#print '%s' %(int(x[1:]))
			else:
				truths[int(x[0])] = True
				#print '%s' %(x)
		satExpressions.remove(x)
	print truths
	
	#print satExpressions
			#else:
				#for y in x:
					
				#loop through the array and remove false expressions
				
				#the expression must evaluate to true
				
			
	

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
					print (solvePuzzle(boardSize,sat))
					sat = []
			else:
				sat.append(x)
		if sat != []:
			print ('next puzzle')
			print (solvePuzzle(boardSize,sat))
		
if __name__ == "__main__":
	main() 