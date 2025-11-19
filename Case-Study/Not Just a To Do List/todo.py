from notifier import alerter
from email_validator import validate_email, EmailNotValidError

todo = []
email = None

def info():
    global email, username
    while True:
        print("Would you like us to send your todo list to you over email (Y/N)?")
        choice = input().strip().upper()

        if choice == 'Y':
            email = input("Enter your email: ").strip()
            if email_validity(email):
                print("Email saved successfully.\n")
                while True:
                    gender = input("Please tell us your gender (Male/Female/Rather Not Say): ").strip().upper()
                    
                    if gender == 'MALE':
                        name = input("Please tell us your preferred name (for mailing only): ")
                        username = f"Mr. {name}"
                        break
                    
                    elif gender == 'FEMALE':
                        name = input("Please tell us your preferred name (for mailing only): ")
                        username = f"Ms. {name}"
                        break

                    elif gender == 'RATHER NOT SAY':
                        username = "You Anonymous User"
                        break
                    else:
                        print("Invalid choice. Please try again.\n")
                break
            else:
                print("Invalid email. Try again.\n")
        elif choice == 'N':
            print("Okay. You will not get your list emailed to you.\n")
            email = "NULL"
            break
        else:
            print("Enter a valid option! (Y or N)\n")


def email_validity(mail):
    try:
        validate_email(mail, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


def display_menu():
    print("\n======= To Do List Menu ==========")
    print("1. Add Item")
    print("2. Mark Task as Complete")
    print("3. Delete Task")
    print("4. Email My List")
    print("5. Exit \n")
    view()
    print("\n")


def add(task, desc):
    todo.append({"Task": task, "Description": desc, "Status": False})
    print(f"Task '{task}' was added successfully!")


def view(return_text=False):
    if not todo:
        print("Your list is empty.")
        return "Your list is empty." if return_text else None

    output = ["======= To Do List =========="]
    print("\n", output)
    for i, item in enumerate(todo):
        status = "✓" if item["Status"] else "✗"
        line = f"{i+1}. [{status}] {item['Task']} - {item['Description']}"
        print(line)
        output.append(line)
    if return_text:
        return "\n".join(output)


def done(index):
    if 0 <= index < len(todo):
        todo[index]["Status"] = True
        print(f"Task '{todo[index]['Task']}' was marked as complete.\n")
    else:
        print("Invalid Event Number")

def not_done(index):
    if 0 <= index < len(todo):
        todo[index]["Status"] = False
        print(f"Task '{todo[index]['Task']}' was marked as incomplete.\n")
    else:
        print("Invalid Event Number")


def remove(index):
    if 0 <= index < len(todo):
        removed_event = todo.pop(index)
        print(f"The item '{removed_event['Task']}' was removed successfully.")
    else:
        print("Invalid Event Number")


def main():
    info()
    global email

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            description = input("Enter the task description: ")
            add(task, description)

        elif choice == '2':
            try:
                task_num = int(input("Enter the task number to mark as complete: "))
                done(task_num - 1)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            try:
                task_num = int(input("Enter the task number to delete: "))
                remove(task_num - 1)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            if email == "NULL":
                print("You have opted out of email.")
            else:
                mail_body = view(return_text=True)
                mail_content = f"""
                Hello {username},
This is a message from Not Just A ToDo List. 

As per your request, we are sending you your to-do list. 
This email and any further emails will only be sent upon request.

{mail_body}

Thank you for choosing Not Just A ToDo List!
        """
                
                alerter(email, mail_content)
                print("Email sent successfully!")

        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
