from urllib import request
import json

url = "https://www.w3schools.com/angular/customers.php"
conn = request.urlopen(url)
w_page = conn.read()
data = json.loads(w_page)

print(data)

for customer in data['records']:
    print("Customer Name: " + customer["Name"])




