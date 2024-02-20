from cryptography.fernet import Fernet

# Function to load the key from a file
def load_key():
    return open("key.key", "rb").read()

# Function to decrypt a message
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

# Function to decrypt passwords from the encrypted file
def decrypt_passwords():
    key = load_key()
    with open("passwords.txt", "rb") as file:
        for line in file:
            decrypted_password = decrypt_message(line.strip(), key)
            print("Decrypted Password:", decrypted_password)

def main():
    decrypt_passwords()

if __name__ == "__main__":
    main()
