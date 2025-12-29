import socket
import json
import time

HOST = "0.0.0.0"
PORT = 5000

def add(a, b):
    return a + b

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("RPC Server started on port", PORT)

while True:
    conn, addr = server.accept()
    print("Connected by", addr)

    data = conn.recv(1024).decode()
    request = json.loads(data)

    print("Request:", request)

    # искусственная задержка (для демонстрации ошибки)
    # time.sleep(5)

    method = request["method"]
    params = request["params"]

    if method == "add":
        result = add(params["a"], params["b"])
    else:
        result = "Unknown method"

    response = {
        "request_id": request["request_id"],
        "result": result,
        "status": "OK"
    }

    conn.send(json.dumps(response).encode())
    conn.close()
