import socket
import json

'''开启UDP Socket
'''


def open_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def connect(host, port):
    fd = open_socket()
    fd.connect((host, port))
    return fd


def send_json(host, port, json):
    try:
        with connect(host, port) as fd:
            fd.sendall(bytearray(json.encode('utf-8')))
    except OSError as msg:
        print(msg)


def open__server(port, buffer_size):
    addr = ('', port)
    try:
        with open_socket() as fd:
            fd.bind(addr)
            while True:
                data, addr = fd.recvfrom(buffer_size)
                print('recvfrom', addr[0])
                print('content:', json.loads(data.decode('utf-8'))['text'])
    except OSError as msg:
        print('openserver error:', msg)
