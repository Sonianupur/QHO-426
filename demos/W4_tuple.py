# declare a tuple
x = ("Piotr", 68, True)
y = tuple(["Garry", 32, False])
# print tuple
print(x)
print(y)
print(x[1])
#cannot change individual items
#x[1] = 69 it do not work .
# concatenate tuple
z = x + y
print(z)
print(y)
print(x)
# using min and max function in tuple.
h = (74, 68, 45, 35, 15, 1, 82)
print(max(h))

#canging tuple .
lista = list(h)
temp = lista[0]
lista[0] = lista[1]
lista[1] = temp
h1 = tuple(lista)
print(h1)
# can use of del but not .pop .insert
del h1
