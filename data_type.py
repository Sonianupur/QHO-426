
print("what is your name?")
name = input()
print("what is your age?")
age = int(input())
print("What is your weight?")
weight = float(input())
print("What is your height")
height = float(input())
#caculate bmi
bmi = weight/(height**2)
print(f"{name} your bmi is{bmi}")