import socket

def get_ip_address():
    website = "ktrv.ru"
    print("website: " + website)
    ip_address = socket.gethostbyname(website)
    print("IP Address:", ip_address)
    return ip_address


def scan_ports(target, start_port, end_port):
    print(f'Scanning target: {target}')
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f'Port {port}: Open')
        sock.close()


def main():
    target = get_ip_address()
    print("Target IP address: " , (target))
    start_port = int(input("Enter start port number: "))
    end_port = int(input("Enter end port number: "))

    scan_ports(target, start_port, end_port)

if __name__ == "__main__":
    main()
    