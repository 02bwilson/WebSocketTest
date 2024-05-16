#!/usr/bin/env python

import asyncio
import random

from scipy.fft import fft
import numpy as np

from websockets.server import serve
m = 1
async def echo(websocket):
    async for message in websocket:
        global m
        if message.startswith("SF"):

            freq = message[2:]
            freq = int(freq)
            m = freq
            print(freq)
            # TUNE


        # Begin to build the data
        data = np.array([random.random() for _ in range(1024)])
        data = fft(data)

        data = [abs(x) + m for x in data]
        data = data[1:]


        await websocket.send(str(list(data)))

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())