import re

# Appending a text file
# with open("file1.txt", mode="a", encoding="UTF-8") as fh2:
#     fh2.write("\n Whats up agein, this a new line of text \n")

# Replace all john with jan, & viceversa
fh = open("file.txt")
strLine = ""
for line in fh:
    strLine1 = line
    if re.search("john", line):
        strLine1 = line.replace("john", "jan")
        print("Replacing.. \n")
    strLine = strLine + strLine1
fh.close()

with open("file.txt", mode="w", encoding="UTF-8") as fh1:
    fh1.write(strLine)









