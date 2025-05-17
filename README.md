# CTF Challenge: Network Recon & Exploitation
in this capture the flag (CTF) : will be examined the technique of the reconnaissance,  discovering open and common ports, sniffing, analyzing traffic with Wireshark and exploiting a vulnerability

## Task : 
You are a penetration tester tasked with assessing the security of two target machines (Metasploitable and Ubuntu) on a network. Your Kali machine is the attacker. Your goal is to identify open ports on both targets, capture and analyze network traffic with Wireshark, and exploit a vulnerability on Metasploitable to gain a shell.
### [~]$%

## Overview

This Capture The Flag (CTF) exercise demonstrates practical penetration testing techniques focused on network reconnaissance, port scanning, traffic sniffing, and vulnerability exploitation. The targets include two virtual machines (Metasploitable and Ubuntu), with Kali Linux acting as the attacker machine.

The main objectives are to:

- Perform network reconnaissance to discover live hosts and open ports.
- Identify common services running on the target machines.
- Capture and analyze network traffic using Wireshark.
- Exploit a known vulnerability on the Metasploitable VM to gain shell access.
- Transfer files between attacker and target machines.

## Authorization

I confirm that I have explicit permission and authorization to perform penetration testing and security assessments on the systems involved in this exercise. All activities were conducted in a controlled, legal environment with no unauthorized access or harm to any systems outside the scope of this test.

## Environment Setup

- **Attacker:** Kali Linux
- **Targets:** Metasploitable, Ubuntu Linux
- **Tools Used:** Nmap, Wireshark, Metasploit Framework, SCP, wget/curl

## Methodology

### 1. Network Reconnaissance and Port Scanning

- Used `nmap` to scan the target IP addresses for open ports and running services.
- Command example:
  ```bash
  nmap -sS -sV -p- <target-ip>
### 2. Traffic Capture and Analysis
Captured network traffic on the attacker machine’s network interface using Wireshark during the scanning process.
Analyzed captured packets to observe TCP handshakes, port scanning patterns, and service banners.
Identified suspicious or interesting traffic that could indicate vulnerabilities or misconfigurations.


### 3. Vulnerability Identification and Exploitation
Reviewed the open ports and services discovered during scanning to identify known vulnerabilities.
Focused on vulnerable services such as the vsftpd 2.3.4 backdoor on Metasploitable.
Used Metasploit Framework to exploit the identified vulnerability and gain remote shell access.
Example Metasploit commands:
```bash
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOST <metasploitable-ip>
run
```
### 4. Post-Exploitation Activities
Once shell access was obtained, gathered system information to understand the target environment.
Checked for additional vulnerabilities or sensitive data that could be leveraged.
Demonstrated file transfer capabilities by moving an image file from the attacker to the Ubuntu target using SCP.
Verified successful file transfer and displayed the image on the Ubuntu machine.

### 5. Reporting and Recommendations
Documented all findings, including open ports, vulnerabilities, exploitation steps, and post-exploitation results.
Provided recommendations to remediate discovered vulnerabilities and improve overall network security.
Emphasized the importance of patching vulnerable services and monitoring network traffic for suspicious activity.
