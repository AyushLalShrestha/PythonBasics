import re
import json


regEx = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
results = re.search(regEx,"192.168.2.22")

with open('my_data.json', 'r') as f:
	data = f.read()
	data_json = json.loads(data)
	print data_json



"""
infile = open("calmBlue.jpg", "rb")
outfile = open("copy.jpg", "wb")

bufferSize = 10000
buffer = infile.read(bufferSize)
while len(buffer):
	outfile.write(buffer)
	buffer = infile.read(bufferSize)

"""