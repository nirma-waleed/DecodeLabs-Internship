import secrets
import string


def generate_password(length):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    character_pool = lowercase + uppercase + digits + symbols

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    for _ in range(length - 4):
        password.append(secrets.choice(character_pool))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():

    print("=" * 50)
    print("        RANDOM PASSWORD GENERATOR")
    print("=" * 50)

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("\nInvalid input! Password length must be at least 8 characters.\n")
                continue

            password = generate_password(length)

            print(f"\nGenerated Secure Password: {password}")

            print("\nPassword generated successfully!\n")
            break

        except ValueError:
            print("\nInvalid input! Please enter a valid number.\n")


if __name__ == "__main__":
    main()