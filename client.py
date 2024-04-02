import socket

def connect_to_server(server_address, port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((server_address, port))
        print("Connected to the server.")
        
        # Ask for the name of the user
        client_name = input("Enter your name: ")
        client_socket.sendall(client_name.encode())
        
        while True:
            # Send a message to the server
            message = input("You: ")
            client_socket.sendall(message.encode())

            # Receive a response from the server
            data = client_socket.recv(1024).decode()
            print(f"your_name: {data}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    server_address = "Your_IPv4_Address"  # Replace with the actual server address
    port = 12345
    
    connect_to_server(server_address, port)
