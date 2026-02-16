import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password   # ← MUST be indented

try:
    length = int(input("Enter password length: "))
    if length < 6:
        print("Password length should be at least 6 characters.")
    else:
        pwd = generate_password(length)
        print("Generated Password:", pwd)
except ValueError:
    print("Please enter a valid number.")