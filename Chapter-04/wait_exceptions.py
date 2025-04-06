import asyncio
import logging

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
        good_request = fetch_status(session, "https://httpbin.org/get")
        bad_request = fetch_status(session, "python://bad")

        fetchers = [asyncio.create_task(good_request), asyncio.create_task(bad_request)]

        done, pending = await asyncio.wait(fetchers)

        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "Request got an exception", exc_info=done_task.exception()
                )


asyncio.run(main())
