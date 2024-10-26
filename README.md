# Port-Scanner
MX Port Scanner is a Python-based port scanning tool that allows users to scan for open ports on a specified target IP address or hostname. It can perform scans across a range of ports, single ports, or common ports, using threading to increase scan speed. With MX Port Scanner, users can easily identify open ports on a server for testing and security auditing purposes.

<h3>Features</h3>

    Customizable Port Scanning: Scan a specific port, a range of ports, or all common ports.
    Multithreaded: Uses threading to speed up the scanning process.
    ASCII Art Banner: Welcomes users with an ASCII banner for a fun CLI experience.
    Error Handling: Provides meaningful error messages for network and input errors.
    Lightweight and Simple to Use: Requires only basic Python libraries and runs on the command line.

<h3>Requirements</h3>

    Python 3.x
    Modules:
        pyfiglet: For the ASCII banner.
        socket: For network communication.
        concurrent.futures: For multithreaded port scanning.

To install the required module, run:
`pip install pyfiglet`

<h3> Usage</h3>
Basic Command
`python3 scanner.py <hostname>`
This command scans the common ports (1-1024) on the specified hostname.

<h3>Options</h3>

    -h: Displays help information.
    -p <port_range>: Specifies a port or range of ports to scan. You can provide a single port (e.g., 80) or a range (1-1024).

Examples

Scan all common ports on a hostname:

`python3 scanner.py example.com`

Scan a specific port on a hostname:

`python3 scanner.py example.com -p 80`

Scan a range of ports on a hostname:

`python3 scanner.py example.com -p 20-80`

Scan a specific port on an IP address:

`python3 scanner.py 192.168.1.1 -p 443`

Scan a range of ports on an IP address:

`python3 scanner.py 192.168.1.1 -p 1000-2000`

<h3>Error Handling</h3>

    Hostname Could Not Be Resolved: Triggered if the hostname provided cannot be converted to an IP address.
    Server Not Responding: Displays when there is no response from the server.
    Exiting Program: Shows when the scan is interrupted (e.g., by pressing CTRL+C).

# License

This project is open-source and available for anyone to use and modify.
Disclaimer

Use MX Port Scanner responsibly and only on networks you have permission to test. Unauthorized port scanning may be illegal in some jurisdictions.
