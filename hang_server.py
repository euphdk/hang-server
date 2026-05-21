#!/usr/bin/env python3

import socket
import threading
import time

HOST = "0.0.0.0"
PORT = 22


def handle_client(conn, addr):
    print(f"Accepted connection from {addr}", flush=True)

    try:
        while True:
            time.sleep(3600)
    finally:
        conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Listening on {HOST}:{PORT}", flush=True)

    while True:
        conn, addr = server.accept()
        threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True,
        ).start()
