import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not any([use_letters, use_numbers, use_symbols]):
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_manually():
    print("Generate your password!")
    password = input("Enter your password: ")
    return password

def main():
    print("Welcome to the Password Generator!")
    manual_gen = input("Do you want to generate your password? (yes/no): ").lower() == 'yes'

    if manual_gen:
        password = generate_password_manually()
        print(f"Your password: {password}")
    else:
        length = int(input("Enter the length of the password: "))
        use_letters = input("Include letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            print(f"Generated Password: {password}")
        else:
            print("Password generation failed. Please try again.")

if __name__ == "__main__":
    main()

