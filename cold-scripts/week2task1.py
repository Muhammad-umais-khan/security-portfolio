# Cold Script #2 asks you to extract IPv4 addresses using a regex consisting of four groups of 1–3 digits separated by dots. Chaining those blocks together looks like this: r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
import sys
import re
filePath = sys.argv[1]
count = 0
with open(filePath, "r") as logs:
    fileContent = logs.read();
    list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", fileContent)
    mySet = set(list)
    count = len(mySet)
print(mySet,"Total count: ",count)

