import socket
import subprocess

def get_hostname_info(hostname):
    try:
        # Get IP address from hostname
        ip_address = socket.gethostbyname(hostname)
        print(f"IP Address: {ip_address}")

        # Get canonical hostname from IP address
        canonical_hostname = socket.getfqdn(ip_address)
        print(f"Canonical Hostname: {canonical_hostname}")

        # Get the list of IP addresses associated with the hostname
        ip_addresses = socket.getaddrinfo(hostname, None)
        ip_addresses = [addr[4][0] for addr in ip_addresses]
        print(f"All IP Addresses: {', '.join(ip_addresses)}")

        # Ping the hostname to get round-trip time and other statistics
        ping_output = subprocess.check_output(['ping', '-c', '4', hostname], universal_newlines=True)
        print("Ping Statistics:")
        print(ping_output)
    except socket.gaierror:
        print("Hostname could not be resolved.")

if __name__ == "__main__":
    hostname = input("Enter the hostname: ")
    get_hostname_info(hostname)
