def interests():
    print("Enter all your interest, one after another or \"stop\" ")
    s1 = set()
    interest = ""
    while interest != "stop":
        interest = input()
        if interest.lower() == "stop":
            break
        s1.add(interest)
    return s1
def tinderDasecond():
    print("first person: ")
    p1 = interests()
    print("second person: ")
    p2 = interests()
    common = p1.intersection(p2)
    if len(common)>= 3:
        print(f"You are a match made in heaven! You have {len(common)} interests in common")
    else:
        print("oh no. its not gonna work. find another person.")
tinderDasecond()



#print(interests())