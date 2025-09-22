
import re  
from datetime import datetime 

def is_valid_email(email: str) -> bool:
    #Valido el email
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def is_valid_dni(dni: str) -> bool:
    #Valido DNI
    return dni.isdigit() and len(dni) in [7, 8]

def is_valid_name(name: str) -> bool:
    #Valido el nombre, pero tambien le doy un formato universal
    cleaned_name = name.replace(" ", "") 
    return cleaned_name.isalpha() and len(cleaned_name) >= 2 

def is_valid_birthdate(date_str: str) -> bool:
    #Valido la fecha de nacimiento y le doy un formato universal
    try:
        birthdate = datetime.strptime(date_str, "%Y-%m-%d")
        return birthdate < datetime.now()
    except ValueError:
        return False