height = float(input("enter height in foot : "))
height_in_meters = height*12/39.37
weight = int(input("enter weight in Kg : "))
BMI = weight/pow(height_in_meters, 2)
print("BMI :- ", BMI)
if BMI > 25:
    print("Overweight")
elif BMI < 18:
    print("Underweight")
else:
    print("Fit")
