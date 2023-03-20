while True:
    print("pls choose one of the following opt: \n1-Nice message\n2-area of rectangle\n3- area of triangle\n4-Times table. \n5- Exit.")
    opt = int(input())
    if opt == 1:
        print("you do not smell bad today!")
    elif opt == 2:
        h = float(input("Enter height: "))
        b = float(input("Enter the base: "))
        print(f"the area of rectangle is {h*b}cm^2")
    elif opt == 3:
        h = float(input("Enter Height: "))
        b = float(input("Enter the base: "))
        print(f"The area of this triangle is {h*b*0.5}cm^2")
    elif opt == 4:
        n = int(input("enter whole number: "))
        for i in range(1, 11, 1):
            print(f"{n}x{i}={n*i}")
    elif opt == 5:
        break
    else:
        print("no such option. ")


