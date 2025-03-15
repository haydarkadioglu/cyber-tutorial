# 🚀 Burp Suite Guide  

Burp Suite is a **powerful penetration testing tool** 🛡️ used for security testing of web applications. It is developed by **PortSwigger** and is widely used by **web security professionals, ethical hackers, and security researchers**. 🕵️‍♂️💻  

## 🔥 Main Features  

- **🕵️ Proxy (Intercepting Proxy)** - Captures and modifies 🔄 HTTP/S traffic between the browser and the target server.  
- **🕸️ Spider (Web Crawler)** - Maps the target website 🌍 by discovering its links.  
- **🛑 Scanner (Security Scanner - Pro Version Only)** - Automatically scans web applications for vulnerabilities like **XSS, SQL Injection, CSRF**. 🛠️  
- **💥 Intruder (Brute Force & Testing Tool)** - Used for attacking different input points (password cracking, SQL Injection, etc.). 🔓  
- **🔁 Repeater (Request Manipulation)** - Allows manual modification ✏️ and resending of HTTP requests.  
- **🔍 Decoder & Comparer** - Helps decode 🛠️ data and analyze differences in HTTP requests.  

---

## 🚀 Installation and Running  

### 🐧 Kali Linux  
```bash
sudo apt install burpsuite
```

### 🖥️ Windows/Mac  
Download it from the [official website](https://portswigger.net/burp).  

---

## 🌐 Setting Up Proxy (To Capture Internet Traffic)  

1. Open **Burp Suite** and navigate to `Proxy > Options`.  
2. Set the **Listener** to:  
   - **IP:** `127.0.0.1`  
   - **Port:** `8080`  
3. Configure your browser’s **proxy settings**:  
   - **Firefox:** 🦊 `Settings > Network Settings > Manual Proxy Configuration`  
   - **Make sure Burp Suite's proxy service is running!** ✅  

---

## 🔍 Scanning the Target Website (Spider & Scanner)  

1. Go to `Proxy > Intercept` and ensure **Intercept is ON** 🎯.  
2. Visit a website 🌐 and browse its pages; all requests will appear in Burp Suite.  
3. Use `Spider` to **map the web application** 🗺️.  
4. **If you have the PRO version**, use `Scanner` to automatically scan for vulnerabilities 🛡️.  

---

## 🛠️ Manual Security Testing (Using Intruder & Repeater)  

- **💥 Use Intruder** for **brute-force attacks** 🔓 or fuzzing.  
- **🔁 Use Repeater** to modify ✏️ and resend specific HTTP requests.  

---

## ⚡ What Can You Do with Burp Suite?  

✔ **Test** web applications for vulnerabilities (**XSS, SQL Injection, CSRF**) 🛡️  
✔ **Capture and modify** form data ✍️  
✔ **Perform API security testing** 🔌  
✔ **Steal or manipulate** user sessions 🕵️‍♂️  
✔ **Conduct brute-force attacks and password testing** 🔓  



