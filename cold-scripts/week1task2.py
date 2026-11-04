#  Write a script that takes a file name and a single character from the command line, then prints the total number of times that specific character appears across the entire document.
# The Arguments: sys.argv[1] will be your file path, and sys.argv[2] will be your target character (for example, e or !).
import sys
filePath = sys.argv[1]
target = sys.argv[2]
count = 0
with open(filePath, "r") as file:
    for line in file:
        for char in line:
            if (target == char):
                count += 1
print(count)