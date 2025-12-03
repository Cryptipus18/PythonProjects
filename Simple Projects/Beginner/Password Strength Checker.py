def check_password():
    password = input("Enter your password: ")
    strength = 0


    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

    if any(c.isupper() for c in password):
        strength += 1

    if any(c.islower() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

  
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(c in special_characters for c in password):
        strength += 1

    
    if strength <= 2:
        print("Password Strength: Weak")
    elif strength <= 4:
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Strong")


check_password()        