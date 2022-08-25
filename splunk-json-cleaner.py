import re

inputLogLocation = "data/in.json"
outputLogLocation = "data/out.json"

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
