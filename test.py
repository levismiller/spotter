import asyncio
from time import sleep

import aiohttp


async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


async def main():
    await request('http://192.168.86.32:8000/ptz/30/30/0')
    await request('http://192.168.86.32:8000/ptz/35/30/0')
    await request('http://192.168.86.32:8000/ptz/40/30/0')
    await request('http://192.168.86.32:8000/ptz/45/30/0')
    await request('http://192.168.86.32:8000/ptz/50/30/0')
    await request('http://192.168.86.32:8000/ptz/55/30/0')
    await request('http://192.168.86.32:8000/ptz/60/30/0')

    sleep(1)
    await request('http://192.168.86.32:8000/ptz/30/30/0')

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
    loop.run_until_complete(loop.shutdown_asyncgens())
finally:
    loop.close()