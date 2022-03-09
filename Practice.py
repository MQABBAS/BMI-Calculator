# My Code
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)


if bmi < 24:
    print('You are in the underweight range!')

else:
    print('You are in the overweight range!')
