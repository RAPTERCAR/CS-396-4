FROM ubuntu:latest

RUN apt update &&/ apt install python3 -y &&/ apt clean

WORKDIR /client

COPY client.py .



EXPOSE 15002/tcp

CMD python3 client.py