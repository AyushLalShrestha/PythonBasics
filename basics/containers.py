

# Sets
name = {"ayush", "astha", "anita", "mahendra"}
name.add("anita")

# Dictionary
person_info = {"name":"Ayush", "address":"sanepa", "age":20}
for attr in person_info:
    print("{}: {}".format(attr, person_info[attr]))

# List
names = []
names.append("Robert")
names.append("John")
names.extend(["Richard", "James",])

# List of dictionaries
people = [
    {'name':'ayush', 'age':22},
    {'name':"Mahendra", 'age':59}
]
for person_info in people:
    print("name: " + person_info['name'] + " aged: " + str(person_info['age']))




