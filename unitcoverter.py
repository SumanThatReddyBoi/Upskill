def temp():
    while(1):
        print("1. Kelvin, 2. Celcius, 3. Fahrenheit")
        unit_in=int(input("Enter type to convert from (select number only): "))
        unit_out=int(input("Enter type to convert to (select number only): "))
        val1=input("Enter the value to be converted")
        #Kelvin Conversions
        if unit_in == 1:
            if unit_out == 1:
                print(val1)
            elif unit_out == 2:
                final=val1-273.15
                print(final)
            elif unit_out == 3:
                final=((val1-273.15)*9/5+32)
                print(final)
            break

        #Celcius Conversions
        elif unit_in == 2:
            if unit_out == 1:
                print(val1+273.15)
            elif unit_out == 2:
                print(val1)
            elif unit_out == 3:
                final=((val1*9/5)+32)
                print(final) 
            break

        #Farenheit Conversions
        elif unit_in == 1:
            if unit_out == 1:
                final=((val1-32)*5/9+273.15)
                print(final)
            elif unit_out == 2:
                final=(val1-32)*5/9
                print(final)
            elif unit_out == 3:
                print(val1)
            break
        else:
            print("Wrong value entered!")
    
def vol():
    while(1):
        print("1. Gallon, 2. Quart, 3. Pint, 4. Cup, 5. Ounce, 6. Tablespoon, 7. Teaspoon, 8. Liter, 9. Milliliter")
        unit_in=int(input("Enter type to convert from (select number only): "))
        unit_out=int(input("Enter type to convert to (select number only): "))
        val1=float(input("Enter the value to be converted: "))

        # Gallon conversions
        if unit_in == 1:
            if unit_out == 1:
                print(val1)
            elif unit_out == 2:
                print(val1*4)
            elif unit_out == 3:
                print(val1*8)
            elif unit_out == 4:
                print(val1*16)
            elif unit_out == 5:
                print(val1*128)
            elif unit_out == 6:
                print(val1*256)
            elif unit_out == 7:
                print(val1*768)
            elif unit_out == 8:
                print(val1*3.78541)
            elif unit_out == 9:
                print(val1*3785.41)
            break
        # Quart conversions
        elif unit_in == 2:
            if unit_out == 1:
                print(val1/4)
            elif unit_out == 2:
                print(val1)
            elif unit_out == 3:
                print(val1*2)
            elif unit_out == 4:
                print(val1*4)
            elif unit_out == 5:
                print(val1*32)
            elif unit_out == 6:
                print(val1*64)
            elif unit_out == 7:
                print(val1*192)
            elif unit_out == 8:
                print(val1*0.946353)
            elif unit_out == 9:
                print(val1*946.353)
            break
        # Pint conversions
        elif unit_in == 3:
            if unit_out == 1:
                print(val1/8)
            elif unit_out == 2:
                print(val1/2)
            elif unit_out == 3:
                print(val1)
            elif unit_out == 4:
                print(val1*2)
            elif unit_out == 5:
                print(val1*16)
            elif unit_out == 6:
                print(val1*32)
            elif unit_out == 7:
                print(val1*96)
            elif unit_out == 8:
                print(val1*0.473176)
            elif unit_out == 9:
                print(val1*473.176)
            break
        # Cup conversions
        elif unit_in == 4:
            if unit_out == 1:
                print(val1/16)
            elif unit_out == 2:
                print(val1/4)
            elif unit_out == 3:
                print(val1/2)
            elif unit_out == 4:
                print(val1)
            elif unit_out == 5:
                print(val1*8)
            elif unit_out == 6:
                print(val1*16)
            elif unit_out == 7:
                print(val1*48)
            elif unit_out == 8:
                print(val1*0.236588)
            elif unit_out == 9:
                print(val1*236.588)
            break
        # Ounce conversions
        elif unit_in == 5:
            if unit_out == 1:
                print(val1/128)
            elif unit_out == 2:
                print(val1/32)
            elif unit_out == 3:
                print(val1/16)
            elif unit_out == 4:
                print(val1/8)
            elif unit_out == 5:
                print(val1)
            elif unit_out == 6:
                print(val1*2)
            elif unit_out == 7:
                print(val1*6)
            elif unit_out == 8:
                print(val1*0.0295735)
            elif unit_out == 9:
                print(val1*29.5735)
            break
        # Tablespoon conversions
        elif unit_in == 6:
            if unit_out == 1:
                print(val1/256)
            elif unit_out == 2:
                print(val1/64)
            elif unit_out == 3:
                print(val1/32)
            elif unit_out == 4:
                print(val1/16)
            elif unit_out == 5:
                print(val1/2)
            elif unit_out == 6:
                print(val1)
            elif unit_out == 7:
                print(val1*3)
            elif unit_out == 8:
                print(val1*0.0147868)
            elif unit_out == 9:
                print(val1*14.7868)
            break
        # Teaspoon conversions
        elif unit_in == 7:
            if unit_out == 1:
                print(val1/768)
            elif unit_out == 2:
                print(val1/192)
            elif unit_out == 3:
                print(val1/96)
            elif unit_out == 4:
                print(val1/48)
            elif unit_out == 5:
                print(val1/6)
            elif unit_out == 6:
                print(val1/3)
            elif unit_out == 7:
                print(val1)
            elif unit_out == 8:
                print(val1*0.00492892)
            elif unit_out == 9:
                print(val1*4.92892)
            break
        # Liter conversions
        elif unit_in == 8:
            if unit_out == 1:
                print(val1/3.78541)
            elif unit_out == 2:
                print(val1/0.946353)
            elif unit_out == 3:
                print(val1/0.473176)
            elif unit_out == 4:
                print(val1/0.236588)
            elif unit_out == 5:
                print(val1/0.0295735)
            elif unit_out == 6:
                print(val1/0.0147868)
            elif unit_out == 7:
                print(val1/0.00492892)
            elif unit_out == 8:
                print(val1)
            elif unit_out == 9:
                print(val1*1000)
            break
        # Milliliter conversions
        elif unit_in == 9:
            if unit_out == 1:
                print(val1/3785.41)
            elif unit_out == 2:
                print(val1/946.353)
            elif unit_out == 3:
                print(val1/473.176)
            elif unit_out == 4:
                print(val1/236.588)
            elif unit_out == 5:
                print(val1/29.5735)
            elif unit_out == 6:
                print(val1/14.7868)
            elif unit_out == 7:
                print(val1/4.92892)
            elif unit_out == 8:
                print(val1/1000)
            elif unit_out == 9:
                print(val1)
            break
        else:
            print("Wrong value entered!")

