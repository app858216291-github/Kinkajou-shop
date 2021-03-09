#/usr/bin/python
import socket
import sys
import os

from _thread import *

HOST = '';PORT = 8887
print(sys.argv);


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
    s.bind((HOST, PORT))
except Exception:
    # print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    # print(str(msg[0]))
    sys.exit()

print ('Socket bind complete')

s.listen(10)

print ('Socket now listening')

def assces_log(request):
    # fp = open('http.log', "aw")
    # fp.write(request+"\r\n")
    # fp.close()
    pass

def parse_request(request):
    request = request.splitlines()
    line = request[0]
    line = line.split();
    dict_request = {'method':line[0], 'path':line[1], 'version':line[2]}
    return dict_request

while True:
    conn, addr = s.accept()
    request = conn.recv(1024)
    print (request)
    print ("\r\n")
    try:
        dist_request = parse_request(request)
    except Exception as e:
        print(e)
        continue
    path='E:/codes/Kinkajou-shop/Kinkajou/installer/h5'
    print(dist_request['path'])
    filename=bytes.decode(dist_request['path'])
    if filename=='/':
        # dist_request['path']='/index.html'
        filename=r'/index.html'
    path = path + filename

    # path=path+str(dist_request['path'], encoding = "UTF-8")
    
    # print(os.getcwd())
    # path = dist_request['path']
    path = os.getcwd() + filename
    result = eval(repr(path).replace('\\', '/'))
    result = eval(repr(result).replace('//', '/'))
    # path=path.replace(r"\\", "/")
    print(result)
    if os.path.isfile(result):
        if os.path.exists(path):
            # if path.find('.png') != -1:
            #     fp = open(path, "r")
            # elif path.find('.woff') != -1:
            #     fp = open(path, "r")
            #
            # else:
            #     fp = open(path, "r" ,encoding='UTF-8')
            # reply
            fp = open(path, "rb",)
            reply = fp.read()

            # reply
            # continue
            response_errno = 200
            response_msg = 'OK'
        else:
            reply = 'Not found page'
            response_errno = 404
            response_msg = 'Not found'
    else:
        reply = 'Forbidden'
        response_errno = 403
        response_msg = 'Forbidden'

    response = 'HTTP/1.1 ' + str(response_errno) + " " + response_msg + '\r\n'
    # response = 'HTTP/1.1 ' + str(response_errno) + " " + response_msg + '\r\n'
    response += "\r\n"
    response=response.encode()
    if isinstance(reply,str):
        reply=reply.encode()
    response += reply
    # print (response)

    # assces_log(request)
    conn.sendall(response)
    # conn.sendall(bytes(response, encoding = "utf8"))
    conn.close()

s.close()

