import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    hashed_password = hash_password(password_to_check)
    
    if email in stored_logins:
        return stored_logins[email] == hashed_password
    else:
        return False

def main():
    stored_logins = {
        "ammar@gmail.com": hash_password("ammar123"),
        "ayan@hotmail.com": hash_password("ayan1"),
    }

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == '__main__':
    main()