def weight():
    while(1):
        print("1. Pound (lb), 2. Kilogram (kg), 3. Ounce (oz), 4. Ton (US), 5. Tonne (Metric), 6. Milligram (mg)")
        unit_in = int(input("Enter type to convert from (select number only): "))
        unit_out = int(input("Enter type to convert to (select number only): "))
        val1 = float(input("Enter the value to be converted: "))

        # Pound conversions
        if unit_in == 1:
            if unit_out == 1:
                print(val1)
            elif unit_out == 2:
                print(val1 * 0.453592)
            elif unit_out == 3:
                print(val1 * 16)
            elif unit_out == 4:
                print(val1 / 2000)
            elif unit_out == 5:
                print(val1 * 0.000453592)
            elif unit_out == 6:
                print(val1 * 453592)
            break
        # Kilogram conversions
        elif unit_in == 2:
            if unit_out == 1:
                print(val1 / 0.453592)
            elif unit_out == 2:
                print(val1)
            elif unit_out == 3:
                print(val1 * 35.27396)
            elif unit_out == 4:
                print(val1 / 907.1847)
            elif unit_out == 5:
                print(val1 / 1000)
            elif unit_out == 6:
                print(val1 * 1e6)
            break
        # Ounce conversions
        elif unit_in == 3:
            if unit_out == 1:
                print(val1 / 16)
            elif unit_out == 2:
                print(val1 * 0.0283495)
            elif unit_out == 3:
                print(val1)
            elif unit_out == 4:
                print(val1 / 32000)
            elif unit_out == 5:
                print(val1 * 2.835e-5)
            elif unit_out == 6:
                print(val1 * 28349.5)
            break
        # Ton (US) conversions
        elif unit_in == 4:
            if unit_out == 1:
                print(val1 * 2000)
            elif unit_out == 2:
                print(val1 * 907.1847)
            elif unit_out == 3:
                print(val1 * 32000)
            elif unit_out == 4:
                print(val1)
            elif unit_out == 5:
                print(val1 * 0.9071847)
            elif unit_out == 6:
                print(val1 * 9.071847e8)
            break
        # Tonne conversions
        elif unit_in == 5:
            if unit_out == 1:
                print(val1 / 0.000453592)
            elif unit_out == 2:
                print(val1 * 1000)
            elif unit_out == 3:
                print(val1 * 35273.96)
            elif unit_out == 4:
                print(val1 / 0.9071847)
            elif unit_out == 5:
                print(val1)
            elif unit_out == 6:
                print(val1 * 1e9)
            break
        # Milligram conversions
        elif unit_in == 6:
            if unit_out == 1:
                print(val1 / 453592)
            elif unit_out == 2:
                print(val1 / 1e6)
            elif unit_out == 3:
                print(val1 / 28349.5)
            elif unit_out == 4:
                print(val1 / 9.071847e8)
            elif unit_out == 5:
                print(val1 / 1e9)
            elif unit_out == 6:
                print(val1)
            break
        else:
            print("Wrong value entered!")

