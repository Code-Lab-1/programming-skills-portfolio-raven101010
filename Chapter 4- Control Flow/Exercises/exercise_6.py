
# BMI CALCULATOR
Weight = int(input())
Height = float(input())


BMI = Weight/(Height)**2



if BMI < 18.5:
    print("Underweight")

elif BMI >= 18.5 and BMI < 25:
  print("Normal")

elif BMI >= 25 and BMI < 30:
    print("Overweight")


elif BMI >30:
    print("Obesity")

