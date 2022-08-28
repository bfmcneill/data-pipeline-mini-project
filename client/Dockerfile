FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

# keep the container open
ENTRYPOINT ["tail", "-f", "/dev/null"]