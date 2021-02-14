import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter URL here:')
url_split = url.split('/')
host = url_split[2]
mysock.connect((host, 80))
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

received = b""
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
    received = received + data

received = received.decode()
print(received[:3000])
print(len(received))

mysock.close()
