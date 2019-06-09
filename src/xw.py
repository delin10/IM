import sys, os, json, threading

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from udpmodule import open__server
from udpmodule import send_json

DEST_HOST = ''
PORT = 0


class Receiver(threading.Thread):
    def __init__(self, port, buffer_size):
        threading.Thread.__init__(self)
        self.port = port
        self.buffer_size = buffer_size

    def run(self):
        open__server(port=self.port, buffer_size=self.buffer_size)


def handle_input():
    try:
        while True:
            print('<', DEST_HOST, '>')
            line = input()
            msg = {'text': line}
            send_json(DEST_HOST, PORT, json.dumps(msg))
    except KeyboardInterrupt:
        print('exit')


def main():
    global DEST_HOST, PORT
    if len(sys.argv) < 3:
        print('require 2 arguments, exit. ')
        exit(1)
    DEST_HOST = str(sys.argv[1])
    PORT = int(sys.argv[2])
    print('dest host is ', DEST_HOST)
    receiver = Receiver(port=10002, buffer_size=1024)
    receiver.setDaemon(True)
    receiver.start()
    handle_input()
    try:
        receiver.join()
    except KeyboardInterrupt:
        print("interrupt!")


if __name__ == '__main__':
    main()
