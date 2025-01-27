FROM ubuntu:latest

WORKDIR /src

COPY ./continual .

RUN apt update

RUN apt install -y python3

RUN apt install -y python3-pip

RUN pip3 install numpy pandas --break-system-packages

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu --break-system-packages
