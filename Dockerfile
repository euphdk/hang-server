FROM python:3.14-alpine

WORKDIR /app

COPY hang_server.py .

EXPOSE 22

CMD ["python", "/app/hang_server.py"]
