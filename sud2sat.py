import sys
import math
import time

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def returnValueAt(row, column, grid):
	return int(grid[column-1][row-1])

def convertToDecimal(x,y,z, size):
	return size**2 * (x-1) + size * (y-1)+z
	
def eachElementHasAtLeastOneNumber(columnNumber, outputGrid):
	for x in range(1,columnNumber+1): #i
		for y in range(1,columnNumber+1): #j
			list = ""
			occurence = False
			first = True
			for z in range(1,columnNumber+1): #k
				if(returnValueAt(x,y,outputGrid) != z and occurence == False):
					#actually dont bother printing this out in that case
					if first == False:
						list += ' '
					first = False
					list += "%s" %(convertToDecimal(x,y,z, columnNumber))
				elif occurence == False:
					list = "%s" %(convertToDecimal(x,y,z, columnNumber))
					occurence = True
			#print ("%s" %list)
			print ("%s %s" %(list,0))
		
def eachRowHasAtMostOneOfEachNumber(columnNumber, outputGrid):
	for y in range(1,columnNumber+1): #i
		for z in range(1,columnNumber+1): #k
			for x in range(1,columnNumber): #j
				for i in range(x+1,columnNumber+1): #l
					#print ("-%s -%s" %(convertToDecimal(x,y,z, columnNumber),convertToDecimal(i,y,z, columnNumber)))
					print ("-%s -%s 0" %(convertToDecimal(x,y,z, columnNumber),convertToDecimal(i,y,z, columnNumber)))

def eachColumnHasAtMostOneOfEachNumber(columnNumber, outputGrid):
	for x in range(1,columnNumber+1): #j
		for z in range(1,columnNumber+1): #k
			for y in range(1,columnNumber): #i
				for i in range(y+1,columnNumber+1): #l
					print ("-%s -%s 0" %(convertToDecimal(x,y,z, columnNumber), convertToDecimal(x,i,z, columnNumber)))
			
def eachNumberAppearsAtMostOncePerGrid(columnNumber, outputGrid):
	for z in range(1,columnNumber+1): #k
		for i in range(0,int(math.sqrt(columnNumber))): #a
			for j in range(0,int(math.sqrt(columnNumber))): #b
				for x in range(1,int(math.sqrt(columnNumber)+1)): #u
					for y in range(1,int(math.sqrt(columnNumber)+1)): #v
						for k in range(y+1,int(math.sqrt(columnNumber)+1)): #w
							print ("-%s -%s 0"%(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,z, columnNumber), convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+k,z, columnNumber)))
						for k in range(x+1,int(math.sqrt(columnNumber)+1)): #w
							for l in range(1,int(math.sqrt(columnNumber))+1): #t
								print ("-%s -%s 0"%(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,z, columnNumber), convertToDecimal(int(math.sqrt(columnNumber))*i+k,int(math.sqrt(columnNumber))*j+l,z, columnNumber)))

# -------------------
								
def atMostOneNumberInEachEntry(columnNumber, outputGrid):
	for x in range(1,columnNumber+1):
		for y in range(1,columnNumber+1):
			for z in range(1,columnNumber):
				for i in range(z+1,columnNumber+1):
					print ("-%s -%s 0" %(convertToDecimal(x,y,z, columnNumber), convertToDecimal(x,y,i, columnNumber)))
					
def eachNumberOncePerRow(columnNumber, outputGrid):
	for y in range(1,columnNumber+1):
		for z in range(1,columnNumber+1):
			list = ""
			first = True
			for x in range(1,columnNumber+1):
				if first == False:
					list += ' '
				first = False
				list += "%s" %(convertToDecimal(x,y,z, columnNumber))
			print ("%s 0" %list)
			
def eachNumberOncePerColumn(columnNumber, outputGrid):
	for x in range(1,columnNumber+1):
		for z in range(1,columnNumber+1):
			list = ""
			first = True
			for y in range(1,columnNumber+1):
				if first == False:
					list += ' '
				first = False
				list += "%s" %(convertToDecimal(x,y,z, columnNumber))
			print ("%s %s" %(list,0))
			
