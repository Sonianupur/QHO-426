def box(word):
    length = len(word)
    print("#"* (length+4))
    print("#" + word + "#")
    print("#"* (length+4))

def low(word):
    print(word.lower())

def upper(word):
    print(word.upper())

def mirror(word):
    print(word, " | ", word[::-1])

def repeat(word):
    n = int(input("how many times to repeat: "))
    for i in range(n):
        if i % 2 == 0:
            upper(word)
        else:
            low(word)

def spastic_writing(word):
    for i in range(len(word)):
        if i % 2 == 0:
            print(word[i].upper(), end = "")
        else:
            print(word[i].lower(), end = "")

def run():
    w = input(" Enter a word: ")
    print(" choose an option: \n1- Box\n2-Lower Case\n3-Upper case\n4-spastic_writing")
    opt = int(input())
    if opt == 1:
        box(w)
    elif opt == 2:
        low(w)
    elif opt == 3:
        upper(w)
    elif opt == 4:
        mirror(w)
    elif opt == 5:
        repeat(w)
    elif opt == 6:
        spastic_writing(w)


spastic_writing("Python is cool.")

repeat("cows can fly!")

mirror("Hamburger")
mirror("Kayak")

# slicing- separating/ accessing of individual item accessing/list of character in a string.
#slice using[start: end: step]

word = "This is sparta!"
print(word[::-1])

low("Jacket Potato")
upper("Rambo is fun")
box("Gary Linekar")
box("drama")

run()