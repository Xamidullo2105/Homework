import hashlib
from file_manager import read

def generate_id(filename: str) -> int:
    data = read(filename=filename)
    try:
        return int(data[-1][0]) + 1 if data else 1
    except (IndexError, ValueError):
        return 1
    

def hash_password(password: str):
    return hashlib.sha256(string=password.encode()).hexdigest()