#This is Q4.py
def decrypt():
    with open('password.txt', 'r') as file:
        encrypted_password = file.read().strip()
        decrypted_password = encrypted_password.replace('&', '')

    return decrypted_password
