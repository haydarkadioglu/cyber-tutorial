📌 **Guide to Using DirBuster on Kali Linux** 🐧

DirBuster is a powerful tool for discovering hidden directories and files on websites. It comes pre-installed in Kali Linux and is very user-friendly. Let's learn step-by-step! 🚀

### 1️⃣ Launching DirBuster

Open the terminal in Kali Linux and run the following command:

```bash
dirbuster
```

The interface will automatically open.

### 2️⃣ Setting the Target 🎯

In DirBuster's main window:
- Enter the target website URL in the **Target URL:** field. For example:

```
http://targetwebsite.com
```

### 3️⃣ Choosing a Wordlist 📚

DirBuster uses a "wordlist" to find directories on a website:
- Click the **Browse** button.
- Wordlists in Kali Linux are located here:

```
/usr/share/wordlists/dirbuster/
```

You can find several wordlists here, for instance:

- **directory-list-2.3-medium.txt** (Medium size, quick scanning)
- **directory-list-2.3-big.txt** (Large, detailed but slower scanning)

Select your preferred wordlist and click "Open" to continue.

### 4️⃣ Configuring Settings 🔧

- **Threads:** Number of simultaneous requests. The default (10-20) is recommended. Higher values may stress the web server.
- **File extension:** Enter extensions such as PHP, HTML, JS to find specific file types. For example:
```
php,html,js
```

### 5️⃣ Starting the Scan 🚨

Once everything is ready, click the **"Start"** button to begin scanning. DirBuster will display results in real-time.

### 6️⃣ Analyzing Results and Reporting 📈

Scan results will appear on the screen:
- Status codes (e.g., 200, 403)
- List of discovered directories and files

You can right-click on found directories and files to open them in a browser and analyze further.

### 🛡️ Additional Tips
- If you suspect the site is using a WAF (Web Application Firewall), reduce Threads to perform a slower scan.
- You can stop the scan at any time using the **Stop** button.
- Save results by using the **Report** menu.

🎉 **You're now ready to uncover hidden directories with DirBuster! Happy exploring! 🕵️‍♂️**