import random
import string

def generate_password(length=12, include_special_chars=True):
    """Generates a random password with the specified length."""
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the password length: ").strip())
        include_special_chars = input("Include special characters (yes/no)? ").strip().lower() == 'yes'

        password = generate_password(length, include_special_chars)
        print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
