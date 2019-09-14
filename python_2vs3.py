
import json

dict_1 =  {
   'name':'Ayush',
   'l_name': 'Shrestha'
}

file = open("ayush", 'wb')
file.write(json.dumps(dict_1).encode())
file.close()

file_1 = open("ayush", 'rb')
contents = file_1.read()

print(contents)
print(type(contents))

file_1.close()

