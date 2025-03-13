import socket;
import threading;

Host = 'localhost'
Port = 19000

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    thread1 = threading.Thread(target=serverInit, args=[server, Host, Port])
    thread2 = threading.Thread(target=clientInit, args=[client])

    thread1.start()
    thread2.start()

def serverInit(server, Host, Port):
    try:
        server.bind((Host, Port))
        print("Esperando conexoes...")
        server.listen()
        client, addr = server.accept()
        msg = "você se conectou!"
        client.send(msg.encode())
    except:
        return print("Não foi possível iniciar o servidor.")

def clientInit(client):
    while True:
        try:
            client.connect(('localhost', 20000))
            msg = client.recv(2048)
            print(msg.decode())
        except:
            return

main()