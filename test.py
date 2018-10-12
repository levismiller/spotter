import asyncio
import aiohttp


async def request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()


async def main():
    host = '192.168.86.32'
    await request(f'http://{host}:8000/ptz/30/30/0')
    await request(f'http://{host}:8000/ptz/150/30/0')
    await request(f'http://{host}:8000/ptz/150/150/0')
    await request(f'http://{host}:8000/ptz/30/30/0')


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
    loop.run_until_complete(loop.shutdown_asyncgens())
finally:
    loop.close()
