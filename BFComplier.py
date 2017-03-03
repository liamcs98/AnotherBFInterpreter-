#This is going to input either a file of BF, or an input
import sys
import os 
dataPoints = []
BFProgram = ""
CurrentPosition = 0
indexIntoString = 0
fileName = "BFTestProgram.txt"
approvedSmybols = ["+","-",">","<",".",",","[","]"]

def createArrayOfData():
	for x in range(30000):
		dataPoints.append(0)
	#print(dataPoints)

def parseBFProgram(filename):
	file = open(filename, "r")
	global BFProgram
	for line in file:
		for element in line:
			if element in approvedSmybols:
				BFProgram += element

def FindFilesInDir():
	global fileName
	brainFuckFiles = 0
	potFiles = []
	dir_path = os.path.dirname(os.path.realpath(__file__))
	for file in os.listdir(dir_path):
		filenameFor, file_extension = os.path.splitext(os.path.join(dir_path,file))
		if file_extension == ".b":
			potFiles.append(file)
			brainFuckFiles += 1
	
	#Assigning FileName
	if brainFuckFiles == 1:
		fileName = potFiles[0]
	elif brainFuckFiles == 0:
		print("Want to give me a file?")
		quit()
	elif brainFuckFiles > 1:
		print("So, couple of files you might want to run.")
		print(potFiles)
		FileNameTemp = input("Which will it be mate?\n")
		fileName = FileNameTemp.strip(" ")


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
	FindFilesInDir()
	print(fileName)
	createArrayOfData()
	parseBFProgram(fileName)
	print(BFProgram)
	#meatAndPotatos()

main()
