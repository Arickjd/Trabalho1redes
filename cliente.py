import socket
import threading

# Decisões da Turma

HEADER = 64
PORT = 18000
SERVER = '192.168.100.254'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = ':D'

# Criando um socket do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)  # conectando ao servidor

def receive():
    while True:
        try:
            msg = client.recv(2048).decode(FORMAT)  # Recebe mensagens do servidor
            if msg:
                print(msg)  # Exibe a mensagem recebida
        except ConnectionResetError:
            print("A conexão com o servidor foi encerrada.")
            break

def send(client_socket, msg):
    # client = 'arick'
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client_socket.send(send_len)  # Envia o tamanho da mensagem
    client_socket.send(message)  # Envia a mensagem

# Inicia uma thread para receber mensagens do servidor
receive_thread = threading.Thread(target=receive)
receive_thread.start()

while True:
    entry = input('Sua mensagem: ')
    send(client, entry)  # Chama a função "send" com o socket do cliente e a mensagem

    if entry == DISCONNECT_MESSAGE:
        print("Desconectando...")
        break

client.close()  # Fecha o socket