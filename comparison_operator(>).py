num = eval(input("Enter a number"))
if num > 0:
    print(f"{num} is positive.")
elif num == 0:
    print(f"{num} is neutral as it's zero.")
else:
    print(f"{num} is negative.")


# 0 is a constraint as its not negative nor positive, it's neutral
# eval works even if a points value is added (float)