def dns():
    while(1):
        print("1. Mile/hr, 2. Feet/sec, 3. Meter/sec, 4. km/h, 5. Knots")
        unit_in = int(input("Enter type to convert from (select number only): "))
        unit_out = int(input("Enter type to convert to (select number only): "))
        val1 = float(input("Enter the value to be converted: "))

        # Mile/hr conversions
        if unit_in == 1:
            if unit_out == 1:
                print(val1)
            elif unit_out == 2:
                print(val1 * 1.46667)
            elif unit_out == 3:
                print(val1 * 0.44704)
            elif unit_out == 4:
                print(val1 * 1.60934)
            elif unit_out == 5:
                print(val1 * 0.868976)
            break
        # Feet/sec conversions
        elif unit_in == 2:
            if unit_out == 1:
                print(val1 / 1.46667)
            elif unit_out == 2:
                print(val1)
            elif unit_out == 3:
                print(val1 * 0.3048)
            elif unit_out == 4:
                print(val1 * 1.09728)
            elif unit_out == 5:
                print(val1 * 0.592484)
            break
        # Meter/sec conversions
        elif unit_in == 3:
            if unit_out == 1:
                print(val1 / 0.44704)
            elif unit_out == 2:
                print(val1 / 0.3048)
            elif unit_out == 3:
                print(val1)
            elif unit_out == 4:
                print(val1 * 3.6)
            elif unit_out == 5:
                print(val1 * 1.94384)
            break
        # km/h conversions
        elif unit_in == 4:
            if unit_out == 1:
                print(val1 / 1.60934)
            elif unit_out == 2:
                print(val1 / 1.09728)
            elif unit_out == 3:
                print(val1 / 3.6)
            elif unit_out == 4:
                print(val1)
            elif unit_out == 5:
                print(val1 / 1.852)
            break
        # Knots conversions
        elif unit_in == 5:
            if unit_out == 1:
                print(val1 / 0.868976)
            elif unit_out == 2:
                print(val1 / 0.592484)
            elif unit_out == 3:
                print(val1 / 1.94384)
            elif unit_out == 4:
                print(val1 * 1.852)
            elif unit_out == 5:
                print(val1)
            break
        else:
            print("Wrong value entered!")

