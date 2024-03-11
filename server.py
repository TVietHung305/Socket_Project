import socket
import threading

def handle_client(client_socket, addr):
    try:
        while True:
            data = client_socket.recv(1024).decode("utf-8")
            if data.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                break
            print(f"Received: {data}")
            response = "accepted"
            client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")
def run_server():
    host = "127.0.0.1"  #server hostname
    port = 8000         #server port number

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen()
        print(f"Listening on {host}:{port}")

        while True:
            client_socket, addr = s.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            thread = threading.Thread(target=handle_client, args=(client_socket,addr))
            thread.start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

run_server()