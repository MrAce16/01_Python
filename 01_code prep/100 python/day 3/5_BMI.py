# write a program that interprests the body mass index based on a user's body and height.
# under 18.5 they are underweight
# Equal to or over 25 but below 30 they are slighly overwight
# Equal to or over 30 but below 35 they are obsese
# Equal to over 35 they are clinically obese
# BMI = weight in kg / height

weight = int(input("Enter your weight in KG : "))
height = float(input("Enter your height in m : "))
bmi = weight / (height * height)

if bmi < 18.5:
    print(" you are under weight")
elif bmi < 25:
    print(" you are normal weight")
elif bmi < 30:
    print(" you are slightly overweight")
elif bmi > 35:
    print(" you are obsese")
else:
    print(" you are clinically obese")
