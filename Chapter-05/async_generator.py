import asyncio

from util.async_timer import async_timed
from util.delay_functions import delay


async def positive_integers_async(until: int):
    for integer in range(1, until):
        await delay(integer)
        yield integer


@async_timed()
async def main():
    async_generator = positive_integers_async(3)
    print(type(async_generator))  # <class 'async_generator'>
    async for number in async_generator:
        print(f"Got number {number}")


asyncio.run(main())
