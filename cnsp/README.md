# Cybersecurity Interview Questions and Answers
- Here the cnsp exam answers


## Table of Contents
1. [Authentication & Authorization](#authentication--authorization)
2. [Network Security](#network-security)
3. [Windows Security](#windows-security)
4. [Linux Security](#linux-security)
5. [Active Directory](#active-directory)
6. [Protocols & Services](#protocols--services)
7. [Attack Types](#attack-types)
8. [System Administration](#system-administration)

## Authentication & Authorization

**Question:** Which of the following statements regarding Authentication and Authorization is true?

**Answer:** Authentication verifies who someone is, while authorization determines what they are allowed to do. Authentication must occur before authorization.
______________________________________
### Password Hash Storage (Windows)
**Question:** Where are the password hashes stored in Windows 64-bit?

**Answer:** Password hashes are stored in:
- SAM database (C:\Windows\System32\config\SAM)
- NTDS.dit file (on domain controllers)
______________________________________
### Password Hash Storage (Linux)
**Question:** Where are password hashes stored in Linux?

**Answer:** In the `/etc/shadow` file, readable only by root user.
______________________________________
## Network Security

### TCP/UDP Ports
**Question:** How many usable TCP/UDP ports are there?

**Answer:** 65,535 usable ports (0-65535, with port 0 reserved), divided into:
- Well-Known Ports (1-1023)
- Registered Ports (1024-49151)
- Dynamic/Private Ports (49152-65535)
______________________________________
### SMB Security
**Question:** Which SMB versions are vulnerable to EternalBlue?

**Answer:** SMB v1 and v2 versions are vulnerable to the EternalBlue (MS17-010) exploit, affecting:
- Windows XP
- Windows 7
- Windows Server 2008
- Windows Server 2008 R2
______________________________________
## Windows Security

**What RID is given to an Administrator account on a MS Window's machine?**

The RID (Relative Identifier) given to the Administrator account on a Microsoft Windows machine is 500.
**What is the response from a closed UDP port which is not behind a firewall?**

When an ICMP packet is sent to a closed UDP port that is not behind a firewall, the typical response is an "ICMP Port Unreachable" message (ICMP Type 3, Code 3).
____________________________________________________________________________
**What is the response from a closed TCP port which is behind a firewall?**

When attempting to connect to a closed TCP port behind a firewall, typically there is no response (the packets are dropped/blocked), resulting in a connection timeout.
____________________________________________________________________________
**Where is the system registry file stored in a MS Windows Operating System?**

The Windows system registry files are stored in the %SystemRoot%\System32\Config directory (typically C:\Windows\System32\Config).
____________________________________________________________________________
**Which of the following represents a valid Windows Registry Key:**

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows is a valid Windows Registry Key.
____________________________________________________________________________
**Which of the following commands will work on Microsoft operating system to add a new domain admin user?**

Without a list of commands provided in the question, a correct command to add a new domain admin user would be:

```powershell
net user username password /add /domain
net group "Domain Admins" username /add /domain
```
____________________________________________________________________________
**How would you establish a null session to a windows host from a windows command prompt?**

To establish a null session to a Windows host from a command prompt, you can use the following command:

```
net use \\target_IP\IPC$ "" /user:""
```

This creates a connection to the IPC$ share with empty credentials, establishing what is known as a "null session." Note that modern Windows systems have security features that may prevent null sessions by default.
____________________________________________________________________________
## Linux Security

**In the context of a Unix-based system where does a daemon process executes in the memory?**

In Unix-based systems, daemon processes execute in the background and are not connected to any terminal. They typically run in user space memory (as opposed to kernel space), though some system daemons may have components that interact with kernel space. Daemons are usually started during the boot process and run until the system is shut down.
____________________________________________________________________________
**Which of the following files has the SGID permission set?**

-rwxr-sr-x 1 root rcot 4096 Jan 1 00:03 myfile

-rwsr-xr-x 1 root root 4896 Jan 1 20:00 myprogram

-rw-r--r-s 1 root root 4096 Jan 1 00:00 anotherfile

Answer: The file with the SGID (Set Group ID) permission set is: `-rwxr-sr-x 1 root rcot 4096 Jan 1 00:03 myfile`

The 's' in the group permission section (r-s) indicates the SGID bit is set.
____________________________________________________________________________
**Which of the following files has the SUID permission set?**

-rwxr-sr-x 1 root root 4096 Jan 1 00:00 myfile

-rwsr-xr-x 1 root root 4096 Jan 1 00:00 myprogram

-rw-r--r-s 1 root root 4096 Jan 1 00:00 anotherfile

Answer: -rwsr-xr-x 1 root root 4096 Jan 1 00:00 myprogram

The SUID bit is represented by the 's' in the user's execute position (4th character).
____________________________________________________________________________

**Which of the following is an example of a SUID program?**

A. /bin/ls

B. /usr/bin/curl

C. /usr/bin/passwd

D. None of the above

Answer: C. /usr/bin/passwd. The passwd program needs to run with root privileges to modify the password file, even when executed by regular users, making it a classic example of a SUID program.
____________________________________________________________________________

**What kind of files are "Dotfiles" in a Linux-based architecture?**

Dotfiles in a Linux-based architecture are configuration files that begin with a dot (.) character. These files are hidden by default when listing directory contents using standard commands. They typically store user-specific application settings and preferences. Examples include .bashrc, .profile, and .vimrc files that configure the bash shell, user environment, and vim editor respectively.
____________________________________________________________________________

**In a Linux-based architecture, what does the /mnt directory contain?**

The /mnt directory in a Linux-based architecture contains temporarily mounted filesystems. It's used as a temporary mount point for mounting storage devices like CD-ROMs, USB drives, or network shares.
____________________________________________________________________________

## Active Directory

**What user account is required to create a Golden Ticket in Active Directory?**

To create a Golden Ticket in Active Directory, an attacker needs the KRBTGT account password hash. The KRBTGT account is a special service account used by the Key Distribution Center (KDC) in Active Directory to encrypt and sign all Kerberos tickets.
____________________________________________________________________________

**The active directory database file stores the data and schema information for the Active Directory database on domain Microsoft Windows operating systems. Which of the following file is the active directory database file?**

Answer: The active directory database file is **ntds.dit**. This file stores all Active Directory data, including objects, attributes, and security principals.
____________________________________________________________________________

## Protocols & Services

**Which of the following Protocols is not vulnerable to address spoofing attacks if implemented correctly?**

TCP with SYN cookies is not vulnerable to address spoofing if implemented correctly due to its three-way handshake mechanism and sequence number verification.
____________________________________________________________________________

**Which one of the following services is not an UDP based protocol?**

Without a list of services provided in the question, it's difficult to give a specific answer. However, common services that use TCP rather than UDP include HTTP, HTTPS, SSH, FTP, SMTP, and Telnet. UDP-based services typically include DNS (though it can use both), DHCP, SNMP, TFTP, and streaming media.
____________________________________________________________________________

**Which of the following services use TCP protocol?**

Answer: Services that use TCP protocol include HTTP, HTTPS, FTP, SSH, SMTP, POP3, IMAP, and TELNET, among others.
____________________________________________________________________________

**Which of the following services do not encrypt its traffic by default?**

Answer: Services that do not encrypt traffic by default include:

- FTP (File Transfer Protocol)
- Telnet
- HTTP (non-HTTPS web traffic)
- SMTP (without STARTTLS)
- SNMP v1 and v2
____________________________________________________________________________

**Which of the following is a valid DNS record Type?**

A. NAPTR record

B. SRV record

C. TXT record

D. All of the above

Answer: D. All of the above. NAPTR (Naming Authority Pointer), SRV (Service), and TXT (Text) are all valid DNS record types.
____________________________________________________________________________

**What ports can be queried to perform a DNS zone transfer?**

Answer: DNS zone transfers typically use TCP port 53. While regular DNS queries can use both UDP/53 and TCP/53, zone transfers specifically require TCP/53 due to the larger amount of data being transferred.
____________________________________________________________________________

**Which command will perform a DNS zone transfer of the domain '[victim.com](http://victim.com)' from the nameserver at 10.0.0.1?**

Answer: The command to perform a DNS zone transfer is: "dig @10.0.0.1 [victim.com](http://victim.com) axfr" or alternatively "host -l [victim.com](http://victim.com) 10.0.0.1"
____________________________________________________________________________

**If a Hash begins with $2a$ what hashing algorithm has been used?**

Answer: If a hash begins with $2a$, the hashing algorithm used is **Bcrypt and also MD5** .
____________________________________________________________________________

**Which of the following algorithms could be used to negotiate a shared encryption key?**

Answer: Algorithms that could be used to negotiate a shared encryption key include:

- Diffie-Hellman key exchange
- RSA
- Elliptic Curve Diffie-Hellman (ECDH)
- Key Exchange Algorithm (KEA)
____________________________________________________________________________

**Which of the following attacke associated with an ICMP protocol?**

Answer: Attacks associated with the ICMP protocol include:

- ICMP Flooding (Ping Flood)
- Ping of Death
- Smurf Attack
- ICMP Tunneling
- ICMP Redirect Attacks
____________________________________________________________________________

**What ports does a MSSQL server typically use?**

Answer: MSSQL server typically uses port 1433 for TCP connections and port 1434 for UDP connections (SQL Server Browser service).
____________________________________________________________________________

**Which built-in Windows utility can be used to verify the validity of a Kerberos ticket?**

Answer: The built-in Windows utility that can be used to verify the validity of a Kerberos ticket is **klist**. This command-line tool displays and purges Kerberos tickets.
____________________________________________________________________________

**Which Kerberos ticket is required to generate a Silver Ticket?**

Answer: The service ticket (TGS - Ticket Granting Service ticket) is required to generate a Silver Ticket. A Silver Ticket is a forged TGS ticket that grants access to a specific service.
____________________________________________________________________________

## Attack Types

**Which of the following is not a DDoS Attack?**

SQL Injection is not a DDoS (Distributed Denial of Service) attack. It is a type of injection attack that targets databases.
____________________________________________________________________________

**Which one of the following is not an online attack?**

Physical theft of hardware is not an online attack. It is a physical security breach rather than a network-base/d or online attack.
____________________________________________________________________________

**What types of attacks are phishing, spear phishing, vishing, scareware, and watering hole?**

Answer: Phishing, spear phishing, vishing, scareware, and watering hole are all types of social engineering attacks.
____________________________________________________________________________

**WannaCry, an attack, spread throughout the world in May 2017 using machines running on outdated Microsoft operating system. What is WannaCry?**

WannaCry is a ransomware worm that spread globally in May 2017. It targeted computers running Microsoft Windows operating systems, particularly those with outdated versions. It encrypted users' files and demanded ransom payments in Bitcoin cryptocurrency to restore access. WannaCry exploited the EternalBlue vulnerability in older Windows systems that had not been patched with the latest security updates.
____________________________________________________________________________

## System Administration

**In the context of the SSH (Secure Shell) public-private key authentication mechanism, which key is uploaded to the server and which key is used by the end-user for authentication?**

Answer: The public key is uploaded to the server and stored in the ~/.ssh/authorized_keys file. The private key is kept securely by the end-user and is used for authentication.
____________________________________________________________________________

**Which is the correct command to change the MAC Address for an Ethernet Adapter in a Unix-based system?**

Answer: The command to change MAC address in Unix-based systems is typically: "ifconfig eth0 hw ether XX:XX:XX:XX:XX:XX" or on newer systems: "ip link set dev eth0 address XX:XX:XX:XX:XX:XX" (where eth0 is the interface name and XX:XX:XX:XX:XX:XX is the new MAC address).
____________________________________________________________________________

**You are performing a security audit on a company's infrastructure and have discovered that the domain name system (DNS) server is vulnerable to a DNS cache poisoning attack. What is the primary security risk?**

Answer: The primary security risk of DNS cache poisoning is that attackers can redirect users to malicious websites while they believe they're visiting legitimate ones. This can lead to phishing attacks, malware distribution, or intercepting sensitive information.
____________________________________________________________________________

**A system encrypts data prior to transmitting it over a network, and the system on the other end of the transmission media are using the symmetric encryption algorithm for encryption and decryption, which of the following statements is true?**

Both systems must share the same encryption key. Symmetric encryption uses a single key for both encryption and decryption processes.
____________________________________________________________________________

**The Management Information Base (MIB) is a collection of object groups that is managed by which service?**

The Management Information Base (MIB) is managed by the Simple Network Management Protocol (SNMP) service. MIBs define the structure of the management data of a device subsystem, using a hierarchical namespace containing object identifiers (OIDs). SNMP agents on managed devices provide this information to network management systems for monitoring network performance and troubleshooting.
____________________________________________________________________________

**What is the response from a closed TCP port which is not behind a firewall?**

When a TCP SYN packet is sent to a closed TCP port that is not behind a firewall, the receiving system will typically respond with a TCP RST (Reset) packet. This indicates that no service is listening on that port and the connection attempt is being actively rejected. 
____________________________________________________________________________

**What is the response from an open UDP port which is not behind a firewall?**

When a UDP packet is sent to an open UDP port that is not behind a firewall, there is typically no response unless the application listening on that port is configured to respond. UDP is connectionless, so there's no built-in acknowledgment mechanism like in TCP. If no application responds, the sender may receive an ICMP "Port Unreachable" message, but this depends on the system configuration.
____________________________________________________________________________

**What is the response from an open UDP port which is behind a firewall (port is open on the firewall)?**

When a UDP packet is sent to an open UDP port that is behind a firewall (but the port is open on the firewall), there is typically no response. The packet is allowed through the firewall to the target system, but since UDP is connectionless, there is no acknowledgment sent back. If the application listening on that port is configured to respond, it might send a reply, but this is application-dependent.
____________________________________________________________________________

# TLS Error Question

The application is showing a TLS error message as a result of a website administrator failing to timely renew the TLS certificate. Upon deeper analysis, it appears that the problem is brought on by the expiration of the TLS certificate.

Which of the following statement is correct:

A. The communication between the browser and the server is now no longer over TLS.

B. The communication between the browser and the server is still over TLS.

Answer: A. The communication between the browser and the server is now no longer over TLS. When a TLS certificate expires, the secure connection cannot be established, reverting to unencrypted communication or failing completely.
____________________________________________________________________________

# EICAR File

An 'EICAR' file can be used to?

Answer: An EICAR file is used to test antivirus software functionality without using actual malware. It's a standard test file recognized by all antivirus products as malicious, but is actually harmless.
____________________________________________________________________________

# SNMP Question

Which of the following is true for SNMP?

A. The default community string for read-only access is public.

B. The default community string for read/write access is private.

Answer: Both A and B are correct. In SNMP v1 and v2c, "public" is the default community string for read-only access, and "private" is the default community string for read/write access.
____________________________________________________________________________

# MAC Address Change Command

Which is the correct command to change the MAC Address for an Ethernet Adapter in a Unix-based system?

Answer: The command to change MAC address in Unix-based systems is typically: "ifconfig eth0 hw ether XX:XX:XX:XX:XX:XX" or on newer systems: "ip link set dev eth0 address XX:XX:XX:XX:XX:XX" (where eth0 is the interface name and XX:XX:XX:XX:XX:XX is the new MAC address).
____________________________________________________________________________

# DNS Record Types

Which of the following is a valid DNS record Type?

A. NAPTR record

B. SRV record

C. TXT record

D. All of the above

Answer: D. All of the above. NAPTR (Naming Authority Pointer), SRV (Service), and TXT (Text) are all valid DNS record types.
____________________________________________________________________________

# DNS Zone Transfer Ports

What ports can be queried to perform a DNS zone transfer?

Answer: DNS zone transfers typically use TCP port 53. While regular DNS queries can use both UDP/53 and TCP/53, zone transfers specifically require TCP/53 due to the larger amount of data being transferred.
____________________________________________________________________________

# Port 111/TCP

If you find the 111/TCP port open on a Unix system, what is the next logical step to take?

Answer: Port 111 is used by the portmapper service (rpcbind). The next logical step would be to query the RPC service using commands like "rpcinfo -p" to enumerate available RPC services, which could reveal additional attack vectors.
____________________________________________________________________________

# DNS Zone Transfer Command

Which command will perform a DNS zone transfer of the domain '[victim.com](http://victim.com)' from the nameserver at 10.0.0.1?

Answer: The command to perform a DNS zone transfer is: "dig @10.0.0.1 [victim.com](http://victim.com) axfr" or alternatively "host -l [victim.com](http://victim.com) 10.0.0.1"
____________________________________________________________________________

# DNS Cache Poisoning Risk

You are performing a security audit on a company's infrastructure and have discovered that the domain name system (DNS) server is vulnerable to a DNS cache poisoning attack. What is the primary security risk?

Answer: The primary security risk of DNS cache poisoning is that attackers can redirect users to malicious websites while they believe they're visiting legitimate ones. This can lead to phishing attacks, malware distribution, or intercepting sensitive information.
____________________________________________________________________________

# SUID Permission

Which of the following files has the SUID permission set?

-rwxr-sr-x 1 root root 4096 Jan 1 00:00 myfile

-rwsr-xr-x 1 root root 4096 Jan 1 00:00 myprogram

-rw-r--r-s 1 root root 4096 Jan 1 00:00 anotherfile

Answer: -rwsr-xr-x 1 root root 4096 Jan 1 00:00 myprogram

The SUID bit is represented by the 's' in the user's execute position (4th character).
____________________________________________________________________________

# SSH Key Authentication

In the context of the SSH (Secure Shell) public-private key authentication mechanism, which key is uploaded to the server and which key is used by the end-user for authentication?

Answer: The public key is uploaded to the server and stored in the ~/.ssh/authorized_keys file. The private key is kept securely by the end-user and is used for authentication.
____________________________________________________________________________

# SUID Program Example

Which of the following is an example of a SUID program?

A. /bin/ls

B. /usr/bin/curl

C. /usr/bin/passwd

D. None of the above

Answer: C. /usr/bin/passwd. The passwd program needs to run with root privileges to modify the password file, even when executed by regular users, making it a classic example of a SUID program.
____________________________________________________________________________

# SMB Versions Vulnerable to EternalBlue

Which SMB (Server Message Block) network protocol versions are vulnerable to the EternalBlue (MS17-010) Windows exploit?

Answer: SMB v1 and SMB v2 versions are vulnerable to the EternalBlue exploit. Specifically, Windows systems running SMB protocol versions 1.0 through 2.0 are affected, which includes Windows XP, Windows 7, Windows Server 2008, and Windows Server 2008 R2.