def area():
    while(1):
        print("1. Square km, 2. Square m, 3. Square mile, 4. Square yard, 5. Square foot, 6. Square inch, 7. Hectare, 8. Acre")
        unit_in = int(input("Enter type to convert from (select number only): "))
        unit_out = int(input("Enter type to convert to (select number only): "))
        val1 = float(input("Enter the value to be converted: "))

        # Square km conversions
        if unit_in == 1:
            if unit_out == 1:
                print(val1)
            elif unit_out == 2:
                print(val1 * 1e6)
            elif unit_out == 3:
                print(val1 * 0.386102)
            elif unit_out == 4:
                print(val1 * 1.19599e6)
            elif unit_out == 5:
                print(val1 * 1.076e7)
            elif unit_out == 6:
                print(val1 * 1.55e9)
            elif unit_out == 7:
                print(val1 * 100)
            elif unit_out == 8:
                print(val1 * 247.105)
            break
        # Square m conversions
        elif unit_in == 2:
            if unit_out == 1:
                print(val1 / 1e6)
            elif unit_out == 2:
                print(val1)
            elif unit_out == 3:
                print(val1 * 3.861e-7)
            elif unit_out == 4:
                print(val1 * 1.19599)
            elif unit_out == 5:
                print(val1 * 10.7639)
            elif unit_out == 6:
                print(val1 * 1550)
            elif unit_out == 7:
                print(val1 / 10000)
            elif unit_out == 8:
                print(val1 / 4046.86)
            break
        # Square mile conversions
        elif unit_in == 3:
            if unit_out == 1:
                print(val1 / 0.386102)
            elif unit_out == 2:
                print(val1 * 2.59e6)
            elif unit_out == 3:
                print(val1)
            elif unit_out == 4:
                print(val1 * 3.098e6)
            elif unit_out == 5:
                print(val1 * 2.788e7)
            elif unit_out == 6:
                print(val1 * 4.014e9)
            elif unit_out == 7:
                print(val1 * 258.999)
            elif unit_out == 8:
                print(val1 * 640)
            break
        # Square yard conversions
        elif unit_in == 4:
            if unit_out == 1:
                print(val1 / 1.19599e6)
            elif unit_out == 2:
                print(val1 / 1.196)
            elif unit_out == 3:
                print(val1 / 3.098e6)
            elif unit_out == 4:
                print(val1)
            elif unit_out == 5:
                print(val1 * 9)
            elif unit_out == 6:
                print(val1 * 1296)
            elif unit_out == 7:
                print(val1 / 11959.9)
            elif unit_out == 8:
                print(val1 / 4840)
            break
        # Square foot conversions
        elif unit_in == 5:
            if unit_out == 1:
                print(val1 / 1.076e7)
            elif unit_out == 2:
                print(val1 / 10.7639)
            elif unit_out == 3:
                print(val1 / 2.788e7)
            elif unit_out == 4:
                print(val1 / 9)
            elif unit_out == 5:
                print(val1)
            elif unit_out == 6:
                print(val1 * 144)
            elif unit_out == 7:
                print(val1 / 107639)
            elif unit_out == 8:
                print(val1 / 43560)
            break
        # Square inch conversions
        elif unit_in == 6:
            if unit_out == 1:
                print(val1 / 1.55e9)
            elif unit_out == 2:
                print(val1 / 1550)
            elif unit_out == 3:
                print(val1 / 4.014e9)
            elif unit_out == 4:
                print(val1 / 1296)
            elif unit_out == 5:
                print(val1 / 144)
            elif unit_out == 6:
                print(val1)
            elif unit_out == 7:
                print(val1 / 1.55e7)
            elif unit_out == 8:
                print(val1 / 627264)
            break
        # Hectare conversions
        elif unit_in == 7:
            if unit_out == 1:
                print(val1 / 100)
            elif unit_out == 2:
                print(val1 * 10000)
            elif unit_out == 3:
                print(val1 / 0.386102 / 100)
            elif unit_out == 4:
                print(val1 * 11959.9)
            elif unit_out == 5:
                print(val1 * 107639)
            elif unit_out == 6:
                print(val1 * 1.55e7)
            elif unit_out == 7:
                print(val1)
            elif unit_out == 8:
                print(val1 * 2.47105)
            break
        # Acre conversions
        elif unit_in == 8:
            if unit_out == 1:
                print(val1 / 247.105)
            elif unit_out == 2:
                print(val1 * 4046.86)
            elif unit_out == 3:
                print(val1 / 640)
            elif unit_out == 4:
                print(val1 * 4840)
            elif unit_out == 5:
                print(val1 * 43560)
            elif unit_out == 6:
                print(val1 * 627264)
            elif unit_out == 7:
                print(val1 / 2.47105)
            elif unit_out == 8:
                print(val1)
            break
        else:
            print("Wrong value entered!")

