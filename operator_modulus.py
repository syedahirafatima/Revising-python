# practice 1
a = eval(input(f"Enter \"a\" number:"))
b = eval(input(f"Enter \"b\" number:"))
remainder = a % b
print(f"Remainder when {a} is divided by {b} is {remainder}")

# Program for checking if the number is even or odd
num  = 4
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
 #Prgram for checking if the number is even or odd using user input
num = eval(input("Enter the number you want to check whether it's even or odd: "))
if num % 2 == 0:
    print(f"Your given number \"{num}\" is even.")
else:
    print(f"Your given number \"{num}\" is odd.")
