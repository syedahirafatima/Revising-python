age = int(input("What is your age: "))
if age == 18 or age > 18:
    print("You are an adult.")
elif age < 18 and age >= 0:
    print("You are a minor.")
elif age < 0:
    print("PLease enter a valid input!")
else:
    print("PLease enter a valid input!")
