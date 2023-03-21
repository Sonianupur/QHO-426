#initialize empty dictionary
d  = {}
dictio = dict()
# initialise non-empty dictionary
phonebook = {"Thomas":7964536124,"Aga":7769988766,"mD":7754234455}

print(phonebook)
#print/ access of middle element
name = input("who you gonna call: ")
if name in phonebook:

    print(f"callin....{phonebook[name]}")
else:
    print(f"No number for {name}")
#zipping two lists together to compose a dictionary
names = ["garry", "Ian", "Laura"]
age = [56, 21, 16]
people = dict(zip(names, age))
print(people)
#Traversing dictionary= accessing keys/values/both
for thing in people:
    print(thing)
for thing in people.values():
    print(thing)
for thing in people.keys():
    print(thing)
for k, v in people.items():
    print(f"Person {k} is {v} years old")