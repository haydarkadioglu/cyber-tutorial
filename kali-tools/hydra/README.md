# 🔥 Hydra - Fast and Flexible Password Cracking Tool  

Hydra is a **powerful and fast password brute-forcing tool** 🔓 used to perform automated attacks against **various network services and protocols**. It is widely used by **penetration testers, ethical hackers, and cybersecurity researchers** 🕵️‍♂️💻.  

🚨 **Warning:** Unauthorized usage of Hydra is illegal! Only use it on systems you have permission to test. 🚨  

---

## 📌 Features of Hydra  

✅ **Fast and efficient** brute-force attack tool.  
✅ **Supports parallel attacks** using multiple threads.  
✅ **Can test multiple login credentials** automatically.  
✅ **Works on various protocols and services** (SSH, FTP, HTTP, RDP, MySQL, etc.).  
✅ **Supports dictionary attacks, hybrid attacks, and more**.  

---

## 🚀 Installation  

### 🐧 Linux (Kali & Debian-based)  
```bash
sudo apt install hydra
```

### 🍏 macOS (Homebrew)  
```bash
brew install hydra
```

### 🖥️ Windows  
Hydra is primarily designed for **Linux**, but it can run on Windows using **Cygwin** or **WSL (Windows Subsystem for Linux)**.  

---

## 🛠️ Basic Command Structure  

```bash
hydra [OPTIONS] -l <username> -P <password_list> <protocol>://<target>
```

### 🔑 Commonly Used Options  

| Option | Description |
|--------|-------------|
| `-l <username>` | Single username |
| `-L <user_list>` | List of usernames |
| `-p <password>` | Single password |
| `-P <password_list>` | List of passwords |
| `-t <threads>` | Number of parallel attack threads (default: 16) |
| `-V` | Show each attempt in real time |
| `-f` | Stop after the first successful attempt |
| `-vV` | Show detailed output |
| `-o <file>` | Save results to a file |
| `-I` | Ignore failure messages |
| `-s <port>` | Specify a custom port |

---

## 🌐 Supported Protocols  

Hydra supports a **wide range of protocols**, including:  

- **🔐 SSH (Secure Shell)**
- **📡 FTP (File Transfer Protocol)**
- **🌍 HTTP / HTTPS (Web Authentication)**
- **💾 SMB (Windows File Sharing)**
- **🎮 RDP (Remote Desktop Protocol)**
- **🛢️ MySQL, PostgreSQL, MSSQL, Oracle (Databases)**
- **📧 SMTP, POP3, IMAP (Email Services)**
- **🖥️ VNC (Remote Desktop)**
- **🔍 LDAP (Directory Services)**
- **💬 Telnet (Old Remote Access Protocol)**  

To see the full list of supported services, run:  
```bash
hydra -h
```

---

## 🚀 Common Usage Examples  

### 🔐 1. SSH Brute-Force Attack  
```bash
hydra -l root -P passwords.txt ssh://192.168.1.100
```
✅ Tries multiple passwords from `passwords.txt` for the **root** user on **SSH**.  

---

### 🗂️ 2. SSH Attack with Username List  
```bash
hydra -L users.txt -P passwords.txt ssh://192.168.1.100
```
✅ Tests multiple usernames from `users.txt` against multiple passwords from `passwords.txt`.  

---

### 🌍 3. HTTP Form-Based Login Attack  
```bash
hydra -l admin -P passwords.txt 192.168.1.100 http-post-form "/login.php:user=^USER^&pass=^PASS^:F=Incorrect"
```
✅ Hydra replaces `^USER^` and `^PASS^` with credentials from the lists.  
✅ The attack stops when it detects "Incorrect" in the response.  

---

### 🎯 4. FTP Brute-Force Attack  
```bash
hydra -L users.txt -P passwords.txt ftp://192.168.1.100
```
✅ Tests FTP login using **multiple usernames and passwords**.  

---

### 🖥️ 5. RDP (Windows Remote Desktop) Attack  
```bash
hydra -l administrator -P passwords.txt rdp://192.168.1.100
```
✅ Attempts to brute-force **Windows RDP** login.  

---

### 💾 6. MySQL Database Attack  
```bash
hydra -L users.txt -P passwords.txt mysql://192.168.1.100
```
✅ Tests login credentials on a **MySQL database**.  

---

### 📨 7. SMTP Email Server Attack  
```bash
hydra -l admin@example.com -P passwords.txt smtp://192.168.1.100 -V
```
✅ Attempts to log in to an **SMTP email server** with a known email account.  

---

### 📡 8. Brute-Force Attack on SMB (Windows File Sharing)  
```bash
hydra -L users.txt -P passwords.txt smb://192.168.1.100
```
✅ Tests login credentials for **Windows SMB file sharing**.  

---

### 🔀 9. Parallel Attack with 50 Threads  
```bash
hydra -L users.txt -P passwords.txt -t 50 ssh://192.168.1.100
```
✅ Increases attack speed by **using 50 concurrent threads**.  

---

### 📝 10. Save Output to a File  
```bash
hydra -L users.txt -P passwords.txt ssh://192.168.1.100 -o results.txt
```
✅ Saves successful login attempts to `results.txt`.  

---

## 📌 Useful Hydra Tricks  

### 🔄 Resume a Previous Attack  
```bash
hydra -R
```
✅ If an attack is interrupted, **this command resumes it**.  

---

### 🚀 Maximize Speed  
```bash
hydra -L users.txt -P passwords.txt -t 64 ssh://192.168.1.100
```
✅ Uses **64 attack threads** for maximum speed.  

---

### 🚫 Stop After First Successful Attempt  
```bash
hydra -L users.txt -P passwords.txt ssh://192.168.1.100 -f
```
✅ Stops as soon as **one working password** is found.  

---

## ⚠️ Ethical Usage Warning  

🚨 **Hydra is a penetration testing tool and should only be used on systems you have permission to test. Unauthorized use is illegal and may result in severe consequences!** 🚨  

---

## 📜 Conclusion  

Hydra is one of the **fastest and most powerful password brute-forcing tools** 🔥. It is widely used by security professionals to **test authentication mechanisms**.  

📌 **For more details, visit the official GitHub repository:**  
[Hydra on GitHub](https://github.com/vanhauser-thc/thc-hydra)  

---

🚀 **Happy Hacking (Ethically)!** 😃🔥
