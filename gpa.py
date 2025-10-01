def perToLetter(x):
    if x >= 97:
        print("A+")
    elif x < 97 and x >= 93:
        print("A")
    elif x < 93 and x >= 90:
        print("A-")
    elif x < 90 and x >= 87:
        print("B+")
    elif x < 87 and x >= 83:
        print("B")
    elif x < 83 and x >= 80:
        print("B-")
    elif x < 80 and x >= 77:
        print("C+")
    elif x < 77 and x >= 73:
        print("C")
    elif x < 73 and x >= 70:
        print("C-")
    elif x < 70 and x >= 67:
        print("D+")
    elif x < 67 and x >= 65:
        print("D")
    elif x < 65:
        print("F")
    else:
        print("Error in Generating Percentage!")

def printable(a):
    ten = a/10 #ten scale
    five = (a/20) #five scale
    hons = ((a/100)*4.5)
    four = ((a/100)*4)
    print(perToLetter(a))
    print("Four Scale (4.0): ", four)
    print("Honours Scale (4.5): ", hons)
    print("Five Scale (5.0): ", five)
    print("Ten Scale (10.0): ", ten)
    print()
    print("Thank you for using GPA Converter!")

def main():      
    print("Welcome to the GPA Converter")

    while(1):
        print("\nWhich form of GPA do you currently have?")
        print("A. Percent")
        print("B. Letter Grade")
        print("C. 4-Scale")
        print("D. 4.5-Scale (Hons.)")
        print("E. 5-Scale")
        print("F. 10-Scale")
        print("\nNote: If you enter 'B' for Letter Grade, we can only return a percentage range!")

        gpa_in = input("Enter the letter corresponding to your choice: ").strip().upper()
        
        if gpa_in == 'A':
            user_in = int(input("Enter your percent: ")).strip()
            printable(user_in)
            break

        elif gpa_in == 'B':
            user_in = input("Enter your letter grade: ").strip()
            if user_in == 'A+':
                print("Percentage Range: 97-100")
                break
            elif user_in == 'A':
                print("Percentage Range: 93-96")
                break
            elif user_in == 'A-':
                print("Percentage Range: 90-92")
                break
            elif user_in == 'B+':
                print("Percentage Range: 87-89")
                break
            elif user_in == 'B':
                print("Percentage Range: 83-86")
                break
            elif user_in == 'B-':
                print("Percentage Range: 80-82")
                break
            elif user_in == 'C+':
                print("Percentage Range: 77-79")
                break
            elif user_in == 'C':
                print("Percentage Range: 73-76")
                break
            elif user_in == 'C-':
                print("Percentage Range: 70-72")
                break
            elif user_in == 'D+':
                print("Percentage Range: 67-69")
                break
            elif user_in == 'D':
                print("Percentage Range: 65-66")
                break
            elif user_in == 'F':
                print("Percentage Range: Below 65")
                break
            else:
                print("Invalid Grade Entered! Try again.")

        elif gpa_in == 'C':
            user_in = float(input("Enter your gpa: "))
            c = ((user_in/4)*100)
            printable(c)
            break

        elif gpa_in == 'D':
            user_in = float(input("Enter your gpa: "))
            d = ((user_in/4.5)*100)
            printable(d)
            break

        elif gpa_in == 'E':
            user_in = float(input("Enter your gpa: "))
            e = (((user_in)/5)*100)
            printable(e)
            break

        elif gpa_in == 'F':
            user_in = float(input("Enter your gpa: "))
            f = ((user_in/10)*100)
            printable(f)
            break

        else:
            print("Invalid Input, Please Try Again!")

if __name__ == "__main__":
    main()