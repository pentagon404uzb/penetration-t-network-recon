import socket
from termcolor import colored
import threading
import sys

# Permission statement
print(colored("[*] Authorized penetration test. Proceeding with reconnaissance...\n", "cyan"))

# Input victim IP
target_ip = input(colored("Enter the victim IP address: ", "yellow"))

# Scan settings
common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
scan_all_ports = False

mode = input(colored("Choose scan mode - (1) Common ports, (2) Advanced (all ports): ", "yellow"))
if mode == "2":
    scan_all_ports = True

open_ports = []

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(colored(f"[+] Port {port} is open - Service: {service}", "green"))
            open_ports.append(port)
        sock.close()
    except Exception as e:
        print(colored(f"[-] Error scanning port {port}: {e}", "red"))

def main():
    ports_to_scan = common_ports if not scan_all_ports else range(1, 65536)
    print(colored(f"\n[*] Starting scan on {target_ip}...\n", "cyan"))

    threads = []
    for port in ports_to_scan:
        t = threading.Thread(target=scan_port, args=(port,))
        threads.append(t)
        t.start()

        # Limit threads to avoid overload
        if len(threads) >= 100:
            for thread in threads:
                thread.join()
            threads = []

    # Join remaining threads
    for thread in threads:
        thread.join()

    print(colored(f"\n[*] Scan complete. Open ports: {open_ports}", "cyan"))

if __name__ == "__main__":
    main()
