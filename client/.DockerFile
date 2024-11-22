FROM ubuntu:latest

RUN apt update &&/ apt install python3 -y &&/ apt clean

WORKDIR /client

COPY client.py .
COPY multiply.py .


EXPOSE 17000/tcp

CMD python3 client.py