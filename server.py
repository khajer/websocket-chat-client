#!/usr/bin/env python

import asyncio
from websockets.server import serve

clients = []


async def echo(client):
    clients.append(client)
    async for message in client:
        for c in clients:
            await c.send("server: -> "+message)
        # await websocket.send(message)


async def main():
    async with serve(echo, "localhost", 8080):
        await asyncio.Future()  # run forever

asyncio.run(main())
