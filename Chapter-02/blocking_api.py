import asyncio

import requests

from util.async_timer import async_timed


@async_timed()
async def get_example_status() -> int:
    # requests 库本身是阻塞的
    return requests.get("http://www.example.com").status_code


@async_timed()
async def main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())
    await task_1
    await task_2
    await task_3


asyncio.run(main())
