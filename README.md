# 🔒 Ransomware Simulation Attack

![Warning](https://img.shields.io/badge/Security-Awareness-red?style=for-the-badge\&logo=hackaday)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Linux](https://img.shields.io/badge/Linux-Compatible-yellow?style=for-the-badge\&logo=linux)
![Educational](https://img.shields.io/badge/Use-Educational-green?style=for-the-badge\&logo=bookstack)

---

## ⚠️ Disclaimer

This attack is created **strictly for educational and awareness purposes only**. It simulates the behavior of a ransomware attack to demonstrate the **risks of downloading software from untrusted or pirated sources**. Do **NOT** misuse this attack for malicious purposes. The author is not responsible for any damages caused by misuse.

---

## 📝 Overview

This repository simulates a basic ransomware attack:

* **encrypt.py** → Encrypts files in the current directory and sends the encryption key to the attacker machine.
* **decrypt.py** → Decrypts the encrypted files using the key retrieved from the attacker.
* **receive\_key.py** → Simple HTTP server running on the attacker machine that receives and stores the encryption key.

The goal is to **educate employees or students** about the dangers of unsafe downloads and the importance of security awareness.

---

## ⚙️ How It Works

1. The **attacker machine** must run the key receiver first to receive and store the encryption key.
2. The **encryptor** script encrypts all files in the working directory (except the scripts themselves) and sends the key to the attacker.
3. The **decryptor** script restores the files using the saved key.

---

## 🚀 Setup & Execution

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ransomware-simulation.git
cd ransomware-simulation
```

### 2. Run the Key Receiver (on attacker machine)

On the **attacker machine** (Linux recommended), run:

```bash
python3 receive_key.py
```

This will start listening on port **8080** by default.

### 3. Configure Encryptor (on victim machine)

Edit **encrypt.py** and replace:

```python
SERVER_URL = "http://your ip:8080/upload"
```

with the IP address of the **attacker machine** running `receive_key.py`.

Example:

```python
SERVER_URL = "http://192.168.1.100:8080/upload"
```

### 4. Run Encryptor (on victim machine)

On the **victim simulation machine**, run:

```bash
python3 encrypt.py
```

All files in the directory will now be encrypted.

### 5. Run Decryptor (on victim machine)

Once the key has been retrieved by the attacker, place the file `received_key.key` into the victim’s directory and run:

```bash
python3 decrypt.py
```

This will restore all encrypted files.

---

## 📌 Notes

* This is a **controlled simulation** only. Do not use on sensitive or personal data.
* Best used in a **virtual machine environment** for demonstrations.
* Teaches employees how **real ransomware** can lock files and why **safe downloading habits** are essential.

---

![Awareness](https://img.shields.io/badge/Cybersecurity-Awareness-orange?style=for-the-badge\&logo=shield)
