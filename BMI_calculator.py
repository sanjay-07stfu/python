print("WELCOME TO BMI CALCULATOR")

weight = float(input("Enter the weight of the person (in kg): "))
print("Weight:", weight)

height = float(input("Enter the height of the person (in meters): "))
print("Height:", height)

bmi = weight / (height ** 2)
print("BMI:", bmi)

if bmi < 18.5:
    print("UNDERWEIGHT")
elif 18.5 <= bmi < 24.9:
    print("NORMAL WEIGHT")
elif 25 <= bmi < 29.9:
    print("OVERWEIGHT")
elif bmi >= 30:
    print("OBESITY")
else:
    print("INVALID INPUT")
    print("THANK YOU")
    
