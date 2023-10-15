FROM python:3.11-slim as builder
# hub.docker.com Використовуємо базовий образ з Python

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
# WORKDIR $APP_HOME

# Робоча директорія в контейнері / Переключаємо робочу директорію
WORKDIR /app    


# Скопіюємо інші файли в робочу директорію контейнера
# COPY . .
COPY . /app

# Встановимо залежності всередині контейнера

# ENV VIRTUAL_ENV=/app/venv
# RUN python -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Встановити ваш пакет з поточної директорії
RUN pip install .

# RUN mkdir $APP_HOME/user_data
# RUN cd $APP_HOME/user_data

# WORKDIR $APP_HOME/user_data

# Позначимо порт, де працює застосунок всередині контейнера

EXPOSE 3000/tcp

VOLUME $APP_HOME/storage

# # Запустимо наш застосунок всередині контейнера
# ENTRYPOINT ["main.py"]

# Ваша команда для запуску додатка
CMD ["python", "main.py"]
