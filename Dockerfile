FROM adferraro/continual_drive:latest

WORKDIR /mnt/repo

RUN apt install -y iputils-ping

RUN apt install -y iproute2

RUN apt install -y vim

RUN pip3 install pillow --break-system-packages

RUN pip3 install keyboard --break-system-packages



