# ----------------------------------------
# CodSoft Python Internship
# Task 3 - Password Generator
# ----------------------------------------

import random
import string

print("========== PASSWORD GENERATOR ==========")

# Get password length from user
length = int(input("Enter the desired password length: "))

# Characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("\nGenerated Password:")
print(password)