from urllib import request

durl = "https://www.tutorialspoint.com/python/python_tuples.htm"
outfile = open("webPage.txt", "w")
conn = request.urlopen(durl)
csv = conn.read()
csv_str = str(csv)
lines = csv_str.split("\\n")
for line in lines:
    outfile.write(line + "\n")
outfile.close()





