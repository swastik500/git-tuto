#edited by sojwal000
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for password length
length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)
