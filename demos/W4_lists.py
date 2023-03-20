# declare a list

bleh = []
meh = list()

# declare a non empty list
yummy = ["chicken", "Ice cream","Chocolate", "chips" ]
# print entire list
print(yummy)
# print a single item
print(yummy[-3])
#print some items
print(yummy[1:3])
# add elements to list
print(bleh)
bleh.append("marmite")
bleh.append("tomato")
bleh.append("liver")
bleh.append("carrot")
bleh.append("Anchoive")
print(bleh)
yummy.append("Pierogi")
print(yummy)
#add amultiple items to a list
#n = int(input("How many items to add: "))
for i in range(2):
 bleh.append(input("Enter horrible food: "))
print (bleh)
bleh.extend(["horse meat", "Pancakes"])
print(bleh)


# insert item in specific position.
bleh.insert(1, "cabbage")
print(bleh)
bleh.insert(4, "onions")
print(bleh)

#remove items from list
if "carrot" in bleh:
 bleh.remove("carrot")
 if "taco" in bleh:
  bleh.remove("toco")
print(bleh)
# remove item by index
x = bleh.pop(5) #returns  taht value
print(x)
print(bleh)
#alternating way of deleting by index
del bleh[4]
print(bleh)
# check  a list for particular datya type/traverse the list
lista = ["Fred", 56, True, 99.4, "Potato", True, 82]
sum = 0
for item in lista:
 #]if isinstance(item, int):

 if isinstance(item, int):
  sum += item
  print(sum)


  #print(item, end = "**@**")


 #print(type(bleh))
 #print(type(meh))