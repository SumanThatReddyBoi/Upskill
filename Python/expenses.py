from datetime import datetime, date
import csv

class Expenses:
    def __init__(self, dated, desc, amt):
        self.dated = dated
        self.desc = desc
        self.amt = amt

class Tracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Ammount Spent"]) #csv wiped fully

    def Add(self, expense):
        self.expenses.append(expense)

        with open(self.filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([expense.dated, expense.desc, expense.amt]) #adds value

    def Remove(self, index):
        if 0 <= index and index < len(self.expenses):
            del self.expenses[index]
            print("Expense Successfully Deleted!")

            with open(self.filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Description", "Amount"]) #csv wiped fully
               
                for i in self.expenses:
                    writer.writerow([i.dated, i.desc, i.amt]) #reads fresh from the memory
        
        else:
            print("Invalid Index Value to Delete!")

    def View(self):
        if len(self.expenses) == 0:
            print("You have no expenses yet!")
        else: 
            print("Expenses List:")
            for i, expense in enumerate(self.expenses, start = 1):
                print(f"{i}. Date: {expense.dated} Description: {expense.desc} Ammount: ${expense.amt:.2f}")
    
    def Total(self):
        total=sum(expense.amt for expense in self.expenses)
        print(f"Total ammount spent: ${total:.2f}")


def main():
    expencetracker = Tracker()

    while(1):
        print("\nExpence Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        valOpt = input ("Select an option (1-5) to proceed: ")
        print("")
        if valOpt == "1":
            #dated = date.today()                               #for today's date (needs import header - incl.)
            dated = input("Enter date (DD-MM-YYYY): ")
            desc = input("Enter Your Description: ")
            amt = float(input("Ammout Spent: $"))
            expense = Expenses(dated, desc, amt)
            expencetracker.Add(expense)
            print("Expense added Successfully!")
        elif valOpt == "2":
            indexVal = int(input("Enter your index value to remove exepnses: "))
            expencetracker.Remove(indexVal-1)
        elif valOpt == "3":
            expencetracker.View()
        elif valOpt == "4":
            expencetracker.Total()
        elif valOpt == "5":
            print("Thank you for using Exepnse Tracker!")
            print("Have a nice day! \nGoodbye!")
            break
        else:
            print("Invalid Option! \n Please Try Again!")

if __name__ == "__main__":
    main()