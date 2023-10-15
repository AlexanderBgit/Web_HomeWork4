import socket
import logging


logging.basicConfig(
    level=logging.ERROR,
    filename='error.log',
    format="%(asctime)s [ %(filename)s:%(lineno)d ] %(message)s")
logger = logging.getLogger(__name__)

def run():
    host = socket.gethostname()
    port = 5000 #було 3000, тестим на 5000 

    logger.info(f"Connecting server on the port {port}")


    client_socket = socket.socket()
    client_socket.connect((host, port))
    # message = input("--> ")
    # Обробка винятку EOFError (вихід з циклу або зупинка виконання потоку)
    try:
        message = input("--> ")
    except EOFError:
    
    # або варіант     
    #     while True:
    #         message = input("--> ")
    #         client_socket.send(message.encode())    



        while message.lower().strip() != 'exit':

            client_socket.send(message.encode())

            msg = client_socket.recv(1024).decode()
            logger.info(f"Server response: {msg}")
            # print(f"Received message: {msg}")
            message = input("--> ")

        
    client_socket.close()


if __name__ == '__main__':
    run()





