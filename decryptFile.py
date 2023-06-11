#1) Read the key from file
key = ''
with open('myTopSecretKey.key', 'rb') as file:
    key = file.read()

#2) Read the encrypted data from file
encryptedData = ''
with open('myTopSecretInfo.txt', 'rb') as file:
    encryptedData = file.read()

#3) Encrypt Data
from cryptography.fernet import Fernet

f = Fernet(key)

decryptedData = f.decrypt(encryptedData)

print('Encrypted data:', encryptedData.decode())

print('Dencrypted data:', decryptedData.decode())