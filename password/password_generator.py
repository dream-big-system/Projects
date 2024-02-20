import random
import string

def generate_password(length=12):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the length of the password
    length = int(input("Enter the length of the password: "))

    # Generate the password
    password = generate_password(length)
    
    # Print the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
