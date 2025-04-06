from utils import hash_password, generate_id
from file_manager import write, read
from employee import print_penalties

def add_employee():
    full_name = input("Enter your name: ")
    phone_number = input("Enter phone number: ")
    start_time = input("Enter employee working start time: ")
    password1 = input("Enter password: ")
    password2 = input("Confirm password: ")
    
    while password1 != password2:
        password1 = input("Enter password: ")
        password2 = input|("Confirm password: ")
        
    hashed_password = hash_password(password=password1)
    new_id = generate_id(filename="users.csv")
    user = [new_id, full_name, phone_number, hashed_password, start_time, 0]
    write(filename="users.csv", data=user, mode="a")
    print("Employee is added")


def show_all_penalties():
    penalties = read(filename="penalties.csv")
    print_penalties(penalties=penalties)
    