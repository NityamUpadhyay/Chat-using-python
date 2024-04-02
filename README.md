# Chat-using-python
Python-based chat application using sockets for real-time communication. Features client-server architecture. Allows users to exchange messages over a network connection.

# Simple Chat Application

A basic chat application implemented in Python using sockets.

## Description

This project provides a simple chat application that enables real-time communication between multiple users over a network connection. It consists of two main components: a server script and a client script. The server script manages connections from multiple clients, relays messages between them, and facilitates communication in a chat room environment. The client script connects to the server, allowing users to exchange messages in a chat-like interface.

## Features

- **Client-Server Architecture**: Utilizes a client-server model for communication.
- **Real-Time Messaging**: Enables users to exchange messages in real-time.
- **Customizable**: Easily extendable and customizable for various use cases.

## Usage

1. **Clone the Repository:**

    ```
    git clone https://github.com/NityamUpadhyay/Chat-using-python.git
    ```
    
2. **Navigate to the Project Directory:**

    ```
    cd Chat-using-python
    ```

    **Edit client.py**
     1. open client.py in any editor.
     2. Go to line no. 23 and replace "your_name" with your name
     3. keep it open
     4. run ipv4 file using cmd by command "python ipv4.py"
     5. copy the ipv4 address e.g. 192.168.0.1
     6. check line no. 33 in client.py file
     7. replace Your_IPv4_Address with ipv4 address
     8. save the file
     9. exit

4. **Run the Server Script:**
    On your pc:
    ```
    python server.py
    ```

5. **Run the Client Script and Follow the Prompts:**
    Run it on client's pc
    ```
    python client.py
    ```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).
