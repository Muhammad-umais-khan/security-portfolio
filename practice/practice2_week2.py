# Create a messy text file named emails.txt containing random words and a few fake email addresses scattered throughout. Make sure to include a duplicate email (e.g., put admin@corp.com in there twice).
# Write a script from scratch that does the following:
# Takes the file path from the command line (sys.argv[1]).
# Opens the file and reads the entire text at once.
# Uses re.findall() to extract every email address.(Hint: The regex pattern for a basic email is r"\w+@\w+\.\w+" which translates to "word @ word . word").
# Converts the resulting list into a set to remove the duplicates.
# Prints the unique emails, separated by a comma on one line, and the total count of unique emails on the next line.
import sys
import re
filePath = sys.argv[1]
with open(filePath, "r") as file:
    emailList = re.findall(r"\w+@\w+\.\w+", file.read())
noDupList = set(emailList)
count = len(noDupList)
for email in noDupList:
    print(email, end= ",")
print("\n total count: " , count)