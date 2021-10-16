import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("arroz", 50000))
s.listen(1)


while True:
    clientsocket, adress = s.accept()
    try:
        clientsocket.send(bytes(input(""), "utf-8"))
    except:
        pass
