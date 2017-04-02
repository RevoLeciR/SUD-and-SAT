import sys
import math

def returnValueAt(row, column, grid):
	return int(grid[column-1][row-1])

def convertToDecimal(x,y,z):
	return 81 * (x-1) + 9 * (y-1)+z
	
def eachElementHasAtLeastOneNumber(columnNumber, outputGrid):
	for x in range(1,columnNumber+1):
		for y in range(1,columnNumber+1):
			list = ""
			occurence = False
			for z in range(1,columnNumber+1):
				if(returnValueAt(x,y,outputGrid) != z and occurence == False):
					#actually dont bother printing this out in that case
					list += "%s " %(convertToDecimal(x,y,z))
				elif occurence == False:
					list = "%s " %(convertToDecimal(x,y,z))
					occurence = True
			print list
		
def eachRowHasAtMostOneOfEachNumber(columnNumber, outputGrid):
	for y in range(1,columnNumber+1):
		for z in range(1,columnNumber+1):
			for x in range(1,columnNumber):
				for i in range(x+1,columnNumber+1):
					string = ""
					if (returnValueAt(x,y,outputGrid) != z):
						string += "-%s " %(convertToDecimal(x,y,z))
					if (returnValueAt(i,y,outputGrid) != z):
						string += "-%s " %(convertToDecimal(i,y,z))
					if(string != ""):
						print string
			
def eachColumnHasAtMostOneOfEachNumber(columnNumber, outputGrid):
	for x in range(1,columnNumber+1):
		for z in range(1,columnNumber+1):
			for y in range(1,columnNumber):
				for i in range(y+1,columnNumber+1):
					string = ""
					if (returnValueAt(x,y,outputGrid) != z):
						string += "-%s " %(convertToDecimal(x,y,z))
					if (returnValueAt(x,i,outputGrid) != z):
						string += "-%s " %(convertToDecimal(x,i,z))
					if(string != ""):
						print string
			
def eachNumberAppearsAtMostOncePerGrid(columnNumber, outputGrid):
	for z in range(1,columnNumber+1):
		for i in range(0,int(math.sqrt(columnNumber))):
			for j in range(0,int(math.sqrt(columnNumber))):
				for x in range(1,int(math.sqrt(columnNumber)+1)):
					for y in range(1,int(math.sqrt(columnNumber)+1)):
						for k in range(y+1,int(math.sqrt(columnNumber)+1)):
							string = ""
							if (returnValueAt(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,outputGrid) != z):
								string += "-%s " %(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,z))
							if (returnValueAt(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+k,outputGrid) != z):
								string += "-%s " %(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+k,z))
							if(string != ""):
								print string
							for l in range(1,int(math.sqrt(columnNumber))+1):
								string = ""
								if (returnValueAt(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,outputGrid) != z):
									string += "-%s " %(convertToDecimal(int(math.sqrt(columnNumber))*i+x,int(math.sqrt(columnNumber))*j+y,z))
								if (returnValueAt(int(math.sqrt(columnNumber))*i+k,int(math.sqrt(columnNumber))*j+l,outputGrid) != z):
									string += "-%s " %(convertToDecimal(int(math.sqrt(columnNumber))*i+k,int(math.sqrt(columnNumber))*j+l,z))
								if(string != ""):
									print string


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
		for x in inputGrid.splitlines():
			if x.startswith('Grid'):
				if(columnNumber != 0):	#not the beginning of the file
					print "next puzzle: "
					eachElementHasAtLeastOneNumber(columnNumber, outputGrid)	
					eachRowHasAtMostOneOfEachNumber(columnNumber, outputGrid)	
					eachColumnHasAtMostOneOfEachNumber(columnNumber, outputGrid)
					eachNumberAppearsAtMostOncePerGrid(columnNumber, outputGrid)
					
					
					outputGrid = []
					#run the input. what form to have the input in? string
				columnNumber = 0
			else:
				outputGrid.append(x)
				columnNumber += 1
		if columnNumber != 0:
			print "next puzzle: "
			eachElementHasAtLeastOneNumber(columnNumber, outputGrid)	
			eachRowHasAtMostOneOfEachNumber(columnNumber, outputGrid)	
			eachColumnHasAtMostOneOfEachNumber(columnNumber, outputGrid)
			eachNumberAppearsAtMostOncePerGrid(columnNumber, outputGrid)
		
if __name__ == "__main__":
	main() 