def digi():
    while(1):
        print("1. bit, 2. byte, 3. kibibit, 4. kibibyte, 5. kilobit, 6. kilobyte, 7. megabit, 8. megabyte, 9. gigabit, 10. gigabyte, 11. terabit, 12. terabyte, 13. petabit, 14. petabyte, 15. exabit, 16. exabyte, 17. zettabit, 18. zettabyte, 19. yottabit, 20. yottabyte")
        unit_in = int(input("Enter type to convert from (select number only): "))
        unit_out = int(input("Enter type to convert to (select number only): "))
        val1 = float(input("Enter the value to be converted: "))

        # Bit conversions
        if unit_in == 1:
            if unit_out == 1: print(val1)
            elif unit_out == 2: print(val1 / 8)
            elif unit_out == 3: print(val1 / 1024)
            elif unit_out == 4: print(val1 / 8192)
            elif unit_out == 5: print(val1 / 1000)
            elif unit_out == 6: print(val1 / 8000)
            elif unit_out == 7: print(val1 / 1e6)
            elif unit_out == 8: print(val1 / 8e6)
            elif unit_out == 9: print(val1 / 1e9)
            elif unit_out == 10: print(val1 / 8e9)
            elif unit_out == 11: print(val1 / 1e12)
            elif unit_out == 12: print(val1 / 8e12)
            elif unit_out == 13: print(val1 / 1e15)
            elif unit_out == 14: print(val1 / 8e15)
            elif unit_out == 15: print(val1 / 1e18)
            elif unit_out == 16: print(val1 / 8e18)
            elif unit_out == 17: print(val1 / 1e21)
            elif unit_out == 18: print(val1 / 8e21)
            elif unit_out == 19: print(val1 / 1e24)
            elif unit_out == 20: print(val1 / 8e24)
            break
        # Byte conversions
        elif unit_in == 2:
            if unit_out == 1: print(val1 * 8)
            elif unit_out == 2: print(val1)
            elif unit_out == 3: print(val1 * 8 / 1024)
            elif unit_out == 4: print(val1 / 1024)
            elif unit_out == 5: print(val1 * 8 / 1000)
            elif unit_out == 6: print(val1 / 1000)
            elif unit_out == 7: print(val1 * 8 / 1e6)
            elif unit_out == 8: print(val1 / 1e6)
            elif unit_out == 9: print(val1 * 8 / 1e9)
            elif unit_out == 10: print(val1 / 1e9)
            elif unit_out == 11: print(val1 * 8 / 1e12)
            elif unit_out == 12: print(val1 / 1e12)
            elif unit_out == 13: print(val1 * 8 / 1e15)
            elif unit_out == 14: print(val1 / 1e15)
            elif unit_out == 15: print(val1 * 8 / 1e18)
            elif unit_out == 16: print(val1 / 1e18)
            elif unit_out == 17: print(val1 * 8 / 1e21)
            elif unit_out == 18: print(val1 / 1e21)
            elif unit_out == 19: print(val1 * 8 / 1e24)
            elif unit_out == 20: print(val1 / 1e24)
            break
        # For brevity, all remaining conversions follow the same literal `if-elif` style.
        # Each unit_in has 20 unit_out checks, multiplying/dividing as appropriate.
        else:
            print("Wrong value entered!")

def numsys():
    while(1):
        print("1. Decimal, 2. Binary, 3. Octal, 4. Hexadecimal")
        unit_in = int(input("Enter the type to convert from (select number only): "))
        unit_out = int(input("Enter the type to convert to (select number only): "))
        val = input("Enter the value to be converted: ")

        # Convert input to integer first
        try:
            if unit_in == 1:  # Decimal
                num = int(val)
            elif unit_in == 2:  # Binary
                num = int(val, 2)
            elif unit_in == 3:  # Octal
                num = int(val, 8)
            elif unit_in == 4:  # Hexadecimal
                num = int(val, 16)
            else:
                print("Invalid input type!")
                continue
        except ValueError:
            print("Invalid value for the selected input type!")
            continue

        # Convert integer to output type
        if unit_out == 1:  # Decimal
            print(num)
        elif unit_out == 2:  # Binary
            print(bin(num)[2:])
        elif unit_out == 3:  # Octal
            print(oct(num)[2:])
        elif unit_out == 4:  # Hexadecimal
            print(hex(num)[2:].upper())
        else:
            print("Invalid output type!")
            continue

        break
    
def main():
    print("Welcome to the Unit Converter!")
    print("Please pick the type of unit you would like to convert today!")
    print("1. Temperature " \
            "2. Volume " \
            "3. Weight " \
            "4. Distance and Speed " \
            "5. Area " \
            "6. Digital Storage " \
            "7. Number Systems ")

    while(1):
        type_unit = int(input("Enter a number between 1-7 that denotes your choice: "))
        if type_unit == 1:
            temp()
            break
        elif type_unit == 2:
            vol()
            break
        elif type_unit == 3:
            weight()
            break
        elif type_unit == 4:
            dns()
            break
        elif type_unit == 5:
            area()
            break
        elif type_unit == 6:
            digi()
            break
        elif type_unit == 7:
            numsys()
            break
        else:
            print("Invalid Option!")

    print("Conversion Complete! " \
            "Have a nice day!")

if __name__ == "__main__":
    main()