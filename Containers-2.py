
#person = ("Anita", "Jawalakhel", 1231299, "anita@gmail.com", "MA/2068,555")
#print(type(person[3]))
#print(person)


person2 = {"name": "Mahendra", "address": "Kathmandu", "contact": 3234556, "job": "Java Developer"}
person1 = {"name": "Ayush", "address": "Lalitpur", "contact": 4545, "job": "Python Developer"}
personList = [person1, person2]

personList.append({"name": "Astha", "address": "Kupondole", "contact": 567657, "job": "Microbiologist"})
personList.append({"name": "Anita", "address": "Jhamsikhel", "contact": 527657, "job": "Housewife"})

for person in personList:
    print(person["name"] + " " + str(person["contact"]) + " " + person["job"])