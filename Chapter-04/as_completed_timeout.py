import asyncio

import aiohttp
from aiohttp import ClientSession

from util.async_timer import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, "https://httpbin.org/get", 1),
            fetch_status(session, "https://httpbin.org/get", 10),
            fetch_status(session, "https://httpbin.org/get", 10),
        ]
        # 先完成先打印
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("We got a timeout error!")

        for task in asyncio.all_tasks():
            print(task)


asyncio.run(main())
