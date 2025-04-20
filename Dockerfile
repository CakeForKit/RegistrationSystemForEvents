# Используем базовый образ с Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем все необходимые зависимости для линтинга и тестов
RUN pip install --no-cache-dir flake8 pylint pytest pytest-asyncio sqlalchemy pydantic asyncpg pytest-cov


COPY src /app/src
COPY src/tests /app/src/tests
COPY ./deployment/tests /app/tests

ENV PYTHONPATH=/app/src

# Делаем test.sh исполняемым
RUN ls
RUN chmod +x /app/tests/test.sh

# Запуск тестов
ENTRYPOINT ["/app/tests/test.sh"]
