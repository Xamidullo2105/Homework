from datetime import datetime
from file_manager import read


def start_working():

    users = read("users.csv")
    for user in users:
        print(user,"\n\n")
    hozir = datetime.now()
    text = "09:30"
    
    boshqa_soat = 14
    boshqa_daqiqa = 30

    boshqa_vaqt = hozir.replace(hour=boshqa_soat, minute=boshqa_daqiqa, second=0, microsecond=0)

    farq = hozir - boshqa_vaqt

    farq_minutlarda = farq.total_seconds() / 60
    print(f"Soatlar orasidagi farq: {farq_minutlarda:.2f} minut")



start_working()