def eachNumberOncePerGrid(columnNumber, outputGrid):
	#print "eachNumberOncePerGrid"
	for z in range(1,columnNumber+1):
		#list = ""
		#first = True
		for i in range(0,int(math.sqrt(columnNumber))):
			for j in range(0,int(math.sqrt(columnNumber))):
				list = ""
				first = True
				for x in range(1,int(math.sqrt(columnNumber))+1):
					for y in range(1,int(math.sqrt(columnNumber))+1):
						if first == False:
							list += ' '
						first = False
						list += "%s" %(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,z, columnNumber))
				print ("%s %s" %(list,0))
		
def encodingCalls(columnNumber, outputGrid):
	if(columnNumber != 0):	#not the beginning of the file
		numclause=(columnNumber*columnNumber*int(math.sqrt(columnNumber))*int(nCr(columnNumber,2))) + (columnNumber*columnNumber)
		numvar=columnNumber*columnNumber*columnNumber
		#print ("p cnf %s %s" %(numvar,numclause)) #for minimal encoding clauses
		exnumclause = (columnNumber*columnNumber*(int(math.sqrt(columnNumber))+1)*int(nCr(columnNumber,2))) + (columnNumber*columnNumber*(int(math.sqrt(columnNumber))+1)) #minimal + extended encodings
		print ("p cnf %s %s" %(numvar,exnumclause))
		
		#print "minimal encoding"
		eachElementHasAtLeastOneNumber(columnNumber, outputGrid)	
		eachRowHasAtMostOneOfEachNumber(columnNumber, outputGrid)	
		eachColumnHasAtMostOneOfEachNumber(columnNumber, outputGrid)
		eachNumberAppearsAtMostOncePerGrid(columnNumber, outputGrid)
		
		#print "extended encoding"
		atMostOneNumberInEachEntry(columnNumber, outputGrid)
		eachNumberOncePerRow(columnNumber, outputGrid)
		eachNumberOncePerColumn(columnNumber, outputGrid)
		eachNumberOncePerGrid(columnNumber, outputGrid)

def hardInputToSudoku(input):
	newArr = []
	nums = ['1','2','3','4','5','6','7','8','9']
	
	for x in range(len(input)):
		if input[x] not in nums:
			newArr.append('0')
		else:
			newArr.append(input[x])
	
	str = ''.join(newArr)
	
	newGrid = []
	for x in range(0, len(input), int(math.sqrt(len(input)))):
		newGrid.append(str[x:x+int(math.sqrt(len(input)))])
		
	return newGrid

def main():
	
	if len(sys.argv) == 1:
		print ("No arguments")
	else:
		inputGrid = ""
		try:
			file = open(sys.argv[1])
			inputGrid = file.read()
			file.close()
		except:
			print ("Not a valid file")
			inputGrid = sys.argv[1]

		columnNumber = 0
		outputGrid = []
		
		boolGrid = False
		
		'''
		#below assumes only two types of inputs, 
			1. projecteuler.net/project/resources/p096 sudoku.txt
			2. magictour.free.fr/top95
		
		if there are other inputs, the for loop below might or might not function
		'''
		for x in inputGrid.splitlines():
			if x.startswith('Grid') and boolGrid is False:
				#print x
				boolGrid = True
			elif boolGrid is True and not x.startswith('Grid'):
				outputGrid.append(x)
				columnNumber = len(outputGrid[0])
			elif boolGrid is True and x.startswith('Grid'):
				encodingCalls(columnNumber, outputGrid)
				#print x
				outputGrid = []
				columnNumber = 0
			else: #this is for all other inputs, mainly magictour (hard inputs). Not sure of other inputs
				outputGrid = hardInputToSudoku(x)
				columnNumber = len(outputGrid)
				encodingCalls(columnNumber, outputGrid)
				
				#reset
				outputGrid = []
				columnNumber = 0				
		
		if outputGrid != []: #for the last grid
			encodingCalls(columnNumber, outputGrid) 
		
if __name__ == "__main__":
	main() 

