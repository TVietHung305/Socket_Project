import socket


def run_client():
    host = "127.0.0.1"
    port = 8000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((host,port))

    try:
        while True:
            msg = input("Enter message: ")
            client.send(msg.encode("utf-8")[:1024])

            data = client.recv(1024)
            data = data.decode("utf-8")

            if data.lower() == "closed":
                break

            print(f"Received: {data}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Connection to server closed")


run_client()
