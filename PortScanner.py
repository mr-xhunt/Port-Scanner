import pyfiglet
import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Displaying the ASCII banner
ascii_banner = pyfiglet.figlet_format("MX PORT SCANNER")
print(ascii_banner)

# Usage function to show help information
def show_usage():
    print("Usage: python3 scanner.py <hostname> [-p <port_range>]")
    print("Options:")
    print("  -h                   Show this help message and exit")
    print("  -p <port_range>      Specify a port or range of ports to scan (e.g., 80 or 1-1024)")
    print("Examples:")
    print("  python3 scanner.py example.com             # Scan common ports on example.com")
    print("  python3 scanner.py example.com -p 80       # Scan only port 80 on example.com")
    print("  python3 scanner.py example.com -p 20-80    # Scan ports 20 to 80 on example.com")
    print("  python3 scanner.py example.com -p 80       # Scan only port 80 on example.com")
    print("  python3 scanner.py example.com -p 20-80    # Scan ports 20 to 80 on example.com")
    print("  python3 scanner.py 192.168.1.1 -p 443      # Scan only port 443 on IP address 192.168.1.1")
    print("  python3 scanner.py 192.168.1.1 -p 1000-2000 # Scan ports 1000 to 2000 on IP address 192.168.1.1")

# Parsing arguments
if len(sys.argv) < 2:
    print("Invalid number of arguments!")
    show_usage()
    sys.exit()

if sys.argv[1] == '-h':
    show_usage()
    sys.exit()

# Defining the target and port range
target = sys.argv[1]
try:
    # Translate hostname to IPv4
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("\nHostname Could Not Be Resolved!")
    sys.exit()

# Default port range (if none specified)
start_port = 1
end_port = 1024

# Check for the -p option to specify a port or range
if len(sys.argv) > 3 and sys.argv[2] == '-p':
    port_input = sys.argv[3]
    if '-' in port_input:
        # Range of ports
        start_port, end_port = map(int, port_input.split('-'))
    else:
        # Single port
        start_port = end_port = int(port_input)

# Adding a banner
print("-" * 50)
print("Scanning Target: " + target_ip)
print("Scanning started at: " + str(datetime.now()))
print(f"Port Range: {start_port} to {end_port}")
print("-" * 50)

# Port scanning function
def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

try:
    # Scanning ports with threading
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, port)
except KeyboardInterrupt:
    print("\nExiting Program!")
    sys.exit()
except socket.error:
    print("\nServer not responding!")
    sys.exit()

print("-" * 50)
print("Scanning completed at: " + str(datetime.now()))
print("-" * 50)
