FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    curl

COPY app/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN curl -o /usr/local/bin/wait-for-it https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod +x /usr/local/bin/wait-for-it

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

