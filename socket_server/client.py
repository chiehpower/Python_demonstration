# 準備要發送的檔案名和檔案內容
import socket

# 創建客戶端 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 連接到服務器
client_socket.connect(('0.0.0.0', 6060))

# 準備發送 XML 檔案
file_name = 'sample.xml'
with open(file_name, 'rb') as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)

# 等到所有數據傳輸完畢再關閉連接
print("檔案已發送完畢")
client_socket.shutdown(socket.SHUT_WR)  # 這一步確保數據已發送完

# 接收來自服務器的確認消息
response = client_socket.recv(1024).decode('utf-8')
print(f'來自服務器的回應: {response}')

# 關閉連接
client_socket.close()
