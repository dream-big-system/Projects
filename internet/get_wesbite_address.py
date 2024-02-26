import socket
website = "ktrv.ru"
ip_address = socket.gethostbyname(website)
print("IP Address:", ip_address)
