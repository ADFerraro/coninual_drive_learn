FROM adferraro/continual_drive:latest

WORKDIR /mnt

RUN pip3 install keyboard --break-system-packages

RUN mkdir images

WORKDIR /mnt/repo
