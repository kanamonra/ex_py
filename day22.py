import socket
print("에코 클라이언트 시작됨")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # used TCP
client_socket.connect(("165.246.115.165", 20000))
print("서버에 연결됨")

while True:
    message = input("전송 메세지 입력 :")
    if message == "exit" or message == "quit":
        break
    client_socket.sendall((message + "\n").encode())  # encode
    data = client_socket.recv(1024).decode()   # decode
    print(f"서버로 부터 받은 메세지 : {data}")

client_socket.close()
