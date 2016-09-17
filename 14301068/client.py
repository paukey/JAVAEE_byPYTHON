# coding=utf-8
# Author:paukey
# Date:2016-9-15
# python 2.7
# version 1.0


"""
这货是web服务器的客户端
"""

import socket
import sys

HOST = '127.0.0.1'
PORT = 3333
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))

while 1:
    data = raw_input('input:')
    clientSocket.send(data)

    buf = clientSocket.recv(4096)
    if not len(buf):
        break
    sys.stdout.write(buf)

clientSocket.close()
