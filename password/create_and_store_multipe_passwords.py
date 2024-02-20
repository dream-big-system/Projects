import json
from cryptography.fernet import Fernet

import json
import base64
from cryptography.fernet import Fernet

# Function to load keys from a file
def load_keys():
    try:
        with open("keys.json", "r") as file:
            content = file.read()
            if content.strip() == "":
                return {}
            keys = json.loads(content)
            # Decode base64 encoded keys
            keys = {key: base64.b64decode(value.encode()) for key, value in keys.items()}
    except FileNotFoundError:
        keys = {}
    return keys

# Function to write keys to a file
def write_keys(keys):
    # Encode keys as base64 before writing to JSON file
    encoded_keys = {key: value.decode() for key, value in keys.items()}
    with open("keys.json", "w") as file:
        json.dump(encoded_keys, file)

# Rest of the code remains the same...



# Function to generate a Fernet key
def generate_key():
    return Fernet.generate_key()

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
def save_password(password, key_name):
    keys = load_keys()
    key = keys.get(key_name)
    if key:
        encrypted_password = encrypt_message(password, key)
        with open("passwords.txt", "ab") as file:
            file.write(encrypted_password + b'\n')
    else:
        print("Key not found!")

def main():
    # Load existing keys or create an empty dictionary
    keys = load_keys()

    # Prompt the user to specify the name of the key
    key_name = input("Enter the name of the key: ")

    # Generate a new key if it doesn't exist
    if key_name not in keys:
        keys[key_name] = generate_key()
        write_keys(keys)

    # Prompt the user to specify the length of the password
    length = int(input("Enter the length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Save the password to the encrypted file using the specified key
    save_password(password, key_name)

    # Print the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
