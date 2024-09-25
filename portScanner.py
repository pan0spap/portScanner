import socket
import sys
from datetime import datetime

target = input('Enter a host to scan: ')

print('-' * 50)
print('Scanning Target:' + target)
print('Scanning started at:' + str(datetime.now()))

t1 = datetime.now()

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open.")

        s.close
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved.")

except socket.error:
    print("Server not responding...")

except KeyboardInterrupt:
    print('You pressed CTRL+C')  
    sys.exit() 
t2 = datetime.now()

total = t2 - t1

print(f'Scanning complete at {total}')
print('-' * 50)
