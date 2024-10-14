import socket

# 創建socket對象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Server_Port = 6060

# 綁定IP和端口
server_socket.bind(('0.0.0.0', Server_Port))

# 監聽連接
server_socket.listen(5)
print('等待客戶端連接...')

while True:
    # 接受客戶端連接
    client_socket, address = server_socket.accept()
    print(f'連接來自: {address}')

    # 開始接收數據並寫入文件
    with open('接收的檔案.xml', 'wb') as f:
        while True:
            # 接收數據（每次接收1024字節）
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)

    print('檔案已接收並儲存')

    # 回應客戶端
    client_socket.send('檔案已接收'.encode('utf-8'))

    # 正確關閉連接
    client_socket.close()
