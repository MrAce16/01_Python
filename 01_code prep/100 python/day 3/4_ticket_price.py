height = int(input("Enter the height in cm :"))

if height > 120:
    print("you can ride")
    age = int(input("Enter the age :"))
    if age < 12:
        print("fare price is 5$")
    elif age > 12 and age <= 18:
        print("fare price is 7$")
    else:
        print("fare is 12 $")


else:
    print("you can't ride")
