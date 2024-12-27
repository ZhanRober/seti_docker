# Используем Python для backend
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Копируем файлы для установки зависимостей
COPY requirements.txt ./

# Устанавливаем Python-зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы
COPY . .

# Указываем порт
EXPOSE 5000

# Команда запуска
CMD ["python", "app.py"]