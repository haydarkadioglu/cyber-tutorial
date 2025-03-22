## 🚀 **Comprehensive DIRB Commands and Parameters Guide**

**DIRB** is a powerful command-line tool designed to scan and discover hidden directories and files on websites. It performs brute-force attacks using predefined wordlists to find sensitive directories and files.

### 🔧 **Installation on Kali Linux (usually pre-installed):**

If DIRB isn't installed, run:

```bash
sudo apt update
sudo apt install dirb
```

---

## 📌 **Detailed Command Syntax:**

**Basic Syntax:**
```bash
dirb [URL] [wordlist] [options]
```

**Example:**
```bash
dirb http://targetwebsite.com /usr/share/wordlists/dirb/common.txt
```

---

## 📚 **Recommended Wordlists:**
- Default location in Kali Linux: `/usr/share/wordlists/dirb/`
- Example popular wordlist: **common.txt**, **big.txt**

You can download additional comprehensive wordlists from:
- [lists](https://github.com/haydarkadioglu/cyber-tutorial/tree/main/kali-tools/dirbuster/lists)

---

## 📑 **Comprehensive DIRB Tool Parameters and Practical Examples**

DIRB is a web content scanner used to find hidden directories and files on web servers by using brute-force methods with wordlists. Below is a detailed explanation of DIRB parameters along with practical command examples to enhance your penetration testing efficiency.

## 📑 **DIRB Tool Parameters and Example Usage**

### **Detailed Parameters:**

- `-r`: Recursively scan discovered directories.
- `-X`: Specify file extensions to search for.
  - Example:
  ```bash
  dirb http://targetwebsite.com common.txt -X .php,.html,.js
  ```

- `-w`: Do not stop on warnings; continue scanning.
- `-v`: Enable verbose output for detailed information.
- `-S`: Silent mode; show only discovered items.
- `-o`: Output results to a file.
  - Example:
  ```bash
  dirb http://targetwebsite.com common.txt -o output.txt
  ```

- `-H`: Set custom HTTP headers.
  - Example:
  ```bash
  dirb http://targetwebsite.com common.txt -H "User-Agent: CustomUserAgent"
  ```

- `-u <username:password>`: HTTP Basic authentication.
- `-a <user-agent>`: Specify custom user agent.
- `-P <proxy:port>`: Use a proxy server.
- `-N <status-code>`: Ignore specified HTTP status codes.
  - Example:
  ```bash
  dirb http://targetwebsite.com common.txt -N 403
  ```

- `-c <cookie>`: Use a specific cookie for the scan.

---

### 📌 **Complete Example Test:**

Recursively scan with verbose mode, ignoring HTTP 403 status codes, and save results to file:

```bash
dirb http://targetwebsite.com common.txt -r -v -N 403 -o scan_results.txt
```



### ⚠️ **Ethical and Legal Reminder:**
Always ensure you have explicit permission to conduct scans on any website. Unauthorized scanning is illegal and unethical.

🚀 **Stay Ethical and Secure!**

