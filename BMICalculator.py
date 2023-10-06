weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

height_in_meters = height / 100

BMI = weight / height_in_meters ** 2

print("Your BMI is:",  BMI)

if BMI < 18.5:
    print ("You are Underweight")

elif BMI <= 25:
    print("You have a healthy weight ")

elif 25 <= BMI < 30:
    print("You are OverWeight")

else:
    print("You are Obs")
