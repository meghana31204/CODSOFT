import random
import string

def generate_password(length):
    characters = string.ascii_letters  # Only alphabets (uppercase and lowercase)
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

main()
