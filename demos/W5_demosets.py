#initialize empty set
s = set()
#initializing non-empty set
colours = {"blue","red", "yellow","purple", "red"}
print(colours)
#adding elements into sets.
colours.add("green")
colours.add("navy blue")
print(colours)
colours = colours.union({"black", "turquise", "crimson", "purple"})
print(colours)
#removing item from a set
if "yellow" in colours:
    colours.remove("yellow")
print(colours)
#sets are heterogeneous and duplicates are not allowed
colours.add(99)
colours.add(True)
print(colours)
# check memebership
if"yellow" in colours:
    print("yey-I like yellow!")
else:
    print("sad days, no yellow  :( ")

c = {"brown", "turquise", "cyan", "coquelicot", "pink", "red"}

#union = join 2 sets together, not keeping dupliocates
c2 = colours.union(c)
print(f"c is {c}")
print(f"c2 is {c2}")
print(f"colours is {colours}")
#intersection- looking at common value of 2 collections
c3 = c.intersection(colours)
print(f"c3 is {c3}")
# difference- keep elements of one set that are not part of others.
c4 = colours.difference(c)
c5 = c.difference(colours)
print(f"c4 is{c4}")
print(f"c5 is {c5}")
