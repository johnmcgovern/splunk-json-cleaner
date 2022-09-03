import re
import sys


# Get file base path in arguments
try:
    file_key = sys.argv[1]
    print("\nFile Key (Without Extension):", sys.argv[1])
except: 
    print("No file specified. Exiting")
    exit()


inputLogLocation = "data/" + file_key + "-in.json"
outputLogLocation = "data/" + file_key + ".json"

print("Input File: " + inputLogLocation)
print("Output File: " + outputLogLocation + "\n")

myInputFile = open(inputLogLocation, "r", encoding='utf-8', errors='ignore')
myOutputFile = open(outputLogLocation, "w")

counter = 1

for line in myInputFile:
    if counter == 1:
        print("First Line Before: " + line)

    line = re.sub(r"^\{.*?result\":","", line)
    line = re.sub(r"}$", "", line)

    if counter == 1:
        print("First Line After: " + line)

    counter += 1       

    myOutputFile.write(line)   
