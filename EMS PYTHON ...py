# ------------------ EMPLOYEE MANAGEMENT SYSTEM ---------------------

# Dictionary to store employee information
employee_database = {}

# Function to Add Employee
def Add_Employee():
    Id = input("Enter Employee Id: ")
    if Id in employee_database:
        print("Employee already exists\nTry Again\n")
        menu()
    else:
        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")
        employee_database[Id] = {'Name': Name, 'Post': Post, 'Salary': Salary}
        print("Employee Added Successfully")
        menu()

# Function to Promote Employee
def Promote_Employee():
    Id = input("Enter Employee's Id: ")
    if Id not in employee_database:
        print("Employee does not exist\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary: "))
        employee_database[Id]['Salary'] = str(int(employee_database[Id]['Salary']) + Amount)
        print("Employee Promoted")
        menu()

# Function to Remove Employee
def Remove_Employee():
    Id = input("Enter Employee Id: ")
    if Id not in employee_database:
        print("Employee does not exist\nTry Again\n")
        menu()
    else:
        del employee_database[Id]
        print("Employee Removed")
        menu()

# Function to Display All Employees
def Display_Employees():
    if not employee_database:
        print("No employees to display")
    else:
        for Id, details in employee_database.items():
            print("Employee Id:", Id)
            print("Employee Name:", details['Name'])
            print("Employee Post:", details['Post'])
            print("Employee Salary:", details['Salary'])
            print("--------------------------")
    menu()

# Menu function
def menu():
    print("  ------------Welcome to Employee Management Record-------------")
    print(" ")
    print("Press:")
    print("1 to Add Employee")
    print("2 to Remove Employee")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Exit")
    choice = input("Enter your Choice: ")
    if choice == '1':
        Add_Employee()
    elif choice == '2':
        Remove_Employee()
    elif choice == '3':
        Promote_Employee()
    elif choice == '4':
        Display_Employees()
    elif choice == '5':
        print("Thank you for using the Employee Management System")
    else:
        print("Invalid Choice")
        menu()

# Branch menu function
def branchmenu():
    print(" ---------- SCHOOLS OF DIFFERENT BRANCHES------------")
    print(" ")
    print("Choice to choose school :")
    print("")
    print("1. School of Advanced Engineering ")
    print("2. School of Business ")
    print("3. School of Design ")
    print("4. School for Computer Science ")
    print("5. School of Law ")
    print("6. School for Life ")
    print("7. School of Liberal Studies ")
    print("8. School for Health Science and Technology")
    print("9. Exit")
    print("")
    choose = input("Enter the School Number:")
    
    if choose == '1':
        print("You have chosen School of Advanced Engineering")
        print(" ")
        menu()
    elif choose == '2':
        print("You have chosen School of Business")
        print(" ")
        menu()
    elif choose == '3':
        print("You have chosen School of Design")
        print(" ")
        menu()
    elif choose == '4':
        print("You have chosen School for Computer Science")
        print(" ")
        menu()
    elif choose == '5':
        print("You have chosen School of Law")
        print(" ")
        menu()
    elif choose == '6':
        print("You have chosen School for Life")
        print(" ")
        menu()
    elif choose == '7':
        print("You have chosenSchool of Liberal Studies")
        print(" ")
        menu()
    elif choose == '8':
        print("You have chosen School for Health Science and Technology")
        print(" ")
        menu()
    elif choose == '9':
        print("Thank you for using the Employee Management System")
    else:
        print("Invalid Choice")
        branchmenu()

# Calling branchmenu function
branchmenu()
