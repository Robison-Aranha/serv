import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("arroz", 50000))
s.listen(1)


while True:
    try:
        clientsocket.send(bytes(input(""), "utf-8"))
    except:
        clientsocket, adress = s.accept()
