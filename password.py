import random 
import string

def generate_password(password_length, numbers, special_character):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        character += digits
    if special_character:
        character += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < password_length:
        values = random.choice(character)
        pwd += values

        if values in digits:
            has_number = True
        elif values in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria_number = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special

    return pwd


password_length = int(input("Password length: "))
number_required = input("Do you want a number in password? (y / n): ").lower() == 'y'
special_required = input("Do you want a special characters in password? (y / n): ").lower() == 'y'

password = generate_password(5, number_required, special_required)
print(password)