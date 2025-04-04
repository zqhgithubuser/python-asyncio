import asyncio

from util.delay_functions import delay


def call_later():
    print("I'm being called in the future!")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(2)


asyncio.run(main())
