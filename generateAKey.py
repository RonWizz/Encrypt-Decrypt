#0) pip install cryptography


#1) Generate a symmertic key
from cryptography.fernet import Fernet
key = Fernet.generate_key()


#2) Save the key in a file
with open('myTopSecretKey.key', 'wb') as file:
	file.write(key)