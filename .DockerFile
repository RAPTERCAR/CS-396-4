FROM ubuntu:latest

RUN apt update &&/ apt install python3 -y &&/ apt clean

WORKDIR /CS-360-2

COPY client.py .
COPY multiply.py .


EXPOSE 17000/tcp

CMD python3 client.py