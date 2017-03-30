def convertToDecimal(x,y,z):
	return 81 * (x-1) + 9 * (y-1)+z
	
def eachElementHasAtLeastOneNumber():
	for x in range(1,10):
		for y in range(1,10):
			list = ""
			for z in range(1,10):
				list += "%s " %(convertToDecimal(x,y,z))
			print list
		
def eachRowHasAtMostOneOfEachNumber():
	for y in range(1,10):
		for z in range(1,10):
			for x in range(1,9):
				for i in range(x+1,10):
					print "-%s -%s" %(convertToDecimal(x,y,z), convertToDecimal(i,y,z))
			
def eachColumnHasAtMostOneOfEachNumber():
	for x in range(1,10):
		for z in range(1,10):
			for y in range(1,9):
				for i in range(y+1,10):
					print "-%s -%s" %(convertToDecimal(x,y,z), convertToDecimal(x,i,z))
			
def eachNumberAppearsAtMostOncePerGrid():
	for z in range(1,10):
		for i in range(0,3):
			for j in range(0,3):
				for x in range(1,4):
					for y in range(1,4):
						for k in range(y+1,4):
							print "-%s -%s" %(convertToDecimal(3*i+x,3*j+y,z), convertToDecimal(3*i+z,3*j+k,z))
							for l in range(1,4):
								print "-%s -%s" %(convertToDecimal(3*i+x,3*j+y,z), convertToDecimal(3*i+k,3*j+l,z))
			
def main():
	eachElementHasAtLeastOneNumber()	
	eachRowHasAtMostOneOfEachNumber()	
	eachColumnHasAtMostOneOfEachNumber()
	eachNumberAppearsAtMostOncePerGrid()	
		
if __name__ == "__main__":
	main() 
