import sys
import math
import time

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
			print ("%s" %list)
		
def eachRowHasAtMostOneOfEachNumber(columnNumber, outputGrid):
	for y in range(1,columnNumber+1): #i
		for z in range(1,columnNumber+1): #k
			for x in range(1,columnNumber): #j
				for i in range(x+1,columnNumber+1): #l
					print ("-%s -%s" %(convertToDecimal(x,y,z, columnNumber),convertToDecimal(i,y,z, columnNumber)))
			
def eachColumnHasAtMostOneOfEachNumber(columnNumber, outputGrid):
	for x in range(1,columnNumber+1): #j
		for z in range(1,columnNumber+1): #k
			for y in range(1,columnNumber): #i
				for i in range(y+1,columnNumber+1): #l
					print ("-%s -%s" %(convertToDecimal(x,y,z, columnNumber), convertToDecimal(x,i,z, columnNumber)))
			
def eachNumberAppearsAtMostOncePerGrid(columnNumber, outputGrid):
	for z in range(1,columnNumber+1): #k
		for i in range(0,int(math.sqrt(columnNumber))): #a
			for j in range(0,int(math.sqrt(columnNumber))): #b
				for x in range(1,int(math.sqrt(columnNumber)+1)): #u
					for y in range(1,int(math.sqrt(columnNumber)+1)): #v
						for k in range(y+1,int(math.sqrt(columnNumber)+1)): #w
							print ("-%s -%s"%(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,z, columnNumber), convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+k,z, columnNumber)))
						for k in range(x+1,int(math.sqrt(columnNumber)+1)): #w
							for l in range(1,int(math.sqrt(columnNumber))+1): #t
								print ("-%s -%s"%(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,z, columnNumber), convertToDecimal(int(math.sqrt(columnNumber))*i+k,int(math.sqrt(columnNumber))*j+l,z, columnNumber)))

# -------------------
								
def atMostOneNumberInEachEntry(columnNumber, outputGrid):
	for x in range(1,columnNumber+1):
		for y in range(1,columnNumber+1):
			for z in range(1,columnNumber):
				for i in range(z+1,columnNumber+1):
					print ("-%s -%s" %(convertToDecimal(x,y,z, columnNumber), convertToDecimal(x,y,i, columnNumber)))
					
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
			print ("%s" %list)
			
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
			print ("%s" %list)
			
def eachNumberOncePerGrid(columnNumber, outputGrid):
	for z in range(1,columnNumber+1):
		list = ""
		first = True
		for i in range(0,int(math.sqrt(columnNumber))):
			for j in range(0,int(math.sqrt(columnNumber))):
				for x in range(1,int(math.sqrt(columnNumber))+1):
					for y in range(1,int(math.sqrt(columnNumber))+1):
						if first == False:
							list += ' '
						first = False
						list += "%s" %(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,z, columnNumber))
		print ("%s" %list)


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
		puzzleNumber = 0		
		t0 = time.time()
		ave = 0
		count = 0

		for x in inputGrid.splitlines():
			if x.startswith('Grid'):
				print x
				if(columnNumber != 0):	#not the beginning of the file
				
					print ("new puzzle, %s*%s" %(columnNumber,columnNumber))
					eachElementHasAtLeastOneNumber(columnNumber, outputGrid)	
					eachRowHasAtMostOneOfEachNumber(columnNumber, outputGrid)	
					eachColumnHasAtMostOneOfEachNumber(columnNumber, outputGrid)
					eachNumberAppearsAtMostOncePerGrid(columnNumber, outputGrid)
					
					atMostOneNumberInEachEntry(columnNumber, outputGrid)
					eachNumberOncePerRow(columnNumber, outputGrid)
					eachNumberOncePerColumn(columnNumber, outputGrid)
					eachNumberOncePerGrid(columnNumber, outputGrid)					
					
					outputGrid = []
					t1 = time.time()
					total = t1-t0
					#print('puzzle time')
					#print(total)
					ave = total + ave
					count = count + 1
					#run the input. what form to have the input in? string
				columnNumber = 0
			else:
				outputGrid.append(x)
				columnNumber += 1

			

		'''		
		if columnNumber != 0:
			t1 = time.time()
			print ("new puzzle, %s*%s" %(columnNumber,columnNumber))
			eachElementHasAtLeastOneNumber(columnNumber, outputGrid)	
			eachRowHasAtMostOneOfEachNumber(columnNumber, outputGrid)	
			eachColumnHasAtMostOneOfEachNumber(columnNumber, outputGrid)
			eachNumberAppearsAtMostOncePerGrid(columnNumber, outputGrid)
			#print ("more encoding")
			atMostOneNumberInEachEntry(columnNumber, outputGrid)
			eachNumberOncePerRow(columnNumber, outputGrid)
			eachNumberOncePerColumn(columnNumber, outputGrid)
			eachNumberOncePerGrid(columnNumber, outputGrid)
			
			total = t1-t0
			#print('puzzle time')
			#print(total)
			ave = total + ave
			count = count + 1
		'''
			
		
	#average = ave/count
	#print('average time')
	#print(average)
	#print('total time')
	#print(ave)	
		
if __name__ == "__main__":
	main() 

