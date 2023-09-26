import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid positive length.")
            return

        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Please enter a valid numeric length.")

if __name__ == "__main__":
    main()
