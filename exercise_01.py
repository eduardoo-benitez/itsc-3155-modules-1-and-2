i = int(input("Enter a grade from 0 to 100: "))

if (i >= 90):
    print("Your grade is A")
elif (i < 90 and i >= 80):
    print("Your grade is B")
elif (i < 80 and i >= 70):
    print("Your grade is C")
elif (i < 70 and i >= 60):
    print("Your grade is D")
else:
    print("Your grade is F")