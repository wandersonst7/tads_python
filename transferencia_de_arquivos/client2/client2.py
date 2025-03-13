import socket;

# Definindo client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando o servidor
client.connect(('localhost', 50000))
print("Conectado!")

# Recebendo nome do arquivo
namef = client.recv(2048).decode()

# Baixando arquivo do servidor
with open(namef, 'wb') as file:
    while True:
        data = client.recv(1000000)

        # Verifica se ainda tem dados para baixar.
        if not data:
            break

        file.write(data)

print(namef ,"foi baixado!")


