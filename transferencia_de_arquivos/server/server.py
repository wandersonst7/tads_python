import socket;

# Definindo socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 50000))
server.listen()
print("Arquivo online!")

def enviaArquivo(conn, addr):
    # Nome do arquivo online
    f = 'arquivo.txt'

    # Enviando nome do arquivo
    conn.send(f.encode())

    # Enviando arquivos
    with open(f, 'rb') as file:
        for data in file.readlines():
            conn.send(data)
        print(f ,"foi enviado para ", addr[0])

    # Fechando conexão
    conn.close()

while True:
    conn, addr = server.accept()
    enviaArquivo(conn, addr)

