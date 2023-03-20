print("pls enter the first number")
first_number = int(input())
print("pls enter the second number")
second_number = int(input())
print("pls enter the third number")
third_number = int(input())
even_numbers = 0
odd_numbers = 0
if(first_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if (second_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if (third_number % 2 == 0):
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
print("there are even numbers and odd numbers")