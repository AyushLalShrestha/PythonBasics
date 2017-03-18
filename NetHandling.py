from urllib import request

durl = "https://www.tutorialspoint.com/python/python_tuples.htm"
outfile = open("webPage_2.html", "w")
conn = request.urlopen(durl)
csv = conn.readline()
csv_str = ""
while len(csv):
    outfile.write(str(csv))
    csv = conn.readline()
outfile.close()





