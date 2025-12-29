import socket
import json
import uuid
import time

SERVER_IP = "50.16.37.231"
PORT = 5000
TIMEOUT = 2
RETRIES = 3

request = {
    "request_id": str(uuid.uuid4()),
    "method": "add",
    "params": {"a": 5, "b": 7}
}

for attempt in range(RETRIES):
    try:
        print(f"Attempt {attempt + 1}")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(TIMEOUT)

        client.connect((SERVER_IP, PORT))
        client.send(json.dumps(request).encode())

        response = client.recv(1024).decode()
        response = json.loads(response)

        print("Response:", response)
        client.close()
        break

    except socket.timeout:
        print("Timeout occurred, retrying...")
    except Exception as e:
        print("Error:", e)

else:
    print("RPC failed after retries")
