import re

#Appending a text file
#with open("file1.txt", mode="a", encoding="UTF-8") as fh2:
    #fh2.write("\n Whats up agein, this a new line of text \n")

#Replace all astha with mahendra and viceversa
fh = open("file1.txt")
strLine = ""
for line in fh:
    strLine1 = line
    if re.search("astha", line):
        strLine1 = line.replace("astha", "elephante")
        print("Replacing.. \n")
    strLine = strLine + strLine1
fh.close()

with open("file1.txt", mode="w", encoding="UTF-8") as fh1:
    fh1.write(strLine)









