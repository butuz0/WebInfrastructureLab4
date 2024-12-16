FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential

COPY app/requirements.txt requirements.txt
COPY wait-for-it.sh /usr/local/bin/wait-for-it
RUN pip install --no-cache-dir -r requirements.txt

