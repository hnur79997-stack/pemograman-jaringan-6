import socket

# Ganti dengan IP address dari laptop server
SERVER_IP = '10.42.3.50'  # contoh IP, ubah sesuai IP laptop server kamu
PORT = 6001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))

print("Terhubung ke server!")

while True:
    pesan = input("Kirim ke server: ")
    client_socket.send(pesan.encode())

    data = client_socket.recv(1024).decode()
    print(f"Balasan dari server: {data}")

client_socket.close()