import socket

HOST = ''  # kosong artinya listen di semua interface (gunakan IP laptop server)
PORT = 12345  # bebas, tapi pastikan belum dipakai aplikasi lain

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server berjalan di port {PORT}, menunggu koneksi...")

conn, addr = server_socket.accept()
print(f"Terhubung dengan client: {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Pesan dari client: {data}")

    balasan = input("Balas ke client: ")
    conn.send(balasan.encode())

conn.close()
server_socket.close()