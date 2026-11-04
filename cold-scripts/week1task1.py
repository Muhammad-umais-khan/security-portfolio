# write a program that takes a file name and a keyword from the command line, then prints how many lines in that file contain the keyword.
import sys
counter = 0
keyword = sys.argv[2]
filePath = sys.argv[1]
with open(filePath , "r" ) as file:
    for line in file:
            if(keyword in line):
                counter = counter+1

print(counter)