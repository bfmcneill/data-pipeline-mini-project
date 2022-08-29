FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

# keep the container open
ENTRYPOINT ["tail", "-f", "/dev/null"]