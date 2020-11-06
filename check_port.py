## For checking your port whether it was used.

import socket
import random

port = random.randint(5000, 5100)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('0.0.0.0',port))

### If used, it would go to while loop until choosing one port which can be used.
while result == 0:
    port = random.randint(5000, 5100)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('0.0.0.0',port))

print(port)