import socket
import json

SERVER_IP = 'nut5.lukoil.net'
PORT = 10987


def send_sms_and_get_status(phone_list, text):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_IP, PORT))
    data = {'phones': phone_list, 'text': text}
    serialized_data = json.dumps(data)
    sock.send(serialized_data.encode('utf-8'))
    status = sock.recv(1024).decode('utf-8')
    sock.close()
    return f'Sended to {len(phone_list)} {status}'
