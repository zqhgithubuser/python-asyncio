import asyncio
import logging

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
            asyncio.create_task(fetch_status(session, "python://bad.com")),
            asyncio.create_task(
                fetch_status(session, "https://httpbin.org/get", delay=3)
            ),
            asyncio.create_task(
                fetch_status(session, "https://httpbin.org/get", delay=3)
            ),
        ]
        # 异常立即返回
        done, pending = await asyncio.wait(
            fetchers, return_when=asyncio.FIRST_EXCEPTION
        )

        print(f"Done task count: {len(done)}")
        print(f"Pending task count: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "Request got an exception", exc_info=done_task.exception()
                )

        for pending_task in pending:
            pending_task.cancel()


asyncio.run(main())
