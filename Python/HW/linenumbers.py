userFile = input("What is the filename? (in the form 'example.py'): ")
try:
    infile = open(userFile,'r')
except FileNotFoundError:
    print("Sorry, no file found.")
lineNum = 'ln_' + userFile
outfile = open(lineNum, 'w')
lineCount = 0
for line in infile:
    lineCount += 1
    lineCount = str(lineCount)
    outfile.write(lineCount)
    outfile.write("  ")
    outfile.write(line)
    lineCount = int(lineCount)
infile.close()
outfile.close()
print("Mission Accomplished")
