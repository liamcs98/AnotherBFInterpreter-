#This is going to input either a file of BF, or an input
import sys
dataPoints = []
BFProgram = ""
CurrentPosition = 0
indexIntoString = 0
fileName = ""

def createArrayOfData():
	for x in range(30000):
		dataPoints.append(0)
	#print(dataPoints)

def parseBFProgram(filename):
	file = open(filename, "r")
	global BFProgram
	for line in file:
		for element in line:
			BFProgram += element



def meatAndPotatos():
	global BFProgram
	global indexIntoString
	global CurrentPosition

	while indexIntoString < len(BFProgram):
		element = BFProgram[indexIntoString]
		if element == "+":
			dataPoints[CurrentPosition] += 1
		elif element == "-":
			dataPoints[CurrentPosition] -= 1
		elif element == ">":
			#print(">")
			CurrentPosition += 1
		elif element == "<":
			#print("<")
			CurrentPosition -= 1
		elif element == ".":
			sys.stdout.write(chr(dataPoints[CurrentPosition]))
			sys.stdout.flush()
		elif element == ",":
			pass
		elif element == "[":
			if dataPoints[CurrentPosition] == 0:
				indexIntoString += 1
				howdeep = 1
				while howdeep != 0:
					char = BFProgram[indexIntoString]
					if char =="[":
						howdeep += 1
					elif char == "]":
						howdeep -= 1
					indexIntoString += 1
				indexIntoString -= 1


		elif element == "]":
			if dataPoints[CurrentPosition] != 0:
				indexIntoString -= 1
				howdeep = 1
				while howdeep != 0:
					char = BFProgram[indexIntoString]
					if char =="[":
						howdeep -= 1
					elif char == "]":
						howdeep += 1
					indexIntoString -= 1
				indexIntoString += 1

		indexIntoString += 1



def main():
	fileName = input("File pls")
	createArrayOfData()
	parseBFProgram(fileName)
	meatAndPotatos()

main()
