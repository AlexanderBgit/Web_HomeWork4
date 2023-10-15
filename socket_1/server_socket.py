import socket
import logging


logging.basicConfig(
    level=logging.ERROR,
    filename='error.log',
    format="%(asctime)s [ %(filename)s:%(lineno)d ] %(message)s")
logger = logging.getLogger(__name__)



# створіть Socket сервер на порту 5000
def run():
    host = socket.gethostname()
    port = 5000

    logger.info(f"Server received on the port {port}")


    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()

    conn, address = server_socket.accept()
    c_host, c_port = address
    logger.info(f"Connection  {c_host}:{c_port}")
    # print(f"Connection from: {address}")


    while True:
        msg = conn.recv(100).decode()
        if not msg:
            break
        logger.info(f"Message {c_host}:{c_port}: {msg}")
        # print(f"Received messages: {msg}")


        message = input("--> ")
        conn.send(message.encode())
    conn.close()
    server_socket.close()


if __name__ == '__main__':
    run()
