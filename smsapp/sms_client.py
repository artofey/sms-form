import socket
import json

SERVER_IP = '10.254.17.70'
PORT = 10987

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))
data = {'number': '79850612580',
        'text': 'Розовый комар укусил Путина. '}
serialized_data = json.dumps(data)
sock.send(serialized_data.encode('utf-8'))

# data = b""
tmp = sock.recv(1024)
# while tmp:
#     data += tmp
#     tmp = sock.recv(1024)
print(tmp.decode('utf-8'))
sock.close()
