import os
import json
import socket
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import threading

app = Flask(__name__)

# збереження повідомлень data.json
def save_message(username, message):
    now = str(datetime.now())
    data = {
        now: {
            "username": username,
            # "message": message
            "message": message.encode('utf-8').decode('unicode_escape')
        }
    }

    if os.path.exists('storage/data.json'):
        with open('storage/data.json', 'r') as file:
            try:
                existing_data = json.load(file)
                if not isinstance(existing_data, dict):
                    # Якщо не є словником, новий словник
                    existing_data = {}
                existing_data.update(data)
                data = existing_data
            except json.JSONDecodeError:
                pass

    with open('storage/data.json', 'w') as file:
        json.dump(data, file, indent=4)



# Основна сторінка
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        # дані з форми
        username = request.form['username']
        message = request.form['message']

        # збереження даних
        save_message(username, message)

    return render_template('message.html')


# Сервер прийому даних
def socket_server():
    host = '127.0.0.1'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f'Socket server listening on {host}:{port}')

        while True:
            data, addr = server_socket.recvfrom(1024)
            message = data.decode('utf-8')
            username, message = message.split(',')
            save_message(username, message)

# Запуск в потоках
if __name__ == '__main__':
    

    # Запуск сервера сокетів у окремому потоці
    socket_thread = threading.Thread(target=socket_server)
    socket_thread.start()

    # Запуск веб-сервера
    app.run(host='0.0.0.0', port=3000)
