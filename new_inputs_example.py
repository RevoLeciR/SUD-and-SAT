import math

#use a test string
test = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......" #row 1: 4.....8.5

#this list is for whatever is valid to put into a cell
nums = ['1','2','3','4','5','6','7','8','9']

#char list
newarr = []

#check the test string for any character that is not in nums
for x in range(len(test)):
	if test[x] not in nums: #any char in test string that is not in nums will get appended into newarr as 0
		newarr.append('0')
	else:
		newarr.append(test[x]) #any char in test string that is in nums will get appended as itself in new arr

#this will turn the newarr char list into a string. join is in the str library
newstr = ''.join(newarr)

#this will separate the rows into their respective areas on the board. NOTE: this is specifically for a 9x9 board
for x in range(0,len(test),int(math.sqrt(len(test)))): 
	print newstr[x:x+int(math.sqrt(len(test)))] #splice the string