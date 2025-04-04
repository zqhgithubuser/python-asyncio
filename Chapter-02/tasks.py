import asyncio

from util.delay_functions import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    print("I'm running other code while I'm waiting!")
    await sleep_for_three
    await sleep_again
    await sleep_once_more


asyncio.run(main())
