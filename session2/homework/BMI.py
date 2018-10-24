height = int(input("enter the height (cm) = "))
weight = int(input("enter the weight (kg) = "))
m = height/100
BMI = weight/(m*m)
print("BMI = ", BMI)
if BMI<16:
    print("Severely underweight")
elif BMI<18.5:
    print("Underweight")
elif BMI<25:
    print("Normally")
elif BMI<30:
    print("Overweight")
else:
    print("Obese")