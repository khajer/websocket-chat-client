#!/usr/bin/env python

from websockets.sync.client import connect
import time


def hello():
    url = "ws://localhost:8080/ws"
    with connect(url) as websocket:
        print("sent message hello, world")
        # websocket.send("send message!")

        time.sleep(3)
        websocket.send("test")
        time.sleep(4)
        websocket.send('{"cmd":"lobby", "params":{"name":"kha"}}')

        while (True):
            message = websocket.recv()
            print(f"recv:[{message}]")


hello()
