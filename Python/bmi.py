print("\n")
print("Welcome to the BMI (Body Mass Index) Calculator")
print("Please Note: This calculator may not always provide accurate values if you are not within the age range of 18-50.")
print("\n")
print("Please choose which unit you will be providing your weight in - kilograms or pounds.")
weight_unit=input("For kilograms (kg), for pounds (lb): ")

if(weight_unit == 'kg'):
    print("Please choose which unit you will be providing your height in - inches or centimeters.")
    tall_unit=input("For inches (in) for centimeters (cm): ")
    if(tall_unit == 'in'):
        kilo = float(input("Enter your weight in kg: "))
        inch = int(input("Enter your height in inches, to the nearst whole number: "))
        tall = inch / 39.37
        weight = kilo

    elif(tall_unit == 'cm'):
        kilo = float(input("Enter your weight in kg: "))
        met = int(input("Enter your height in centimeters, to the nearst whole number: "))
        tall = met / 100
        weight = kilo

    else:
        print("Invalid Input Please Try Again!")

    bmi = weight / (tall ** 2)
            
elif(weight_unit == 'lb'):
    print("Please choose which unit you will be providing your height in - inches or centimeters.")
    tall_unit=input("For inches (in) for centimeters (cm): ")
    if(tall_unit == 'in'):
        lb = float(input("Enter your weight in kg: "))
        inch = int(input("Enter your height in inches, to the nearst whole number: "))
        tall = inch
        weight = lb

    elif(tall_unit == 'cm'):
        lb = float(input("Enter your weight in kg: "))
        met = int(input("Enter your height in centimeters, to the nearst whole number: "))
        tall = met / 2.54
        weight = lb

    else:
        print("Invalid Input Please Try Again!")

    bmi = (703 * (weight / (tall ** 2)))


else:
    print("Invalid Input Please Try Again!")
    sys.exit(1)

print("\n")
final_bmi = "{:.2f}".format(bmi)

if (bmi <= 16): 
    print("Your BMI is ", final_bmi, ". This means you are Severely underweight.")
elif (bmi <= 18.5 and bmi > 16): 
    print("Your BMI is ", final_bmi, ". This means you are Slightly Underweight.")
elif (bmi <= 24.9 and bmi > 18.5): 
    print("Your BMI is ", final_bmi, ". This means you are Healthy and in the Perfect BMI Range.")
elif (bmi <= 29.9 and bmi > 24.9): 
    print("Your BMI is ", final_bmi, ". This means you are Overweight.")
elif (bmi <= 34.5  and bmi > 29.9): 
    print("Your BMI is ", final_bmi, ". This means you are Obsese (Obesity Class 1).")
elif (bmi <=  39.9 and bmi > 34.5): 
    print("Your BMI is ", final_bmi, ". This means you are Obsese (Obesity Class 2).")
elif (bmi > 40): 
    print("Your BMI is ", final_bmi, ". This means you are Severely Obese (Obesity Class 3).")
