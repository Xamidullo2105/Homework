from datetime import datetime
from auth import get_active_user
from file_manager import write, read
from utils import generate_id


def start_working():

    start_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    current_time = datetime.now()
    
    difference = current_time - start_time
    minutes_passed = difference.total_seconds() // 60
    
    if minutes_passed > 0:
        fine = int(minutes_passed) * 1000
        new_id = generate_id(filename="penalties.csv")
        user_id = get_active_user()[0]
        new_penalty = [new_id, user_id, fine, current_time]
        write(filename="penalties.csv", data=new_penalty, mode="a")
        print(f"Penalty: {int(minutes_passed)}minutes * 1000 soum = {fine} soum")    
    else:
        print("Invalid time")


def show_employee_penalties():
    user_id = get_active_user()[0]
    penalties = read(filename="penalties.csv")
    user_penalties = []
    for penalty in penalties:
        if penalty[1] == user_id:
            user_penalties.append(penalty)
    
    print_penalties(penalties=user_penalties)



def print_penalties(penalties: list):
    total_penalty = 0
    massage = "All of your penalties: \n\n"
    for penalty in penalties:
        total_penalty += int(penalty[2])
        massage += f"ID: {penalty[0]}, Amount: {penalty[2]} soum Date: {penalty[3]}\n"
    massage += f"Total penalties: {total_penalty} soum"
    print(massage)
