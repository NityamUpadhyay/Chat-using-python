import socket

def start_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind to the port
        server_socket.bind((host, port))
        
        # Listen for incoming connections
        server_socket.listen(5)
        print(f"Server listening on {host}: {port}")

        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Ask for the name of the user
        client_name = client_socket.recv(1024).decode()
        print(f"{client_name} joined the chat.")
        
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            print(f"{client_name}: {data}")

            # Send a response
            message = input("You: ")
            client_socket.sendall(message.encode())

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    host = socket.gethostname()
    port = 12345
    
    start_server(host, port)
