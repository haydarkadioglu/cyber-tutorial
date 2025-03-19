

🔥 Kali Linux Essential Commands (Without Additional Tools!)

These are built-in commands that help you manage the system, analyze networks, and perform basic operations in Kali Linux.

📌 1. System & User Information

uname -a                # Show kernel information
cat /etc/os-release     # Display Kali Linux version
uptime                  # Show system uptime
whoami                  # Show current username
who                     # List logged-in users
id                      # Display user UID, GID, and group info

📌 2. User Management

useradd hacker           # Create a new user
passwd hacker            # Set a password for the user
usermod -aG sudo hacker  # Add user to the sudo group
cat /etc/passwd          # List all users
deluser hacker           # Delete a user

📌 3. File & Directory Management

ls -la                # List all files including hidden ones
pwd                   # Show current directory
cd /var/log           # Change directory
mkdir test            # Create a new folder
rm -rf test           # Delete a folder with its contents
touch newfile.txt     # Create an empty file
cp file1.txt file2.txt  # Copy a file
mv file1.txt /home/user/  # Move or rename a file

📌 4. Viewing File Contents

cat file.txt          # Display file content
less file.txt         # View file content page by page
head -n 10 file.txt   # Show the first 10 lines
tail -n 10 file.txt   # Show the last 10 lines

📌 5. Network & Internet Commands

ip a                  # Show IP addresses
ifconfig              # (Deprecated) Show network interfaces
ip route show         # Display routing table

ping 8.8.8.8          # Send ICMP packets to test connection
traceroute google.com # Trace the route to a host
arp -a                # List devices on the local network
netstat -tulnp        # Show open ports and services
ss -tulnp             # Alternative to netstat (faster)

📌 6. DNS Lookup & Resolution

nslookup google.com   # Find the IP of a domain
dig google.com        # Detailed DNS lookup
host google.com       # Quick DNS resolution

📌 7. Managing Processes & Services

ps aux                # List all running processes
top                   # Show real-time system usage
htop                  # Advanced process viewer (if installed)
kill <PID>            # Kill a process by ID
pkill firefox         # Kill a process by name

systemctl start apache2   # Start a service
systemctl stop apache2    # Stop a service
systemctl restart ssh     # Restart a service
systemctl enable apache2  # Enable a service at startup
systemctl disable apache2 # Disable a service at startup

📌 8. Disk & Memory Management

df -h                 # Show disk usage (in GB/MB)
du -sh /var           # Show folder size
mount                 # Show mounted disks

free -h               # Show RAM usage
vmstat 5              # System performance every 5 seconds

📌 9. Log Analysis

cat /var/log/syslog    # Show system logs
tail -f /var/log/auth.log   # Monitor authentication logs
journalctl -xe         # Show detailed logs

📌 10. File Permissions & Ownership

ls -l file.txt        # Show file permissions
chmod 777 file.txt    # Give full permissions (Risky!)
chmod 644 file.txt    # Read-only for others
chown root:root file.txt  # Change file owner

📌 11. Cryptography (Hashing & Encryption)

echo -n "password123" | md5sum    # Generate an MD5 hash
echo -n "password123" | sha256sum # Generate a SHA-256 hash

gpg -c secret.txt    # Encrypt a file (will ask for a password)
gpg secret.txt.gpg   # Decrypt the file


---

🎯 Summary

These commands help you with:
✅ User & system management
✅ File & directory operations
✅ Network scanning & analysis
✅ Process & service management
✅ Disk & memory monitoring
✅ Log analysis & cryptography

🔥 Now you're ready to master Kali Linux! 🚀

