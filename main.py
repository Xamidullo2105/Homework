from auth import logout, login
from admin import add_employee
from employee import show_employee_penalties, start_working
from admin import show_all_penalties

def auth_menu():
    print("""
    1.Login
    2.Exit
    """)
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            result = login()
            if result == "admin":
                return admin_menu()
            elif result == "user":
                return employee_menu()
            else:
                return auth_menu()
        elif choice == "2":
            return print("Good bye")
        else:
            print("Invalid choice")
    except KeyboardInterrupt:
        print("Good bye")
        
def admin_menu():
    print("""
    1.Show all employees
    2.Add new employee
    3.Show all penalties
    4.Delete employee
    5.Delete penalty
    6.Logout
    """)
    
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            pass
        elif choice == "2":
            add_employee()
        elif choice == "3":
            show_all_penalties()
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            return auth_menu()
        else:
            print("Invalid choice")
        return admin_menu()
    except KeyboardInterrupt:
        print("Good bye")


def employee_menu():
    print("""
    1.Start work
    3.Show all my penalties
    3.Logout
    """)
    
    try:
        choice = input("Enter your choice: ")
        if choice == "1":
            start_working()
        elif choice == "2":
            show_employee_penalties()
        elif choice == "3":
            logout()
            return auth_menu()
        else:
            print("Invalid choice")
        return employee_menu()
    except KeyboardInterrupt:
        print("Good bye")


if __name__ == "__main__":
    logout()
    auth_menu()