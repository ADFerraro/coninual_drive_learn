FROM adferraro/continual_drive:latest

WORKDIR /src

COPY ./continual .

CMD ["python3", "main.py"]
