import asyncio

import aiohttp
from aiohttp import ClientSession

from util.async_timer import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ["https://httpbin.org/get", "python://httpbin.org/get"]
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        successful_results = [res for res in results if not isinstance(res, Exception)]

        print(f"All results: {results}")
        print(f"Finished successfully: {successful_results}")
        print(f"Threw exceptions: {exceptions}")


asyncio.run(main())
