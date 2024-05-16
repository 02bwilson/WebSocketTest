#!/usr/bin/env python

import asyncio
import random

from scipy.fft import fft

from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        data = [random.random() for _ in range(1024)]
        data = fft(data)
        data = [abs(x) for x in data]
        data = data[1:]
        await websocket.send(str(list(data)))

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())