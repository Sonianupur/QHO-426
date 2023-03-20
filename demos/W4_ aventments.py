# adding
def adding(lista = []):
    new_member = input("Enter new hero: ")
    lista.append(new_member)

def removing(lista = []):
    rejected = input("Enter hero to be removed: ")
    if rejected in lista:
        lista.remove(rejected)

def printing(lista = []):
    for hero in lista:
        print(f"The mighty {hero} is part of avengers!")

def run():
    avengers = []
    while True:
        opt = int(input("Avengers , Assemble!\n\n1- add a member\n2-remove a member\n3- check on team \n9-exit\noption:"))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            removing(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 9:

            break
        else:

            print("sort yourself out!")
run()
