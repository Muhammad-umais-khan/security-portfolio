# Set a 20-minute timer. Create a fake log file with random text and some 3-digit HTTP status codes scattered inside (like 404, 200, 500). Then, write a script from scratch that:
# Takes the file path from the command line.
# Opens and reads the entire file.
# Uses re.findall() to extract every 3-digit number. (The regex pattern for exactly three digits is r"\d{3}").
# Converts the results into a set to destroy duplicates.
# Prints the unique codes and their total count.
import sys
import re
filePath = sys.argv[1]
with open(filePath, "r") as file:
        threeDig = re.findall(r"\d{3}", file.read())

digSet = set(threeDig)
count  = len(digSet)
print("total count: " , count)
for each in digSet:
    print(each)
        
