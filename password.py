import random
import string

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + "@#$&"

password = ""

if length >= 8:
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
else:
    print("Password must contain at least 8 characters")