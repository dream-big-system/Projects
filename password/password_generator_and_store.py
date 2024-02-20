from cryptography.fernet import Fernet
import random
import string

# Function to generate a Fernet key
def generate_key():
    return Fernet.generate_key()

# Function to load the key from a file
def load_key():
    return open("key.key", "rb").read()

# Function to write the key to a file
def write_key(key):
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to encrypt a message
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Function to generate a password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to save the password to an encrypted file
def save_password(password):
    key = load_key()
    encrypted_password = encrypt_message(password, key)
    with open("passwords.txt", "ab") as file:
        file.write(encrypted_password + b'\n')

def main():
    # Prompt the user to specify the length of the password
    length = int(input("Enter the length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Save the password to the encrypted file
    save_password(password)

    # Print the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    # Generate and write the key if it doesn't exist
    try:
        key = load_key()
    except FileNotFoundError:
        key = generate_key()
        write_key(key)

    main()
