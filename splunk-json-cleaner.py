import re

inputLogLocation = "logs-final/badlogs-final.log"
outputLogLocation = "logs-final/badlogs.log"

print("Input File: " + inputLogLocation)
print("Output File: " + outputLogLocation + "\n")

myInputFile = open(inputLogLocation, "r")
myOutputFile = open(outputLogLocation, "a")
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


# inputLogLocation = "logs-final/badlogs-final.log"
# outputLogLocation = "logs-final/badlogs.log"

# print("Input File: " + inputLogLocation)
# print("Output File: " + outputLogLocation + "\n")

# myInputFile = open(inputLogLocation, "r")
# myOutputFile = open(outputLogLocation, "a")
# myOutputFile = open(outputLogLocation, "w")

# counter = 1

# for line in myInputFile:
#     if counter == 1:
#         print("First Line Before: " + line)

#     line = re.sub(r"^\{.*?result\":","", line)
#     line = re.sub(r"}$", "", line)

#     if counter == 1:
#         print("First Line After: " + line)

#     counter += 1       

#     myOutputFile.write(line)       

