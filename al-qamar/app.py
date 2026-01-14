import socket
import uuid

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

mac = uuid.getnode()
mac_address = ':'.join(f'{(mac >> i) & 0xff:02x}' for i in range(40, -1, -8))

print("System Name:", hostname)
print("IP Address:", ip)
print("MAC Address:", mac_address)
