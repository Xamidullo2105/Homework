import csv
import os

def read(filename: str) -> list:
    path = f"data/{filename}"
    if os.path.exists(path):
        with open(file=path, mode="r", encoding="UTF-8", newline="") as file:
            return list(csv.reader(file))  
    return []

def write(filename: str, data: list, mode: str = "w") -> None:
    path = f"data/{filename}"

    os.makedirs("data", exist_ok=True)  

    with open(file=path, mode=mode, encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)

        if mode == "w":
            writer.writerows(data) 
        else:
            writer.writerow(data) 
